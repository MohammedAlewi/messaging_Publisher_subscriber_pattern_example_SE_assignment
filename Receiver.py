from  Message import *
from Brocker import *


class Reciver:
    def __init__(self,reciver_name):
        self.reciver_name=reciver_name
        self.subscribe_to=None
        self.recivedMessages=[]
        self.brocker=Brocker()

    def setSubscribedTo(self,senderName):
        self.subscribe_to=senderName

    def getRecievedMessages(self):
        return self.recivedMessages

    def checkNewMessage(self):
        self.brocker.check_new_message(self)
