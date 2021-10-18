#!/usr/bin/env python
# coding=utf-8
import os,re,sys,math


#def remove_punctuation(line):
#    rule = re.compile(r"\[^\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]")
#    line = rule.sub('',line)
#    return line
#def remove_punctuation(line, strip_all=False):
#    if strip_all:
#        rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
#        line = rule.sub('',line)
#    else:
#        punctuation = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏"""
#        re_punctuation = "[{}]+".format(punctuation)
#        line = re.sub(re_punctuation, "", line)
#
#    return line.strip()

def changename():
    current_path = os.path.abspath('.')
#    father_path = os.path.abspath('..')
    father_path = os.getcwd()
    path = os.listdir(os.getcwd())
    for i in path:
        if os.path.isfile(i):
            if os.path.splitext(i)[1] == ".pdf":
                name = i
                temp = name.split('.')
                num = len(temp)-1
                for j in range(0,len(temp)):
                    temp[j] = temp[j].replace('？', "")
                    temp[j] = temp[j].replace('：', "")
                    temp[j] = temp[j].replace("]", "")
                    temp[j] = temp[j].replace("[", "")
                    temp[j] = temp[j].replace("，", "")
                    temp[j] = temp[j].replace("：", "")
                    temp[j] = temp[j].replace("。", "")
                    temp[j] = temp[j].replace("、", "")
                    temp[j] = temp[j].replace("【", "")
                    temp[j] = temp[j].replace("】", "")
                    temp[j] = temp[j].replace("(", "")
                    temp[j] = temp[j].replace(")", "")
                    temp[j] = temp[j].replace(":", "")
                    temp[j] = temp[j].replace(":", "")
                    temp[j] = temp[j].replace("\?", "")
                    temp[j] = temp[j].replace(" ", "")
                    temp[j] = temp[j].replace(" ", "")
                    temp[j] = temp[j].replace(",", "")
                    temp[j] = temp[j].replace("\n", "")
                    temp[j] = temp[j].replace(":", "")
                    temp[j] = temp[j].replace("\t", "")
                newname = ""
                for l in range(0,len(temp)-1):
                    newname += temp[l]
                newname = newname.partition("by")[0]
                newname += '.pdf'
                os.rename(i,newname)
