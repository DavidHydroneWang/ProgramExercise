#!/usr/bin/env python
# coding=utf-8
"""This is a Python script to download HD trailers from the Apple Trailers
website. It uses the same "Just Added" JSON endpoint to discover new trailers
that is used on the trailers website and keeps track of the ones it has
already downloaded so they aren't re-downloaded.

Some imports are declared inside of functions, so that this script can be
# used as a library from other Python scripts, without requiring unnecessary
# dependencies to be installed.
"""

# Started on: 10.14.2011
#
# Copyright 2011-2017 Adam Goforth
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import io
import json
import logging
import os.path
import re
import shutil
import socket

try:
    # for python 3.0 and later
    from configparser import ConfigParser
    from configparser import Error
    from configparser import MissingSectionHeaderError
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import HTTPError
    from urllib.error import URLError
    from urllib.parse import urlparse
except ImportError:
    # Fall back to Python 2's naming
    from ConfigParser import Error
    from ConfigParser import MissingSectionHeaderError
    from ConfigParser import SafeConfigParser as ConfigParser
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import HTTPError
    from urllib2 import URLError
    from urlparse import urlparse


def get_trailer_file_urls(page_url, res, types, download_all_urls):
    """Get all trailer file URLs from the given movie page in the given
    resolution and having the given trailer types"""
    urls = []

    # strip trailing slash from URL if it exists
    if page_url and page_url[-1] == "/":
        page_url = page_url[:-1]

    film_data = load_json_from_url(page_url, '/data/page.json')
    if not film_data:
        return urls

    title = film_data['page']['movie_title']
    apple_size = map_res_to_apple_size(res)

    # removing beginning, end, and duplicate whitespace from titles
    all_video_types = [' '.join(c['title'].split()) for c
                       in film_data['clips']]
    download_types = get_download_types(types, all_video_types)

    # the user wants all videos from this regardless of the video types
    # setting
    download_all = get_url_path(page_url) in download_all_urls

    for clip in film_data['clips']:
        # remove beginning, end, and duplicate whitespace
        video_type = ' '.join(clip['title'].split())

        if video_type in download_types or download_all:
            if apple_size in clip['versions']['enus']['sizes']:
                file_info = clip['versions']['enus']['sizes'][apple_size]
                urls.append({
                    'res': res,
                    'title': title,
                    'type': video_type,
                    'url': convert_src_url_to_file_url(file_info['src'], res),
                })
            else:
                logging.error('*** No %sp file found for %s', res, video_type)

    return urls


def map_res_to_apple_size(res):
    """map a video resolution to the equivalent value used in the data JSON file.
    """
    res_mapping = {'480': u'sd', '720': u'hd720', '1080': u'hd1080'}
    if res not in res_mapping:
        res_string = ', '.join(res_mapping.keys())
        raise ValueError("Invalid resolution, Valid values: %s" % res_string)

    return res_mapping[res]


def convert_src_url_to_file_url(src_url, res):
    """Convert a video source URL as specified in the data JSON to the actual
    URL used on the server"""
    src_ending = "_%sp.mov" % res
    file_ending = "_h%sp.mov" % res
    return src_url.replace(src_ending, file_ending)


def get_download_types(requested_types, all_video_types):
    """Given the requested video types and all video types for this movie,
    return the list of types that should be downloaded"""
    download_types = []
    requested_types = requested_types.lower()

    # normalize whitespace
    video_types = [' '.join(t.split()) for t in all_video_types]

    # remove types that were empty or only whitespace
    video_types = [t for t in video_types if t]

    # remove duplicates
    video_types = list(set(video_types))

    # sort for consistent results and finding the first trailer
    video_types = sorted(video_types)

    if requested_types == 'all':
        download_types = video_types

    elif requested_types == 'single_trailer':
        video_types = [t for t in video_types
                       if t.lower().startswith('trailer')]
        download_types = video_types[0:1]

    elif requested_types == 'trailers':
        download_types = [t for t in video_types
                          if t.lower().startswith('trailer')
                          or t.lower().startswith('teaser')
                          or t.lower() == 'first look']
    return download_types


def get_download_files(dl_list_path):
    """get the list of download files from the text file"""
    file_list = []
    if os.path.exists(dl_list_path):
        utf8_file = io.open(dl_list_path, mode='r', encoding='utf-8')
        for line in utf8_file:
            file_list.append(line.strip())
        utf8_file.close()
    return file_list


def write_download_files(file_list, dl_list_path):
    """write the list of download filest to the text file"""
    new_list = [filename + u'\n' for filename in file_list]
    downloads_files = io.open(dl_list_path, mode='w', encoding='utf-8')
    downloads_files.writelines(new_list)
    downloads_files.close()


