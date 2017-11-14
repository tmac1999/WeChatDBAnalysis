#!/usr/bin/python
# -*- coding:utf8 -*- 为了支持中文注释
import sys
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')
from Friend import Friend
from FriendAnalysis import FriendAnalysis

if __name__ == '__main__':
    # friend_analysis = FriendAnalysis()
    # dbLocation = '/Users/lianhua/Downloads/WCDB_Contact.sqlite'
    # nameDict = friend_analysis.openDB(dbLocation)
    # friend = Friend('asd', 'asddasda')
    # d = {}
    # d['aaa'] = friend
    # get = d.get('aaa')
    # print get.contactRemark, get.userName
    # s = '\xe9\x9d\x92\xe8\x9b\x99\xe7\x8e\x8b\xe5\xad\x90'
    # ss = s.encode('raw_unicode_escape')
    # print(ss)  # 结果：b'\xe9\x9d\x92\xe8\x9b\x99\xe7\x8e\x8b\xe5\xad\x90'
    # sss = ss.decode('unicode_escape')
    # print(sss)
    print np.random.randint(1, 100, 5)
    # print np.random.rand(5)
    # a = np.array(1, 2, 3, 4)  # 错误
    a1 = np.array([1, 2, 3, 4])  # 正确
    print type(a1)
