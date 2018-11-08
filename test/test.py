#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:commas
# datetime:2018/10/31 11:31

import os
import time
import sys
pro_path = os.path.dirname(sys.path[0])
sys.path.append(pro_path)

# pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(pro_path)
from conf.settings import *
print(time.strftime('%Y-%m-%d %H:%M:%S'))

print(RPROJECT_ROOT_PATH)
print(pro_path)


'''
class foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = foo('commas',18)
print(getattr(obj,'age'))
'''