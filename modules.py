import random
import mysql.connector as m 
import os 
import time
db = m.connect(host="localhost", user="ins-nishidh", passwd="ins-nishidh-@47", database="bugs", ssl_disabled=True)
#cursor object
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
    if str(value).isdigit() != True:
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


def loading_bar(total, prefix='Progress:', suffix='Complete', bar_width=50, fill='█', delay=0.1):
    """
    Displays a centered loading bar in the terminal.

    :param total: Total steps for the loading bar
    :param prefix: Text before the bar
    :param suffix: Text after the bar
    :param bar_width: Width of the loading bar
    :param fill: Character to fill the bar
    :param delay: Delay between updates in seconds
    """
    # Get terminal width
    columns = int(os.get_terminal_size().columns)

    for step in range(total + 1):
        percent = step / total * 100
        filled = int(bar_width * step // total)
        bar = fill * filled + ' ' * (bar_width - filled)

        # Construct the loading bar string
        line = f"{prefix} |{bar}| {percent:.1f}% {suffix}"

        # Center the line in the terminal
        centered_line = line.center(columns)

        # Print and refresh
        print(f"\r{centered_line}", end='', flush=True)
        time.sleep(delay)

    # Print a new line after completion
    print()

# Example usage

    

