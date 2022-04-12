#!/usr/bin/env python
# coding=utf-8
import sys
#s1 = r'\'hello, world!\''
#s2 = r'\n\\hello, world!\\\n'
#print(s1, s2, end='')
#str1 = 'hello, world!'
#print(str1.center(50, '*'))
#print(str1.rjust(50, ' '))
#list1 = [1, 3, 5, 7, 100]
#print(list1)
#list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
#list2 = sorted(list1)
## sorted函数返回列表排序后的拷贝不会修改传入的列表
## 函数的设计就应该像sorted函数一样尽可能不产生副作用
#list3 = sorted(list1, reverse=True)
## 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
#list4 = sorted(list1, key=len)
#print(list1)
#print(list2)
#print(list3)
#print(list4)
#list1.sort(reverse=True)
#print(list1)
#f = [x for x in range(1, 10)]
#print(f)
#f = [x + y for x in 'ABCDE' for y in '1234567']
#print(f)
#f = [x ** 2 for x in range(1, 1000)]
#print(sys.getsizeof(f))  # 查看对象占用内存的字节数
#print(f)
#f = (x ** 2 for x in range(1, 1000))
#print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
#print(f)
#for val in f:
#    print(val)
#def fib(n):
#    a, b = 0, 1
#    for _ in range(n):
#        a, b = b, a + b
#        yield a
#
#
#def main():
#    for val in fib(20):
#        print(val)
#
#
#if __name__ == '__main__':
#    main()
#fruits_list = ['apple', 'banana', 'orange']
#fruits_tuple = tuple(fruits_list)
#print(fruits_tuple)
#set1 = {1, 2, 3, 3, 3, 2}
##print(set1)
##print('Length =', len(set1))
#set2 = set(range(1, 10))
#set3 = set((1, 2, 3, 3, 2, 1))
##print(set2, set3)
#set1.add(4)
#set1.add(5)
#set2.update([11, 12])
#set2.discard(5)
#if 4 in set2:
#    set2.remove(4)
#print(set1, set2)
#print(set3.pop())
#print(set3)
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
items1 = dict(one=1, two=2, three=3, four=4)
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
print(scores['骆昊'])
print(scores['狄仁杰'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
