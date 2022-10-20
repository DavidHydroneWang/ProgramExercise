#!/usr/bin/env python
# coding=utf-8
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        stack = []
        while tokens:
            temp = tokens.pop(0)
            if temp not in ['+', '-', '*', '/']:
                stack.append(temp)
            else:
                if temp == '+':
                    i = int(stack.pop())
                    j = int(stack.pop())
                    stack.append(i + j)
                elif temp == '-':
                    i = int(stack.pop())
                    j = int(stack.pop())
                    stack.append(j - i)
                elif temp == '*':
                    i = int(stack.pop())
                    j = int(stack.pop())
                    stack.append(i * j)
                else:
                    i = int(stack.pop())
                    j = int(stack.pop())
                    stack.append( int(j / i))

        return stack[0]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operator = ['+', '-', '/', '*']
        while tokens:
            value = tokens.pop(0)
            if value not in operator:
                stack.append(value)
            else:
                a = stack.pop()
                b = stack.pop()
                c = str(int(eval( b + value + a)))
                #print(c)
                tokens.insert(0, c)
                if not stack and len(tokens) == 1:
                    break

        return int(tokens[0])


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                stack.append(int(1/stack.pop()*stack.pop()))
            else:
                stack.append(int(token))
        return stack.pop()


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                stack.append(item)
            else:
                first_num, second_num = stack.pop(), stack.pop()
                stack.append(
                    int(eval(f'{second_num} {item} {first_num}'))   # 第一个出来的在运算符后面
                )
        return int(stack.pop()) # 如果一开始只有一个数，那么会是字符串形式的
