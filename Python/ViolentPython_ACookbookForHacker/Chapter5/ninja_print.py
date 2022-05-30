#!/usr/bin/env python
# coding=utf-8
import obexftp

try:
    btPrinter = obexftp.clien(obexftp.BLUETOOTH)
    btPrinter.connect('00:16:38:DE:AD:11', 2)
    btPrinter.put_file('/tmp/ninja.jpg')
    print('[+] Printed Ninja Image')
except:
    print('[-] Failed to print Ninja Image.')
