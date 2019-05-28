

class Brocker:
    def __init__(self):
        self.senders_list=[]
        self.recivers_list=[]
        self.senders_message=[]
        

    def add_message(self,message):
        self.senders_list.append(message.senderName)
        self.senders_message.append(message)

    def add_senders(self,sender):
        self.senders_list.append(sender)
    
    def add_reciver(self,reciver):
        self.recivers_list.append(reciver)
    
    def check_new_message(self,reciver):
        self.recivers_list.append(reciver)
        for  message  in self.senders_message:
            if(message.senderName==reciver.subscribe_to):
                reciver.recivedMessages.append(message)
    
    def check_new_message_using_name(self,subscribe_to):
        rec=[]
        for  message  in self.senders_message:
            if(message.senderName==subscribe_to):
                rec.append(message)
        return rec
