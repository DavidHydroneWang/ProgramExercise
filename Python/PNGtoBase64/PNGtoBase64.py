#!/usr/bin/env python
# coding=utf-8

import base64

fin = open("temp.png", "rb")
fout = open("temp.txt", "w")
base64.encode(fin, fout)
# temp = ''
# test = bytes(fout)
# temp = base64.b64encode(test)
# print(temp)
fin.close()
fout.close()

#with open("temp.txt", "r") as f:
#    for line in f.readlines():
#        line = line.strip('\n')
#        print(line)
with open("out.txt", "w") as f2:
    with open("temp.txt", "r") as f:
        temp = ''
        for line in f.readlines():
            temp += line.strip('\n')
        for l in temp:
            f2.write(l)
    f.close()
f2.close()
