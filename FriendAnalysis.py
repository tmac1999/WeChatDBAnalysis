#!/usr/bin/python
# -*- coding:utf8 -*- 为了支持中文注释
import hashlib
import sqlite3

from Friend import Friend


class FriendAnalysis(object):
    # 返回MD5-UerName键值对
    def openDB(self,DBLocation):
        connect = sqlite3.connect(DBLocation)
        cursor = connect.cursor()
        execute = cursor.execute('select userName,dbContactRemark from Friend')
        nameDict = {}
        for row in execute:
            md5 = hashlib.md5(row[0]).hexdigest()
            friend = Friend(row[0], row[1])
            print md5,':',row[0]
            nameDict[md5] = friend
            # print row[0]

        # get = nameDict.get(u'0362ee74f7b2265ac2a36e5135804233')
        # print get.contactRemark, get.userName
        return nameDict
