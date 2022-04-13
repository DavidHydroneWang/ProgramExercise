#!/usr/bin/env python
# coding=utf-8
import os,re,sys,math


class PathHandler:
    """
    分别对文件和文件夹进行处理
    """

    def __init__(self):
        self.path = os.listdir(os.getcwd())
        self.fatherpath = os.getcwd()

    def Change(self):
#        print(self.path)
        for i in self.path:
            if os.path.isfile(i):
                name = i
                name = re.sub(r'[\*>#？：，：。、【】:\?,\n\t]','',name)
                name = re.sub(r'\s','',name)
                name = re.sub(r'[\（]','(',name)
                name = re.sub(r'[\）]',')',name)
                temp = name.split('.')
                newname = ""
                for l in range(0,len(temp)-1):
                    newname += temp[l]
                newname = newname.partition("by")[0]
                newname += "."
                newname += temp[-1]
                os.rename(i,newname)
            else:
#                print(i)
#                print(str(i))
                os.chdir(str(i))
                inside_change = PathHandler()
                inside_change.Change()
                os.chdir(self.fatherpath)


if __name__ == "__main__":
    chang = PathHandler()
    chang.Change()
