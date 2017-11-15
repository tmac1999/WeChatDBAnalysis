#!/usr/bin/python
# -*- coding:utf8 -*- 为了支持中文注释
import hashlib
import sqlite3
import numpy as np
from FriendAnalysis import FriendAnalysis
from test.basic_pie_chart_test import ShowPieChart
from test.matplotlib_test import ShowChart
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == '__main__':

    connect = sqlite3.connect('/Users/lianhua/Downloads/MM.sqlite')
    # connect = sqlite3.connect('/Users/lianhua/Downloads/MM(1).sqlite')
    tableNameBeKicked = 'Chat_221bd83233e2e7e73bb366ef7b7a7d2a'
    # tableNameBeKicked = 'Chat_7fda574311c228948e1786bf1aa6a349'
    tableNameBeKicked = 'Chat_41307402b68753a7d2aec07c61ccee1f'  ##
    print "Opened database successfully"
    c = connect.cursor()

    cursorDes = c.execute("SELECT Des  from " + tableNameBeKicked)
    totalMsgCount = 0
    s = set([1, 2, 3])
    # d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    d = {}
    noColonRowCount = 0
    myselfMsgCount = 0
    myselfMsgCount = 0
    systemMsgCount = 0
    for rowDes in cursorDes:
        if rowDes[0] == 0:
            myselfMsgCount += 1

    cursorType = c.execute("SELECT Type  from " + tableNameBeKicked)
    for rowType in cursorType:
        if rowType[0] == 10000:
            systemMsgCount += 1

    d['myself'] = myselfMsgCount
    d['10000'] = systemMsgCount
    cursor = c.execute("SELECT Message  from " + tableNameBeKicked)
    for row in cursor:

        if row[0].__contains__(':\n'):

            split = row[0].split(':\n')
            if d.get(split[0]) == None:
                d[split[0]] = 1
                # s.add(split[0])
            else:
                d[split[0]] = d.get(split[0]) + 1
                # if split[0].__contains__(''):
                #     d.pop(split[0])
        else:
            noColonRowCount += 1
        totalMsgCount += 1

    print 'total msg count =', totalMsgCount
    realChatMsgCount = 06
    otherMsgCount = 0
    friend_analysis = FriendAnalysis()
    dbLocation = '/Users/lianhua/Downloads/WCDB_Contact.sqlite'
    nameDict = friend_analysis.openDB(dbLocation)
    # labels = []
    # sizes = []

    people = []
    perf = []  # 横轴数量
    for single in d:
        if single.__len__() < 50:
            hexdigest = hashlib.md5(single).hexdigest()
            friend = nameDict.get(hexdigest)
            if friend != None:
                # print single, ":", d[single], friend.contactRemark, hexdigest
                # labels.append(friend.contactRemark)
                # sizes.append(d[single])
                people.append(str(friend.contactRemark).split()[0])
                perf.append(d[single])
            realChatMsgCount += d[single]
        else:
            otherMsgCount += d[single]

    print 'realChatMsgCount:', realChatMsgCount, 'otherMsgCount:', otherMsgCount, 'theRestMsgCount:', totalMsgCount - realChatMsgCount - otherMsgCount
    # print 'noColonRowCount:', noColonRowCount

    # todo 在Friend表中找到昵称 来对群聊username进行匹配，同时绘制饼状图 or条形图
    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    #
    # sizes = [15, 30, 45, 10]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    # explode = None
    # chart = ShowPieChart()
    # chart.show(explode, labels, sizes)

    show_chart = ShowChart()
    y_pos = np.arange(len(people))
    performance = np.array(perf)
    error = np.random.rand(len(people))
    show_chart.showBarChart(y_pos, performance, error, people)


    def printSet(set):
        for single in set:
            print single
