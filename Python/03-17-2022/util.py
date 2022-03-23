#!/usr/bin/env python
# coding=utf-8


def lines(file):
    for line in file:
        yield line
#        print(line)
    yield '\n'
#    print(line)


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
#            print(line)
#            print(block)
        elif block:
            yield ''.join(block).strip()
#            print(line)
#            print(block)
            block = []
