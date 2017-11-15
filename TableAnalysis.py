#!/usr/bin/python
# -*- coding:utf8 -*- 为了支持中文注释
import sqlite3

import numpy as np

from ChatTable import ChatTable
from FriendAnalysis import FriendAnalysis
from test.matplotlib_test import ShowChart


def prn_obj(obj):
    print '\n'.join(['%s:%s' % item for item in obj.__dict__.items()])


if __name__ == '__main__':
    connect = sqlite3.connect('/Users/lianhua/Downloads/MM.sqlite')
    cursor = connect.cursor()
    cursor.execute("select name from sqlite_master where type='table' order by name;")
    # cursor.execute("select * from sqlite_master where name='tablename' and sql like '%fieldname%'; ")
    # cursor.execute("select count(rownum) from [table]")
    # cursor.fetchall()

    #
    tableList = []
    friend_analysis = FriendAnalysis()
    dbLocation = '/Users/lianhua/Downloads/WCDB_Contact.sqlite'
    nameDict = friend_analysis.openDB(dbLocation)
    for row in cursor:
        # print row[0]
        cursorTemp = connect.cursor()
        # cursorRowCount.execute("select * from sqlite_master where name='"+row[0]+"' and sql like 'Des'; ")
        # cursorRowCount.execute("select count(*) from " + row[0])
        cursorTemp.execute("PRAGMA table_info([" + row[0] + "])")
        fetchall = cursorTemp.fetchall()

        if fetchall[-1].__contains__('Des'):
            cursorMyMsgRowCount = connect.cursor()
            cursorOtherMsgRowCount = connect.cursor()
            cursorMyMsgRowCount.execute("select count(*) from " + row[0] + " where Des = 0")
            cursorOtherMsgRowCount.execute("select count(*) from " + row[0])
            msg_row_count_next_ = cursorMyMsgRowCount.next()[0]
            next_ = cursorOtherMsgRowCount.next()[0]
            # cursorRowCount.next() 返回第一行数据，tuple类型，第0号位置即Des=0的行数（自己说话的行数）

            # 分隔后第一位即Username
            row__split = row[0].split('_')

            friend = nameDict.get(row__split[1])
            # print friend.userName
            if friend != None:
                table = ChatTable(row[0], friend.userName, friend.contactRemark, msg_row_count_next_, next_,
                                  msg_row_count_next_ / float(next_))
                tableList.append(table)

                # print row[0],':',friend.contactRemark, ":", msg_row_count_next_, '-', next_, '-', msg_row_count_next_ / float(
                #
                # next_)  # 分母应该还要减去Type=10000 的msg，因为这类msg都Des=1

    l = sorted(tableList)
    # 当输出list时，里面的元素按%r(调__repr__())处理，当输出str时，按%s(调__str__())处理。所以https://segmentfault.com/q/1010000004706142
    people = []
    perf = []
    for object in l:
        print object.dict(), str(object.contactRemark).split()[0]
        if len(people) > 16:
            continue
        people.append(str(object.contactRemark).split()[0])
        perf.append(object.myMsgCount)
    # people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = np.array(perf)
    # performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    chart = ShowChart()
    chart.showBarChart(y_pos, performance, error, people)