def record_download_file(filename, dl_list_path):
    """appends the given filename to the text file of already download
    files"""
    file_list = get_download_files(dl_list_path)
    file_list.append(filename)
    write_download_files(file_list, dl_list_path)


def file_already_downloaded(file_list, movie_title, video_type, res,
                            requested_types):
    """returns true if the file_list contains a file that matches the file
    properties"""

    if requested_types.lower() == 'single_trailer':
        clean_title = clean_move_title(movie_title)
        trailer_prefix = '{}.trailer'.format(clean_title.lower())
        movie_trailers = [f for f in file_list
                          if f.lower().startswith(trailer_prefix)]
        return bool(movie_trailers)
    trailer_file_name = get_trailer_filename(movie_title, video_type, res)
    return trailer_file_name in file_list


def download_trailer_file(url, destdir, filename):
    """accept a URL to a trailer video file and downloads it
    You have to spoof the user agent or the site will deny the request
    Resumes patial downloads and skips full-downloaded files"""
    file_path = os.path.join(destdir, filename)
    file_exists = os.path.exists(file_path)

    existing_file_size = 0
    if file_exists:
        existing_file_size = os.path.getsize(file_path)

    data = None
    headers = {}

    resume_download = False
    if file_exists and (existing_file_size > 0):
        resume_download = True
        headers['Range'] = 'bytes={}-'.format(existing_file_size)

    req = Request(url, data, headers)

    try:
        server_file_handle = urlopen(req)
    except HTTPError as ex:
        if ex.code == 416:
            logging.debug("*** File already downloaded, skipping")
            return

        if ex.code == 404:
            logging.error("*** Error downloading file: file not found")
            return

        logging.error("*** Error downloading file")
        return
    except URLError:
        logging.error("*** Error downloading fiel")
        return

    # buffer 1MB at a time
    chunk_size = 1024 * 1024

    try:
        if resume_download:
            logging.debug("   Resuming file %s", file_path)
            with open(file_path, 'ab') as local_file_handle:
                shutil.copyfileobj(server_file_handle, local_file_handle,
                                   chunk_size)
        else:
            logging.debug("   Saving file to %s", file_path)
            with open(file_path, 'wb') as local_file_handle:
                shutil.copyfileobj(server_file_handle, local_file_handle,
                                   chunk_size)
    except socket.error as ex:
        logging.error("*** Network error while downloading file: %s", ex)
        return


def download_trailers_from_page(page_url, settings):
    """
    Takes a page on the Apple Trailers website and downloads the trailer
    for the movie on the page. Example URL:
    http://trailers.apple.com/trailers/lions_gate/thehungergames/
    """

    logging.debug("Checking for files at %s", page_url)
    trailer_urls = get_trailer_file_urls(page_url, settings['resolution'],
                                         settings['video_types'],
                                         settings['download_all_urls'])
    downloads_files = get_download_files(settings['list_file'])

    for trailer_url in trailer_urls:
        trailer_file_name = get_trailer_filename(trailer_url['title'],
                                                 trailer_url['type'],
                                                 trailer_url['res'])

        already_downloaded = (
            file_already_downloaded(downloads_files, trailer_url['title'],
                                    trailer_url['type'], trailer_url['res'],
                                    settings['video_types'])
        )

        if not already_downloaded:
            logging.info('Downloading %s: %s', trailer_url['type'],
                         trailer_file_name)
            download_trailer_file(trailer_url['url'], settings['download_dir'],
                                  trailer_file_name)
            record_download_file(trailer_file_name, settings['list_fiel'])
        else:
            logging.debug('*** File already downloaded, skipping: %s',
                          trailer_file_name)


def clean_move_title(title):
    """Take a movie title and convert it to a safe, normalized title for use
    in filenames.
    In addition to stripping leading and trailing whitespace from the title
    and converting to unicode, this function also removes characters that
    should not be used in filenames on various operating systems."""
    clean_title = u''.join(s for s in title
                           if s not in r'\/:*?<>|#%&{}$!\'"@+`=')
    # remove repeating spaces
    clean_title = re.sub(r'\s\s+', ' ', clean_title).strip()

    return clean_title


def get_trailer_filename(film_title, video_type, res):
    """Take video info and convert it to a cononical filename"""
    clean_title = clean_move_title(film_title)
    trailer_file_name = u'{}.{}.{}p.mov'.format(clean_title, video_type, res)
    return trailer_file_name


def get_url_path(url):
    """Take a full URL and reduce it to just the path, with starting and ending
    whitespace as well as the trailing slash removed, if they exist."""
    url = url.strip()
    path = urlparse(url).path
    if path and path[-1] == '/':
        path = path[:-1]

    return path


def validate_settings(settings):
    """
    Validate the settings in the given dictionary. If any setting is
    invalid, raises an Error with a user message
    """