#                print(num)
#                print(temp)
#                print(newname)
            if os.path.splitext(i)[1] == ".epub":
                name = i
                temp = name.split('.')
                num = len(temp)-1
                for j in range(0,len(temp)):
                    temp[j] = temp[j].replace('？', "")
                    temp[j] = temp[j].replace('：', "")
                    temp[j] = temp[j].replace("]", "")
                    temp[j] = temp[j].replace("[", "")
                    temp[j] = temp[j].replace("，", "")
                    temp[j] = temp[j].replace("：", "")
                    temp[j] = temp[j].replace("。", "")
                    temp[j] = temp[j].replace("、", "")
                    temp[j] = temp[j].replace("【", "")
                    temp[j] = temp[j].replace("】", "")
                    temp[j] = temp[j].replace("(", "")
                    temp[j] = temp[j].replace(")", "")
                    temp[j] = temp[j].replace(":", "")
                    temp[j] = temp[j].replace(":", "")
                    temp[j] = temp[j].replace("\?", "")
                    temp[j] = temp[j].replace(" ", "")
                    temp[j] = temp[j].replace(" ", "")
                    temp[j] = temp[j].replace(",", "")
                    temp[j] = temp[j].replace("\n", "")
                    temp[j] = temp[j].replace(":", "")
                    temp[j] = temp[j].replace("\t", "")
                newname = ""
                for l in range(0,len(temp)-1):
                    newname += temp[l]
                newname = newname.partition("by")[0]
                newname += '.epub'
                os.rename(i,newname)
            if os.path.splitext(i)[1] == ".mobi":
                name = i
                temp = name.split('.')
                num = len(temp)-1
                for j in range(0,len(temp)):
                    temp[j] = temp[j].replace('？', "")
                    temp[j] = temp[j].replace('：', "")
                    temp[j] = temp[j].replace("]", "")
                    temp[j] = temp[j].replace("[", "")
                    temp[j] = temp[j].replace("，", "")
                    temp[j] = temp[j].replace("：", "")
                    temp[j] = temp[j].replace("。", "")
                    temp[j] = temp[j].replace("、", "")
                    temp[j] = temp[j].replace("【", "")
                    temp[j] = temp[j].replace("】", "")
                    temp[j] = temp[j].replace("(", "")
                    temp[j] = temp[j].replace(")", "")
                    temp[j] = temp[j].replace(":", "")
                    temp[j] = temp[j].replace(":", "")
                    temp[j] = temp[j].replace("\?", "")
                    temp[j] = temp[j].replace(" ", "")
                    temp[j] = temp[j].replace(" ", "")
                    temp[j] = temp[j].replace(",", "")
                    temp[j] = temp[j].replace("\n", "")
                    temp[j] = temp[j].replace(":", "")
                    temp[j] = temp[j].replace("\t", "")
                newname = ""
                for l in range(0,len(temp)-1):
                    newname += temp[l]
                newname = newname.partition("by")[0]
                newname += '.mobi'
                os.rename(i,newname)
            if os.path.isdir(i):
                os.chdir(str(i))
                path1 = os.listdir(os.getcwd())
                father_path1 = os.getcwd()
                for i in path1:
                    if os.path.isfile(i):
                        if os.path.splitext(i)[1] == ".pdf":
                            name = i
                            temp = name.split('.')
                            num = len(temp)-1
                            for j in range(0,len(temp)):
                                temp[j] = temp[j].replace("]", "")
                                temp[j] = temp[j].replace("[", "")
                                temp[j] = temp[j].replace("(", "")
                                temp[j] = temp[j].replace(")", "")
                                temp[j] = temp[j].replace(":", "")
                                temp[j] = temp[j].replace(":", "")
                                temp[j] = temp[j].replace("\?", "")
                                temp[j] = temp[j].replace(" ", "")
                                temp[j] = temp[j].replace(" ", "")
                                temp[j] = temp[j].replace(",", "")
                                temp[j] = temp[j].replace(":", "")
                                temp[j] = temp[j].replace("\n", "")
                                temp[j] = temp[j].replace("\t", "")
                                temp[j] = temp[j].replace('？', "")
                                temp[j] = temp[j].replace('：', "")
                            newname = ""
                            for l in range(0,len(temp)-1):
                                newname += temp[l]
                            newname += '.pdf'
                            os.rename(i,newname)
                        if os.path.splitext(i)[1] == ".epub":
                            name = i
                            temp = name.split('.')
                            num = len(temp)-1
                            for j in range(0,len(temp)):
                                temp[j] = temp[j].replace('？', "")
                                temp[j] = temp[j].replace('：', "")
                                temp[j] = temp[j].replace("]", "")
                                temp[j] = temp[j].replace("[", "")
                                temp[j] = temp[j].replace("，", "")
                                temp[j] = temp[j].replace("：", "")
                                temp[j] = temp[j].replace("。", "")
                                temp[j] = temp[j].replace("、", "")
                                temp[j] = temp[j].replace("【", "")
                                temp[j] = temp[j].replace("】", "")
                                temp[j] = temp[j].replace("(", "")
                                temp[j] = temp[j].replace(")", "")
                                temp[j] = temp[j].replace(":", "")
                                temp[j] = temp[j].replace(":", "")
                                temp[j] = temp[j].replace("\?", "")
                                temp[j] = temp[j].replace(" ", "")
                                temp[j] = temp[j].replace(" ", "")
                                temp[j] = temp[j].replace(",", "")
                                temp[j] = temp[j].replace("\n", "")
                                temp[j] = temp[j].replace(":", "")
                                temp[j] = temp[j].replace("\t", "")
                            newname = ""
                            for l in range(0,len(temp)-1):
                                newname += temp[l]
                            newname = newname.partition("by")[0]
                            newname += '.epub'
                            os.rename(i,newname)
                        if os.path.splitext(i)[1] == ".mobi":
                            name = i
                            temp = name.split('.')
                            num = len(temp)-1
                            for j in range(0,len(temp)):
                                temp[j] = temp[j].replace('？', "")
                                temp[j] = temp[j].replace('：', "")
                                temp[j] = temp[j].replace("]", "")
                                temp[j] = temp[j].replace("[", "")
                                temp[j] = temp[j].replace("，", "")
                                temp[j] = temp[j].replace("：", "")
                                temp[j] = temp[j].replace("。", "")
                                temp[j] = temp[j].replace("、", "")
                                temp[j] = temp[j].replace("【", "")
                                temp[j] = temp[j].replace("】", "")
                                temp[j] = temp[j].replace("(", "")
                                temp[j] = temp[j].replace(")", "")
                                temp[j] = temp[j].replace(":", "")
                                temp[j] = temp[j].replace(":", "")
                                temp[j] = temp[j].replace("\?", "")
                                temp[j] = temp[j].replace(" ", "")
                                temp[j] = temp[j].replace(" ", "")
                                temp[j] = temp[j].replace(",", "")
                                temp[j] = temp[j].replace("\n", "")
                                temp[j] = temp[j].replace(":", "")
                                temp[j] = temp[j].replace("\t", "")
                            newname = ""
                            for l in range(0,len(temp)-1):
                                newname += temp[l]
                            newname = newname.partition("by")[0]
                            newname += '.mobi'
                            os.rename(i,newname)
                if os.path.isdir(i):
                    os.chdir(str(i))
                    path2 = os.listdir(os.getcwd())
                    father_path2 = os.getcwd()
                    for i in path2:
                        if os.path.isfile(i):
                            if os.path.splitext(i)[1] == ".pdf":
                                name = i
                                temp = name.split('.')
                                num = len(temp)-1
                                for j in range(0,len(temp)):
                                    temp[j] = temp[j].replace("]", "")
                                    temp[j] = temp[j].replace("[", "")
                                    temp[j] = temp[j].replace("(", "")
                                    temp[j] = temp[j].replace(")", "")
                                    temp[j] = temp[j].replace(":", "")
                                    temp[j] = temp[j].replace("?", "")
                                    temp[j] = temp[j].replace(" ", "")
                                    temp[j] = temp[j].replace("\n", "")
                                    temp[j] = temp[j].replace("\t", "")
                                    temp[j] = temp[j].replace('？', "")
                                    temp[j] = temp[j].replace('：', "")
                                newname = ""
                                for l in range(0,len(temp)-1):
                                    newname += temp[l]
                                newname += '.pdf'
                                os.rename(i,newname)
                            if os.path.splitext(i)[1] == ".epub":
                                name = i
                                temp = name.split('.')
                                num = len(temp)-1
                                for j in range(0,len(temp)):
                                    temp[j] = temp[j].replace('？', "")
                                    temp[j] = temp[j].replace('：', "")
                                    temp[j] = temp[j].replace("]", "")
                                    temp[j] = temp[j].replace("[", "")
                                    temp[j] = temp[j].replace("，", "")
                                    temp[j] = temp[j].replace("：", "")
                                    temp[j] = temp[j].replace("。", "")
                                    temp[j] = temp[j].replace("、", "")
                                    temp[j] = temp[j].replace("【", "")
                                    temp[j] = temp[j].replace("】", "")
                                    temp[j] = temp[j].replace("(", "")
                                    temp[j] = temp[j].replace(")", "")
                                    temp[j] = temp[j].replace(":", "")
                                    temp[j] = temp[j].replace(":", "")
                                    temp[j] = temp[j].replace("\?", "")
                                    temp[j] = temp[j].replace(" ", "")
                                    temp[j] = temp[j].replace(" ", "")
                                    temp[j] = temp[j].replace(",", "")
                                    temp[j] = temp[j].replace("\n", "")
                                    temp[j] = temp[j].replace(":", "")
                                    temp[j] = temp[j].replace("\t", "")
                                newname = ""
                                for l in range(0,len(temp)-1):
                                    newname += temp[l]
                                newname = newname.partition("by")[0]
                                newname += '.epub'
                                os.rename(i,newname)
                            if os.path.splitext(i)[1] == ".mobi":
                                name = i
                                temp = name.split('.')
                                num = len(temp)-1
                                for j in range(0,len(temp)):
                                    temp[j] = temp[j].replace('？', "")
                                    temp[j] = temp[j].replace('：', "")
                                    temp[j] = temp[j].replace("]", "")
                                    temp[j] = temp[j].replace("[", "")
                                    temp[j] = temp[j].replace("，", "")
                                    temp[j] = temp[j].replace("：", "")
                                    temp[j] = temp[j].replace("。", "")
                                    temp[j] = temp[j].replace("、", "")
                                    temp[j] = temp[j].replace("【", "")
                                    temp[j] = temp[j].replace("】", "")
                                    temp[j] = temp[j].replace("(", "")
                                    temp[j] = temp[j].replace(")", "")
                                    temp[j] = temp[j].replace(":", "")
                                    temp[j] = temp[j].replace(":", "")
                                    temp[j] = temp[j].replace("\?", "")
                                    temp[j] = temp[j].replace(" ", "")
                                    temp[j] = temp[j].replace(" ", "")
                                    temp[j] = temp[j].replace(",", "")
                                    temp[j] = temp[j].replace("\n", "")
                                    temp[j] = temp[j].replace(":", "")
                                    temp[j] = temp[j].replace("\t", "")
                                newname = ""
                                for l in range(0,len(temp)-1):
                                    newname += temp[l]
                                newname = newname.partition("by")[0]
                                newname += '.mobi'
                                os.rename(i,newname)
                    os.chdir(father_path1)
            os.chdir(father_path)






if __name__ == "__main__":
    changename()
