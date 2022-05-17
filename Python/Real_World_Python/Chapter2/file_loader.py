#!/usr/bin/env python
# coding=utf-8


def text_to_string(filename):
    strings = []
    with open(filename, encoding='utf-8', errors='ignore') as f:
        strings.append(f.read())
    return '\n'.join(strings)
