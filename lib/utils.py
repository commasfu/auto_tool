#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:xcl commas
    datetime:2018/10/31 13:55
"""
import re, os
import shlex
import time
import logging
import subprocess
import configparser

log = logging.getLogger(__name__)


def ping(ip):
    res = True
    cmd = "ping -c 1 %s" % ip
    args = shlex.split(cmd)
    for i in range(30):
        try:
            log.info(cmd)
            subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            res = True
            break
        except subprocess.CalledProcessError:
            log.error("Check ip failed: %s" % cmd)
            res = False
    return res


def get_ip_all():
    """

    :return:
    """
    iplist = []
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
    output = ipconfig_process.stdout.read()
    ip_pattern = re.compile('(inet %s)' % ipstr)
    pattern = re.compile(ipstr)
    for ipaddr in re.finditer(ip_pattern, str(output)):
        ip = pattern.search(ipaddr.group())
        if ip.group() != "127.0.0.1":
            iplist.append(ip.group())
    return iplist

def get_config_value(file,session,key):
    if os.path.isfile(file):
        conf = configparser.ConfigParser(allow_no_value=True)
        conf.read(file)
        values = conf.get(session, key)
    else:
        log.error('%s not exist' % file)
        values = False
    return values


def exce_function(f):
    '''
    return second
    :param f:
    :return:
    '''
    def new_f():
        start_time = time.time()
        f()
        end_time = time.time()
        print('%s speed  %s' %(f, round(end_time - start_time, 2)))
    return new_f

def main():
    print(get_ip_all())
    return


if __name__ == "__main__":
    main()