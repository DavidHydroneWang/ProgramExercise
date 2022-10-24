#!/usr/bin/env python
# coding=utf-8
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        my_dict = {}
        for word in sentence.split(' '):
            for i in range(len(dictionary)):
                root = dictionary[i]
                length = len(root)
                if word[:length] == root:
                    my_dict[word] = root
                    break
        #print(my_dict)
        res = sentence.split(' ')
        for i in range(len(res)):
            if res[i] in my_dict:
                res[i] = my_dict[res[i]]
        #print(res)
        return ' '.join(res)



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = set(dictionary)
        words = sentence.split()
        for i, word in enumerate(words):
            for j in range(1, len(word) + 1):
                if word[:j] in s:
                    words[i] = word[:j]
                    break
        return ' '.join(words)
