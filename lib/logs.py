#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:xcl commas
    datetime:2018/10/31 13:55
"""
import sys
import logging
import logging.handlers


from conf.settings import ROOT_LOG, DEBUG



class Logger(object):
    """
        Public log hander for logging
    """
    def __init__(self, model, logfile=None, DEBUG=True):
        """

        :param model:
        :param logfile:
        :param DEBUG:
        :return:
        """
        self.debug = DEBUG
        self.level = 0 if DEBUG else 3
        self.model = model
        self.logfile = logfile if logfile else ROOT_LOG

    def config(self, size=5*10**8, counts=5):
        """
            Init the logger and return the logger object
        """
        levels = {0: logging.DEBUG,
                  3: logging.INFO,
                  2: logging.WARNING,
                  1: logging.ERROR}
        level = levels.get(self.level, logging.NOTSET)
        logger = logging.getLogger(self.model)
        logger.setLevel(level)
        fh = logging.handlers.RotatingFileHandler(self.logfile, maxBytes=size, backupCount=counts)
        formater = logging.Formatter('%(asctime)s %(name)-18s %(levelname)-5s %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formater)
        logger.addHandler(fh)
        if self.debug:
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(level)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
            ch.setFormatter(formatter)
            logger.addHandler(ch)

    def getlogger(self):
        """
        :return:
        """
        self.config()
        return logging.getLogger(self.model)


def init_log_handler(model, logfile=None):
    """

    :return:
    """
    models = ['lib']
    models.append(model)
    for model in models:
        l = Logger(model, logfile, DEBUG)
        l.config()

if __name__ == "__main__":
    log = logging.getLogger('test.aa')
    log.error("error")
    log = logging.getLogger(__name__)
    log.error('123')