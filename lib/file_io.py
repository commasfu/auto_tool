#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:xcl commas
    datetime:2018/10/31 13:55
"""


import logging

log = logging.getLogger(__name__)


def read_file(filename, mode='rb', tostr=False):
    """
        return all the file content as a list
            empty string when meet errors
    """
    content = []
    try:
        f = open(filename, mode)
        if tostr:
            content = f.read()
        else:
            content = f.readlines()
    except IOError as ex:
        log.error('Failed to open file : {0}  {1}'.format(filename, ex))
    return content


def write_file(filename, content, mode='wb'):
    """
        write the file content into specified file,the content should be
        a iterable object includes strings.
        return
                True when job finished
                False  when meet errors
    """
    try:
        f = open(filename, mode)
        if isinstance(content, list):
            f.writelines(content)
        else:
            f.write(content.encode())
    except IOError as ex:
        log.error('Failed to open file : {0}  {1}'.format(filename, ex))
        return False, ex
    return True, ''
