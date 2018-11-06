#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:commas
    datetime:2018/11/6 16:36
"""

import time
from lib.utils import exce_function

@exce_function
def s_test():
    time.sleep(1)
    print('test....')

s_test()


