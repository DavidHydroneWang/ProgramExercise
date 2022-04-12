#!/usr/bin/env python
# coding=utf-8
import sys
import re


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


class Handler:
    """
    对Parser发起的方法调用进行处理的对象

    Parser将对每个文本块调用方法start()和end(),并将合适
    的文本块名称作为参数。方法sub()将用于正则表达式替换,
    使用诸如'emphasis'等名称调用时,这个方法将返回相应的
    替换函数
    """

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
            return result

        return substitution


class HTMLRenderer(Handler):
    """
    用于渲染HTML的具体处理程序
    HTMLRenderer的方法可通过超类Handler的方法
    start()、end()和sub()来访问。这些方法实现了
    HTML文档使用的基本标记
    """

    def start_document(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul>')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))

    def sub_url(self, match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))

    def sub_email(self, match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1),
                                                   match.group(1))

    def feed(self, data):
        print(data)


class Rule:
    """
    所有规则的基类
    """

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """
    标题只包含一行,不超过70个字符且不以冒号结尾
    """
    type = 'heading'

    def condition(self, block):
        return '\n' not in block and len(block) < 70 and not block[-1] == ':'


class TitleRule(HeadingRule):
    """
    题目是文档中的第一个文本块,前提条件是它属于标题
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    """
    列表项是以连字符打头的段落。在设置格式的过程中,将把连字符删除
    """
    type = 'listitem'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    """
    列表以紧跟在非列表项文本块后面的列表项打头,以相连的最后一个列表项结束
    """
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    """
    段落是不符合其他规则的文本块
    """
    type = 'paragraph'

    def condition(self, block):
        return True


class Parser:
    """
    Parser读取文本文件,应用规则并控制处理程序
    """

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
#            print(block)
            for filter in self.filters:
                block = filter(block, self.handler)
#                print(block)
                for rule in self.rules:
                    if rule.condition(block):
                        last = rule.action(block, self.handler)
                        if last:
                            break
                if last:    # missed in source code
                    break   # missed in source code
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    在构造函数中添加规则和过滤器的Parser子类
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
