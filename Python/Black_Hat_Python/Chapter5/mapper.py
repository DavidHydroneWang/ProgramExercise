#!/usr/bin/env python
# coding=utf-8
import contexlib
import os
import queue
import resquest
import sys
import threading
import time

FILTERED = ['.jpg', '.gif', '.png', '.css']
TARGET = 'http://boodelyboo.com/wordpress'
THREADS = 10

answers = queue.Queue()
web_paths = queue.Queue()


def gather_paths():
    for root, _, files in os.walk('.'):
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERED:
                continue
            path = os.path.join(root, fname)
            if path.startswith('.'):
                path = path[1:]
            print(path)
            web_paths.put(path)


@contexlib.contextmanager
def chdir(path):
    """
    On enter, change directory to specified path.
    On exit, change directory to original.
    """
    this_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(this_dir)


def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = f'{TARGET}{path}'
        time.sleep(2)
        r = resquest.get(url)
        if r.status_code = 200:
            answers.put(url)
            sys.stdout.write('+')
        else:
            sys.stdout.write('x')
        sys.stdout.flush()


def run():
    mythreads = list()
    for i in range(THREADS):
        print(f'Spawing thread {i}')
        t = threading.Thread(target=test_remote)
        mythreads.append(t)
        t.start()

    for thread in mythreads:
        thread.join()


if __name__ == '__main__':
    with chdir('/home/wss/downloads/wordpress'):
        gather_paths()
    input('Press return to continue.')

    run()
    with open('myanswer.txt', 'w') as file:
        while not answers.empty():
            f.write(f'{answers.get()}\n')
    print('done')
