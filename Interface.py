from  Message import *
from  Receiver import *
from Brocker import *
from datetime import datetime
from  Sender import *
def main():
    print(" \tWelcome")
    print("Messaging App")
    ans=input("1. for sending Message\n2. for recieving message\n :")
    sender=Sender(ans)
    reciver=Reciver(ans)
    brock=Brocker()
    while(ans!="quit"):
        if(ans=="1"):
            ans=input("Enter Your Name\n :")
            sender.sender_name=ans
            sender.brocker=brock
            brock.add_senders(sender)
            ans=input("Enter 1 to send or 2 to quit  Message\n :")
            while(ans!="2"):
                if(ans=="1"):
                    msg=input("Enter Your Message :")
                    sender.writeMessage(msg)
                    sender.publish_message()
                ans=input("Enter 1 to send or 2 to quit  Message\n :")

        if(ans=="2"):
            print("receiver")
            ans=input("Enter Your Name\n :")
            reciver.reciver_name=ans
            reciver.brocker=brock
            brock.add_reciver(reciver)
            ans=input("Enter 1 to recive or quit to quit  Message\n :")

            while(ans!="2"):
                snd=input("Enter Sender Name\n :")
                reciver.setSubscribedTo(snd)
                if(ans=="1"):
                    reciver.checkNewMessage()
                    #brock.check_new_message(reciver)
                    print("-----messages-----------")
                    while(len(reciver.recivedMessages)):
                        message=reciver.recivedMessages.pop()
                        print("--------------------------------")
                        print(" Sender Name:",message.senderName)
                        print(" Messge:",message.messageBody)
                        print(" Date :",message.datePublished)

                    print("--------------------------------")
                    ans=input("Enter 1 to recieve or 2 to quit  Message\n :")
        
    

main()