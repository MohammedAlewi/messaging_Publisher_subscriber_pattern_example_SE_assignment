from  Message import *
from Brocker import *

class Sender:
    def __init__(self,sender_name):
        self.sender_name=sender_name
        self.messagesSent=[]
        self.queneingMessages=[]
        self.currentMessage=None
        self.brocker=Brocker()

    def writeMessage(self,message_body):
        message=Message(self.sender_name,message_body)
        self.currentMessage=message
        self.queneingMessages.append(message)

    def publish_message(self):
        self.brocker.add_message(self.queneingMessages.pop())
        self.brocker.add_message(self.currentMessage)
        self.messagesSent.append(self.currentMessage)

    def clearMessage(self):
        self.queneingMessages.clear()
        self.messagesSent.clear()