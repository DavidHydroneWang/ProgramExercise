#!/usr/bin/env python
# coding=utf-8

import re

input = ['asdgaf1_hsg534', 'asdfh23_hsjd12', 'dgshg_jhfsd86']

for s in input:
 print( re.sub('.*?([0-9]*)$',r'\1',s))

