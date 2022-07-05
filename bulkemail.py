import smtplib
#https://docs.python.org/3/library/ssl.html
import ssl


class User:
    def __init__(self, name, email, service):
        self.name = name
        self.email = email
        self.service = service




reciverlist_adv=[]
reciverlist_not = []


reciverlist_not.append(User("FATEMA", "FFF@GMAIL.COM", 1))
reciverlist_adv.append(User("FATEMA", "FFF@GMAIL.COM", 1))
def addReciver():
    name = input("enter the name: ")
    email = input("enter the email: ")
    service = int(input("enter 1 for advertisment 2 to get notification and 3 for both options: "))
    newUser = User(name, email, service)
    if newUser.service==1:
        reciverlist_adv.append(newUser)
        print("you have been added successfully")
    elif newUser.service==2:
        reciverlist_not.append(newUser)
        print("you have been added successfully")
    elif newUser.service==3:
        reciverlist_not.append(newUser)
        reciverlist_adv.append(newUser)
        print("you have been added successfully")

    else:
        errormsg()

def deleteReciver():
    email = input("enter your email to unsubscribe: ")
    for obj in reciverlist_adv:
        if obj.email == email:
            reciverlist_adv.remove(obj)
    for obj in reciverlist_not:
        if obj.email == email:
            reciverlist_not.remove(obj)

def errormsg():
    print("error")


def sendbulkemail(msg_file, reciver_list):
    server = "smtp.gmail.com"
    port = 587
    # iblnkighblcnvikx
    sender_email = "julnara266@gmail.com"
    password = "qavtncickchjhhlu"

    addresses = ["julnar01@icloud.com"]
    # open('uu.txt', 'r').readlines()

    context = ssl.create_default_context()
    with smtplib.SMTP(server, port) as mailer:
        # Setting debug level in order to get detailed information for debuging
        mailer.set_debuglevel(1)
        mailer.ehlo()
        mailer.starttls(context=context)
        # Authentication
        mailer.login(sender_email, password)

        # Sending the email
        for obj in reciver_list:
            # toaddr = address
            receiver_email = obj.email  # "receiver@yahoo.com"

            subject = "Subject: coventry automatic emails\n"

            message_body = open(msg_file, "r").read()  # "\nTest email from Python."

            message = subject + "\n" + message_body + "\n"

            mailer.sendmail(sender_email, receiver_email, message)



role = int(input("enter 1 if you are user or 2 for agent: "))
print("u chose " + str(role))

if role==1:
    choice= int(input("enter 1 for subscription or 2 to unsubscribe: "))
    if choice==1:
        addReciver()

    elif choice==2:
        deleteReciver()
        print("you have unsubscribed")

    else:
        print("your choice is incorrect")


elif role== 2:
    choice=int(input("enter 1 to register as a user or 2 to delete user or 3 to send bulk email: "))
    if choice==1:
        addReciver()

    elif choice==2:
        deleteReciver()
        print("you have unsubscribed")

    elif choice==3:
        type = int(input("enter 1 for adv or 2 for sending not: "))

        if type==1:
            file = "adv.txt"
            sendbulkemail(file, reciverlist_adv)
        elif type==2:
            file = "not.txt"
            sendbulkemail(file, reciverlist_not)
        else:
            errormsg()

    else:
        errormsg()


else:
    print("your choice is not correct")
