#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:commas
    datetime:2018/11/9 10:39
"""

import socket
address = ('127.0.0.1', 8001)
sok = socket.socket()
sok.bind(address)
sok.listen(3)
print('wating.....')
while True:
    conn, addr = sok.accept()
    print(type(addr))
    conn.send(bytes(str(addr), encoding='utf-8'))
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        data = str(data, encoding='utf-8')
        if data == 'bye':
            print('waiting......next people.....')
            break
        print(data)
        inp = input(">>>")
        conn.send(bytes(inp, encoding='utf-8'))
    conn.close()
