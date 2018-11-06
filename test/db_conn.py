#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:commas
    datetime:2018/10/31 21:19
"""

import logging

log = logging.getLogger(__name__)

try:
    import mysql.connector
except ImportError:
    log.error("Exceptions.ImportError: No module named mysql.connector")
DBCONFIG = dict()


class MysqlConn(object):
    """
        class of mysql connector
        all the sqls executed will be logged in debug mode

    """

    def __init__(self, conf=None, is_dict=True):
        """
            conf: dict of configuration
            DBCONFIG = {
                'host': '127.0.0.1',
                'port': 3306,
                'user': 'mega',
                'password': 'mega',
                'database': 'mega',
                'charset': 'utf8',
            }
        """
        self.db = DBCONFIG if not conf else conf
        self.is_dict = is_dict
        self.conn = None
        self.connect(self.db)

    def __del__(self):
        '''
            Close the connection when the object is going to erase
        '''
        self.close()

    def connect(self, conf={}):
        try:
            conn = mysql.connector.connect(**conf)
            if conn:
                self.conn = conn
            else:
                self.conn = None
            return conn
        except Exception as ex:
            msg = "Connect to {0} failed as :{1}".format(conf.get('host'), ex)
            print(msg)
            log.error(msg)
            return False

    def cursor(self):
        '''
            The connection should be close if use the cursor out of this class
        '''
        if self.conn:
            return self.conn.cursor(dictionary=self.is_dict)
        else:
            return False

    def select(self, sql, size=0):
        '''
            Used for general queries that required
            Return list of dictionary of all the data as default
            Size:
                0 : all the matched rows [{'k': 'v'}, {'k': 'v'}]
                1 : the first row default
                n : return n rows
                -1 : single value queried by sql ,return the value directly;
                    if none is returned by mysql server,return -1.
        '''
        log.debug(sql)
        if size == -1:
            self.is_dict = False
        cursor = self.cursor()
        if not cursor:
            if size != -1:
                return []
            else:
                return 0
        cursor.execute(sql)
        if size == 0:
            data = cursor.fetchall()
        elif size == 1:
            data = cursor.fetchone()
        elif size == -1:
            data = cursor.fetchone()
            data = data[0] if data else None
        else:
            data = cursor.fetchmany(size)
        if self.conn.unread_result:
            result = self.conn.get_rows()
        return data
    def execute(self, sql):
        """
            Run sql directly
        """
        log.debug(sql)
        cursor = self.cursor()
        if cursor:
            try:
                cursor.execute(sql)
                self.conn.commit()
                return True
            except Exception as ex:
                log.error('Excute sql gets error:{}'.format(ex))
                log.error(sql)
        return False
    def close(self):
        '''
            Close the connection
        '''
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    conn = MysqlConn(dict(host='127.0.0.1', port=3306, user='root', password='123456', database='commas'))
    print(conn.select('select version();'))
    print(conn.select('select * from auth_user;', size=0))




