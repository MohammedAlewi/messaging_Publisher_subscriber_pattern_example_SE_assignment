from datetime import datetime


class Message:
    def __init__(self,senderName,messageBody):
        self.senderName=senderName
        self.messageBody=messageBody
        self.datePublished=datetime.now()

    def insertMessgeBody(self,messageBody):
        self.messageBody=messageBody

    def insertSender(self,sender):
        self.senderName=sender

    def getDate(self):
        return self.datePublished