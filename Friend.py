class Friend(object):
    def __init__(self,userName,contactRemark):
        self.userName = userName
        self.contactRemark = contactRemark
    def getUserName(self):
        return self.userName
    def getContactRemark(self):
        return self.contactRemark