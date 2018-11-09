#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:commas
    datetime:2018/11/9 10:39
"""

import socket

obj = socket.socket()

obj.connect(('127.0.0.1', 8001))
# data = obj.recv(1024)
# print(str(data, encoding='utf-8'))

while True:
    inp = input('>>>')
    if inp == 'exit':
        obj.send(bytes('bye', encoding='utf-8'))
        break
    else:
        obj.send(bytes(inp, encoding='utf-8'))
        data = obj.recv(1024)
        print(str(data, encoding='utf-8'))
        #inp = input('>>>')
obj.close()



