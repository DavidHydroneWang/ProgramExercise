#!/usr/bin/env python
# coding=utf-8
from xml.sax.handler import ContentHandler
from xml.sax import parse


class PageMaker(ContentHandler):
    passthroug = False

    def startElement(self, name, attrs):
        if name == 'page':
            self.passthroug = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write('<title>{}</title>\n'.format(attrs['title']))
            self.out.write('</head><body>\n')
        elif self.passthroug:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key, val))
            self.out.write('>')

    def endElement(self, name):
        if name == 'page':
            self.passthroug = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passthroug:
            self.out.write('</{}>'.format(name))

    def characters(self, chars):
        if self.passthroug:
            self.out.write(chars)


parse('website.xml', PageMaker())
