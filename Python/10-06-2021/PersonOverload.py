#!/usr/bin/env python
# coding=utf-8


class Person():
    def say_hi(self, name=None):
        self.name = name
        if name == None: print('您好！ ')
        else: print('您好！　我叫',self.name)


p21 = Person()
p21.say_hi()
p21.say_hi('威尔逊')
