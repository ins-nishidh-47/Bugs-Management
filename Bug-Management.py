import mysql.connector as mysql
import modules as easy
import os
import time

# actualsts = {1:'Intest', 2:'Open', 3:'Close', 4:'Reopen', 5:'Inprogress'}

# Connect to MySQL
db = mysql.connect(host="localhost", user="root", passwd="nishidh@123", database="bug_tracking")
cur = db.cursor()  #creating cursor

def credentials():  #taking credentials
    global email
    global password
    email, password = str(input('Enter the email address : ')), str(input("Enter your password"))

def codestatus():
    time.sleep(3)
    os.system('clear')
    bugID = input('Enter the Id of your respective Bug : ')
    print('\n',{1:'Intest', 2:'Open', 3:'Close', 4:'Reopen', 5:'Inprogress'})
    choice = int(input('Enter your choice (1/2/3/4/5) => '))
    easy.update('buginfo', 'bugstatus', choice, f"bugID = '{bugID}'")
    os.system('clear')
    print('Updating ....'), time.sleep(3)
    print('------------------- Updated Successfully -------------------')

def addbug():
    try:
        id = easy.bugID()
        bugds = str(input('Enter the bug Description : '))
        severity = str(input('Enter the severity of the bug : '))
        bugstatus = str(input("{1:'Intest', 2:'Open', 3:'Close', 4:'Reopen', 5:'Inprogress'} Enter (1/2/3/4/5): " ))
        reqdays = int(input('Enter the no. of days required : '))
        opendt = str(input('Enter the date of Opening : '))#2020-03-23
        closingdt = str(input('Enter the date of Closing (expected)'))
        priority = int(input("PRIORITY => {1:'high', 2:'Medium', 3:'low'} Enter (1/2/3): "))
        assign_to = str(input('Enter the name of the assigne: '))
        assign_by = str(input('Enter the name of bug assigner: '))
        cur.execute(f"insert into buginfo values ('{id}','{bugstatus}', '{bugds}', '{severity}', {reqdays}, '{opendt}', '{closingdt}', {priority})"), db.commit()
        cur.execute(f"insert into assign (assign_to,assigned_by,bugID) values ('{assign_to}','{assign_by}','{id}')"), db.commit()
        print('------------------ BUG SUCCESSFULLY UPDATED ------------------'), time.sleep(4)
        work()
    except:
        print('\n'*4 + '--------------------------- SOMETHING WENT WRONG ---------------------------')
        addbug()

def bugreport():  #edit code status  
    global id 
    id = easy.bugID()
    actualsts = {1:'Intest', 2:'Open', 3:'Close', 4:'Reopen', 5:'Inprogress'}
    print('Current Code Status => ')
    """ CAN  USE TABULATE LIBRARY BUT ALREADY USED TOO MANY ${NOT TO TAKE BURDEN}"""
    status = easy.select('buginfo', '*', 1, f"bugID = '{id}'") 
    print(f"\n {id}                                        Bug Status : {actualsts[list(status)[1]]}\n\n Description : {list(status)[2]} \n\n Severity : {list(status)[3]}                                        Fixing Days : {list(status)[4]}               \n\n Opening Date : {list(status)[5]}                      closing date : {list(status)[6]} \n \n \n")

def assignes():#switch assignes
    try:
        id = easy.bugID()
        if (id != None):
            cur.execute(f"select assign_to,bugID,assigned_by from assign where bugID = '{id}'")
            print('fetching Assignes ... '), time.sleep(3)
            os.system('clear')
            # print(f'Current Assignee => {cur.fetchone()}' if cur.fetchone!= None else print('-------------- BugID not found --------------'), time.sleep(4) ,assignes())
            bugdetails = cur.fetchone()
            if bugdetails!= None:
                print(f'Current Assignee => {bugdetails}')
            else:
                print('-------------- BugID not found --------------')
                inpu = str(input('Press Enter to see all bugs: '))
                if inpu == '':
                    allbugs(), print()
                assignes()
        elif (id == None):
            id = input('Enter the bugID')# if the bugID is not present
            cur.execute(f"select assign_to from assign where bugID = '{id}'")
            print(f'Current Assignee => {cur.fetchone()}')
        print(' < -- Change Assignes --> \n {1} => Draw Names  \n {2} => Continue  \n {3} => Back')
        choice = int(input('Enter your choice'))
        if(choice == 1):
            names = str(input('Enter the name to find the EmailID : '))
            details = easy.select('userinfo', 'username,email', 90, f"username like '{names}%'")
            os.system('clear')
            print('( username , Email )\n', *(i for i in details), sep='\n')
            time.sleep(4)
        elif (choice == 2):
            email = str(input('Enter the EmailID of the person to check it exist or not: '))
            details = easy.select('userinfo', 'username,email', 90, f"email like '{email}'")
            print(details)
            # easy.update('assign', 'assign_to', email, f"bugID = '{id}'")
        elif (choice == 3):
            time.sleep(2), os.system('clear')
            work()
        else:
            os.system('clear'),print('------------------------- wrong choice selected -------------------------')
            time.sleep(4)
            assignes()
        if (details != []):
            newassign = str(input('Enter the new assignee EmailId : '))
            os.system('clear')
            print('Updating Assignee ... ')
            time.sleep(4)
            os.system('clear')
            cur.execute(f"update assign set assign_to = '{newassign}' where bugID = '{id}'")
            print('Assignee updated successfully')
            time.sleep(2)
        else:
            print("--------------- Enter email properly ; This name didn't exist in our data ---------------")
            assignes()
        db.commit()
        os.system('clear'), time.sleep(3)
        if input('Press Enter to continue ...') == '': os.system('clear'), work()
    except:
        print('\n'*4 + '--------------------------- SOMETHING WENT WRONG ---------------------------')
        work()


def allbugs():
    os.system('clear')
    print('fetching data ... '), time.sleep(4)
    os.system('clear')
    print('--------------------------------- All Bugs ---------------------------------')
    cur.execute("select * from buginfo")
    print('(bugID, status, description, severity, fixingdays, openingdate, closingdate, priority)\n',*(i for i in cur.fetchall()), sep='\n \n')
    print("PRIORITY => {1:'high', 2:'Medium', 3:'low'}")

def work():
    print('--------------------------------- What you want to do ---------------------------------\n {1} => Edit code status \n {2} => Switch Assignes \n {3} => Bug Report \n {4} => See All bugs \n {5} => Add bugs \n {6} => logout / login ')
    newchoice = int(input('Enter your choice'))
    if newchoice == 1:
        codestatus()
        work()
    elif newchoice == 2:
        assignes()
    elif newchoice == 3:
        bugreport()
        work()
    elif newchoice == 4:
        allbugs()
        work()
    elif newchoice == 5:
        addbug()
    elif newchoice == 6:
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
