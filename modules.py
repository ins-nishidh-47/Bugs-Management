import random
import mysql.connector as m 
import os 
db = m.connect(host="localhost", user="root", passwd="nishidh@123", database="bug_tracking")

cur = db.cursor()

def cleared():
    os.system('clear')

def hashID():  #creating HashIds for account protection
    hashelements = 'ABCDEFIGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    elements = "#$*&!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    specialval = "¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿"
    hashIds = ''
    for i in range(0, 5):
        hashIds += (hashelements[random.randint(0, len(hashelements) - 1)] + elements[
            random.randint(0, len(elements) - 1)] + specialval[random.randint(0, len(specialval) - 1)])
    # print(hashIds)
    return hashIds

def bugID():
    id = input("Enter the bugId of the bug : ")
    return id

def select(tablename, first: str, tofetch: int, condition: str = None):
    # cur.execute(f"select {first} from {tablename} where {condition}")
    if condition == None:cur.execute(f"select {first} from {tablename}")
    else:cur.execute(f"select {first} from {tablename} where {condition}")
    if tofetch == 1:return cur.fetchone()
    else:return cur.fetchall()

def update(tablename, column, value, condition: str):
    if value.isdigit() != True:
        newval = 1
        try:
            newval = float(value)
        except:
            value = value

        try:
            if type(float(value)) == float :
                pass
        except ValueError:
            if newval != float :
                value = f"'{value}'"
                print(value)
    cur.execute(f"update {tablename} set {column} = {value} where {condition}")    
    db.commit()
    

