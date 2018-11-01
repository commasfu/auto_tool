#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:commas
# datetime:2018/10/31 11:31

import os
import time

from conf.settings import *

print(time.strftime('%Y-%m-%d %H:%M:%S'))


print(RPROJECT_ROOT_PATH)

print(os.path.dirname(__file__))