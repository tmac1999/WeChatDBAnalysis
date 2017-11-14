#!/usr/bin/python
# -*- coding:utf8 -*- 为了支持中文注释
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#此方法是将Python2的默认编码ASCII改为 utf-8。但此方法不是一劳永逸的，可能会使一些代码的行为变得怪异。
class ChatTable(object):
    def __str__(self):
        return self.tableName, self.userName, self.myMsgCount

    def __init__(self, tableName, userName, contactRemark, myMsgCount, totalMsgCount, percentage):
        self.tableName = tableName
        self.userName = userName
        self.contactRemark = contactRemark
        self.myMsgCount = myMsgCount
        self.otherMsgCount = totalMsgCount
        self.percentage = percentage

    def __cmp__(self, other):
        if self.myMsgCount < other.myMsgCount:
            return 1
        elif self.myMsgCount > other.myMsgCount:
            return -1
        else:
            return 0

    def __dict__(self):
        return self.tableName

    def dic(self):
        return self.tableName + ':', self.userName, ':', self.contactRemark, ':', self.myMsgCount, '-', self.otherMsgCount, '-', self.percentage

    def dict(self):
        return self.myMsgCount, ':', self.otherMsgCount, ':', self.percentage, ':',# str(self.contactRemark).split()[0].encode('raw_unicode_escape')
