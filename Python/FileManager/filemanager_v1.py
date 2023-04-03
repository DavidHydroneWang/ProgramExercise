#!/usr/bin/env python3
# coding=utf-8
import os, re, sys, math

#def remove_punctuation(line, strip_all=False):
#    if strip_all:
#        rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
#        line = rule.sub('',line)
#    else:
#        punctuation = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏"""
#        re_punctuation = "[{}]+".format(punctuation)
#        line = re.sub(re_punctuation, "", line)
#    return line.strip()


def filemanager():
#    current_path = os.path.abspath('.')
#    father_path = os.path.abspath('..')
    destinationr_path = '/home/wss/test/'
    os.chdir(destinationr_path)
#    print(destinationr_path)
    path = os.listdir(destinationr_path)
    year = os.popen('date +%Y').read()
    if not  os.path.exists(str(year).rstrip('\n')):
        os.system('mkdir ' + str(year))
    os.chdir(str(year).rstrip('\n'))
    month = os.popen('date +%m').read()
    if not  os.path.exists(str(month).rstrip('\n')):
        os.system('mkdir ' + str(month))
#    os.system('mkdir ' + str(month))
    os.chdir(str(month).rstrip('\n'))
    day = os.popen('date +%d').read()
    if not  os.path.exists(str(day).rstrip('\n')):
        os.system('mkdir ' + str(day))
#    os.system('mkdir ' + str(day))
#    os.chdir(str(day).rstrip('\n'))
    os.chdir(destinationr_path)
    name = os.popen('date +%Y/%m/%d ').read()
    No_File = False
#    print(name)
    for i in path:
        if os.path.isfile(i):
            No_File = True
#        else:
#            No_File = False
    if No_File:
        for i in path:
            if os.path.isfile(i):
                os.system('mv ' + i + ' ' + name)
                print('Ok')
    else:
        if not os.listdir(name.rstrip('\n')):
            os.system('rm  -rf ' + str(year).rstrip('\n') + '/' + str(month).rstrip('\n') + '/' + str(day).rstrip('\n'))
#        os.system('rm  -rf ' +  str(year).rstrip('\n') + '/' + str(month).rstrip('\n') + '/' + str(day).rstrip('\n') )
            print('No File')
#    for i in path:
#        if os.path.isfile(i):
#            os.system('mv ' + i + ' ' + name)
#            print('Ok')
#        else:
#            os.system('rm  -rf ' +  str(year).rstrip('\n') + '/' + str(month).rstrip('\n') + '/' + str(day).rstrip('\n') )
#            print('No File')
#                print(num)
#    os.chdir(father_path)


if __name__ == "__main__":
    filemanager()
