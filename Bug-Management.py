import mysql.connector as mysql
import modules as easy
import os
import time

# Connect to MySQL
db = mysql.connect(host="localhost", user="root", passwd="nishidh@123", database="bug_tracking")
cur = db.cursor()  #creating cursor


def credentials():  #taking credentials
    global email
    global password
    email, password = str(input('Enter the email address : ')), str(input("Enter your password"))

def bugreport():  #edit code status
    actualsts = {1:'Intest', 2:'Open', 3:'Close', 4:'Reopen', 5:'Inprogress'}
    global id 
    id = easy.bugID()
    print('Current Code Status => ')
    """ CAN  USE TABULATE LIBRARY BUT ALREADY USED TOO MANY ${NOT TO TAKE BURDEN}"""
    status = easy.select('buginfo', '*', 1, f"bugID = '{id}'") 
    print(f"\n {id}                                        Bug Status : {actualsts[list(status)[1]]}\n\n Description : {list(status)[2]} \n\n Severity : {list(status)[3]}                                        Fixing Days : {list(status)[4]}               \n\n Opening Date : {list(status)[5]}                      closing date : {list(status)[6]} \n")
def assignes():#switch assignes
    id = easy.bugID()
    if (id != None):
        cur.execute(f"select assign_to from assign where bugID = '{id}'")
        print('fetching Assignes ... ')
        os.system('clear')
        print(f'Current Assignee => {cur.fetchone()}')
    elif (id == None):
        id = input('Enter the bugID')# if the bugID is not present
        cur.execute(f"select assign_to from assign where bugID = '{id}'")
        print(f'Current Assignee => {cur.fetchone()}')
    print(' < -- Change Assignes --> \n {1} => Draw Names  \n {2} => Continue')
    choice = int(input('Enter your choice'))
    if(choice == 1):
        names = str(input('Enter the name to find the EmailID : '))
        details = easy.select('userinfo', 'username,email', 90, f"username like '{names}%'")
        os.system('clear')
        print('( username , Email )\n', *(i for i in details), sep='\n')
    else:names = str(input('Enter the name to find the EmailID : ' ))
    cur.execute(f"select username from userinfo where username like '{names}%'")
    if (cur.fetchall() != []):
        newassign = str(input('Enter the new assignee : '))
        os.system('clear')
        print('Updating Assignee ... ')
        time.sleep(4)
        os.system('clear')
        cur.execute(f"update assign set assign_to = '{newassign}' where bugID = '{id}'")
        print('Assignee updated successfully')
        time.sleep(2)
    db.commit()
    os.system('clear')
    print("The memeber doesn't exist"), time.sleep(4)
    if input('Press Enter to continue ...') == '': os.system('clear'), work()

def allbugs():
    os.system('clear')
    print('fetching data ... '), time.sleep(4)
    os.system('clear')
    print('--------------------------------- All Bugs ---------------------------------')
    cur.execute("select * from buginfo")
    print('(bugID, status, description, severity, fixingdays, openingdate, closingdate, priority)\n',*(i for i in cur.fetchall()), sep='\n \n')
    print("PRIORITY => {1:'high', 2:'Medium', 3:'low'}")

def work():
    print('--------------------------------- What you want to do ---------------------------------\n {1} => Edit code status \n {2} => Switch Assignes \n {3} => Bug Report \n {4} => See All bugs \n {5} => logout / login ')
    newchoice = int(input('Enter your choice'))
    if newchoice == 1:
        codestatus()
    elif newchoice == 2:
        assignes()
    elif newchoice == 3:
        bugreport()
    elif newchoice == 4:
        allbugs()
    elif newchoice == 5:
        user_login()

def user_login():  #login/Signin
    time.sleep(2),os.system('clear')
    print('--------------------------------- Login / Singup ---------------------------------')
    print(' {1}=>(login) \n {2}=>(singup)')
    choice = int(input('Enter your choice'))
    if (choice == 1):
        print('--------------------------------- Login Here ---------------------------------')
        credentials() # home page if the credentials didn't match then again login
    elif (choice == 2):
        print('--------------------------------- Signup Here ---------------------------------')
        username = str(input('Enter your Name : '))
        # cur.execute(f"select username from userinfo where {username} = '';")
        credentials()
    else:
        print('--------------------------------- Some Error occurred ---------------------------------')
        user_login()

    def verification(choice):
        if (choice == 1):
            # cur.execute(f"select * from userinfo where email = '{email}' and password = '{password}'; ")
            record = easy.select('userinfo', '*', 1, f"password = '{password}' and email = '{email}'")
            if record != None:
                os.system('clear')
                print('Logged in successfully') # go to the main page
                work()
            else:
                os.system('clear'),time.sleep(2)
                print('--------------------------------- Wrong Credentials ---------------------------------')
                user_login()
        elif (choice == 2):
            cur.execute(f"insert into userinfo (username,password,email,hash)values ('{username}','{password}','{email}','{easy.hashID()}')")
            db.commit()
            os.system('clear'),time.sleep(2)
            print('--------------------------------- Signed up successfully ---------------------------------')
            user_login()

    verification(choice)


user_login()