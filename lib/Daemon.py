#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:xcl commas
    datetime:2018/10/31 13:55
"""

import os
import sys
import time
import atexit
import logging
import subprocess
from signal import SIGTERM

from lib.file_io import write_file, read_file
from lib.sender import TaskSender

from lib.logs import init_log_handler
init_log_handler(__name__)
log = logging.getLogger(__name__)


class Daemon(object):
    def __init__(self, func=None, args=None, service=None, stderr='/dev/null', stdout='/dev/null', stdin='/dev/null'):
        self.func = func
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.args = args
        self.service = service

    def _daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            log.error("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)
        os.setsid()
        os.chdir("/")
        os.umask(0)
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            log.error("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(self.stdin, 'r')
        so = open(self.stdout, 'a+')
        se = open(self.stderr, 'a+')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())
        # pid = str(os.getpid())
        # write_file(self.pidfile, "%s\n" % pid, 'w+')


    def delpid(self):
        if os.path.exists(self.pidfile):
            os.remove(self.pidfile)

    def start(self):
        """
        Start the daemon
        """
        self._daemonize()
        log.debug(os.getpid())
        try:
            self.func(self.args)
        except:
            log.exception('Script meets exception:')
            if self.args.taskid:
                t = TaskSender(self.args.taskid, self.args.consoleip, self.args.consoleport)
                res = t.sync_status(code=99999, msg='Script Error!')
                t.close()
                if res:
                    log.info(res)
                else:
                    log.error('Failed to sync status with console server!')


    def stop(self):
        self._kill_pid()

    def restart(self):
        self.stop()
        time.sleep(2)
        self.start()

    def _kill_pid(self):
        """
        kill the pids in the pidfile and remove the pidfile
        :param pidfile:
        :return:
        """
        if not os.path.isfile(self.pidfile):
            message = "pidfile %s does not exist. Daemon not running?\n"
            sys.stderr.write(message % self.pidfile)
            return
        # Try killing the daemon process
        pids = read_file(self.pidfile, 'r')
        for pid in pids:
            try:
                pid = pid.strip()
                log.info('Process will be killed: %s' % pid)
                pid_info = subprocess.getoutput("ps -p %s -f" % pid).split('\n')
                if len(pid_info) < 2:
                    log.warn('Failed to get process info ! Does it exists?')
                    continue
                # log the process detail in the log for trouble shooting
                log.info(pid_info[1])
                if self.service in pid_info[1]:
                    os.kill(int(pid.strip()), SIGTERM)
                else:
                    log.warn('Not %s process, skip!' % self.service)
            except OSError as err:
                log.error(err)
        self.delpid()
        return True


def main(*args):
    log.debug('test')
    write_file('/tmp/test', 'test')
    return

if __name__ == "__main__":
    Daemon(main).start()
