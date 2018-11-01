#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:xcl commas
    datetime:2018/10/31 13:55
"""
import ssl
import json
import time
import socket
import struct
import logging

from conf.settings import SSL_KEYS, SOCKET_DEFAULT_TIMEOUT, MANAGEMENT_HOST

log = logging.getLogger(__name__)


class Sender(object):
    """
    HEADER: 8 bytes
        name         len     defaut comment
        version:     1 bytes  1     b(signed char)
        flags:       2 bytes  0     h(short)
        type   :     1 bytes  -     b
        length :     4 bytes  0     i(int)

    """
    VERSION = b'1'
    FLAG = 0
    TYPE = 180
    FORMAT = '!1sHBI'

    def __init__(self):
        """

        :return:
        """
        self.socket = None
        self.timeout = SOCKET_DEFAULT_TIMEOUT

    def connect(self, host, port, **kwargs):
        """

        :param host:
        :param port:
        :param kwargs:
        :return:
        """
        ssl_socket = None
        log.info("Connect to %s " % [host,port])
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            ssl_socket = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, do_handshake_on_connect=False, **SSL_KEYS)
            ssl_socket.connect((host, port))
            self.socket = ssl_socket
        except:
            log.exception('Connection Error:')
        return ssl_socket

    def send(self, data, retry=3, flags=0):
        """

        :return:
        """
        for t in range(retry):
                try:
                    self.socket.send(self.pack(data=data, flags=flags))
                    res = self.socket.recv()
                    log.debug(res)
                    if res:
                        return self.unpack(res)
                except socket.error as se:
                    time.sleep(1)
                    log.error(se)
        return False

    def pack(self, data=b'', type=180, flags=0):
        """
        :return:
        """
        if not isinstance(data, bytes):
            data = bytes(data, encoding='utf8')
        header = struct.pack(self.FORMAT, self.VERSION, flags, self.TYPE, len(data))
        return header + data

    def unpack(self, data):
        """

        :param data:
        :return:
        """
        header = data[:8]
        data = json.loads(data[8:].decode())
        return data

    def close(self):
        if self.socket:
            self.socket.close()


class TaskSender(Sender):
    """

    """

    def __init__(self, tid, server=None, port=None):
        Sender.__init__(self)
        if server and port:
            self.connect(server, int(port))
        else:
            self.connect(*MANAGEMENT_HOST)
        self.tid = tid

    def sync_status(self, code=0, msg='success', flag=0, data=None, flags=0):
        try:
            data = dict(id=self.tid, code=code, message=msg, data=data, flag=flag)
            res = self.send(json.dumps(data), flags=flags)
        except Exception as ex:
            res = False
            log.error('Failed to sync status with console server: %s' % ex)
        return res

    def success(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return self.sync_status(**kwargs)

def main():
    # s = Sender()
    # s.connect('192.168.200.89', 5522)
    # print(s.send('ping'))
    t = TaskSender(110)
    t.sync_status()

if __name__ == "__main__":
    main()