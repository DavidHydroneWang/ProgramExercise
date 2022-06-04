#!/usr/bin/env python
# coding=utf-8
import urllib.error
import urllib.parse
import urllib.request
from anon_browser import *


def google(search_item):
    ab = AnonBrowser()
    search_item = urllib.parse.quote_plus(search_item)
    reponse = ab.open(f'http://ajax.googleapis.com/ajax/services/search/web'
                      f'?v=1.0&q={search_item}')
    print(reponse.read())


if __name__ == '__main__':
    google('Boondock Saint')
