#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:commas
    datetime:2018/10/31 15:01
"""
import os


PATH_ROOT = '/data'
ROOT_LOG = os.path.join(PATH_ROOT, 'logs', 'auto_tool.log')
DEBUG = False

RPROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

# socket
MANAGEMENT_HOST = ('192.168.200.89', 5522)
SOCKET_DEFAULT_TIMEOUT = 10
SSL_KEYS = dict(
                keyfile=os.path.join(RPROJECT_ROOT_PATH,'conf','keys', "client-key.pem"),
                certfile=os.path.join(RPROJECT_ROOT_PATH,'conf','keys', "client-cert.pem"),
                ca_certs=os.path.join(RPROJECT_ROOT_PATH,'conf','keys', "ca-cert.pem")
                )