import os
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
import subprocess , platform , string , time
from colorama import Fore , Back , Style
from modules import missions

def clear():
    os_virson = platform.uname()
    if "Windows" in os_virson:
        os.system("cls")
    else:
        os.system("clear")
clear()

def check_password(password):
        if len(password) < 6:
            if string.punctuation not in password:
                return "BAD"
            else:
                return "MORE"
        else:
            return "OK"
    

def account():
    os.chdir("setting")
    if "Windows" in platform.uname():
        datas_list = subprocess.getoutput("dir /b")
    else:
        datas_list = subprocess.getoutput("ls")
    if "account.txt" in datas_list:
        userdata = open("account.txt","r").read().split(sep=":")
        clear()
        os.chdir("..")
        return userdata[0]
    else:
        username = input(Fore.LIGHTYELLOW_EX + "Please Choose One Username : ")
        while True:
            password = input(Fore.LIGHTYELLOW_EX + "\nAnd Please Choose a Password now : ")
            if check_password(password) == "BAD":
                print(Fore.LIGHTRED_EX + "\nPlease Choose a Stonger Password")
            elif check_password(password) == "MORE":
                print(Fore.LIGHTRED_EX + "\nPassword Shoud be More Than 6\n")
            else:
                print(Fore.LIGHTGREEN_EX + "\nWait...")
                break
        charecters = list(string.punctuation)
        charecter = ""
        for char in charecters:
            if char in password:
                None
            else:
                charecter.join(char)
                open("account.txt","w").write(f"{username}{char}{password}")
        clear()
        os.chdir("..")
        sepp = charecter
        print(sepp)
        return sepp

spsep = account()

def edit_username():
    clear()
    global spsep
    userdata = open("setting/account.txt","r").read().split(sep=spsep)
    while True:
        password = input(Fore.LIGHTYELLOW_EX + "Please Enter Your Password : ")
        print(userdata[1])
        if userdata[1] == password:
            username = input(Fore.LIGHTYELLOW_EX + "\nChoose a Username : ")
            open("setting/account.txt","w").write(f"{username}{spsep}{password}")
            print(Fore.LIGHTGREEN_EX + "\nUsername Changed :)")
            time.sleep(2)
            clear()
            break
        else:
            print(Fore.LIGHTCYAN_EX + """
Password Is Not Correct

[1] Main Menu 
[2] Try Again
            """)
            select = input("Which One : ")
            if select == "2":
                clear()
                continue
            else:
                clear()
                break

def show_ansers():
    clear()
    level = open("setting/level.txt","r").read()
    try:
        if int(level.split(sep=" ")[0].replace(".5","")) < 10:
            time.sleep(0.5)
            print(Fore.LIGHTRED_EX + "\n  * Your Point Shoud Be More Than 10 *")
            time.sleep(2)
            input(Fore.LIGHTYELLOW_EX + "\n  Enter For The Menu...")
            time.sleep(0.5)
        else:
            os.chdir("setting")
            if "Windows" in platform.uname():
                os.system("answers.txt")
            else:
                os.system("open answers.txt")
            os.chdir("..")
            print(" Waiting...")
            time.sleep(4)
    except ValueError:
            time.sleep(0.5)
            print(Fore.LIGHTRED_EX + "\n  * Your Point Shoud Be More Than 10 *")
            time.sleep(2.5)
def display_level():
    clear()
    time.sleep(0.4)
    global spsep
    username = open("setting/account.txt","r").read().split(sep=spsep)[0]
    level = open("setting/level.txt","r").read().replace(".0","")
    if level == "":
        print(Fore.LIGHTRED_EX + "\nYou Dont Have Any Point Yet :(")
        time.sleep(2)
    else:
        print(Fore.GREEN +"\n    " + Back.LIGHTWHITE_EX + f"{username} Level : {level}" + Style.RESET_ALL)
        time.sleep(2)
        input(Fore.LIGHTYELLOW_EX + "\n    Enter For The Menu...")
        time.sleep(0.5)

def about_developper():
    clear()
    text = """
Hello , my name is Taha and im only 14
I will be happy if you follow me on GitHub
This is my GitHub ID : 

Taha-Security

Be In Touch With Me:

+ Email address : tahabakhtari88@gmail.com
"""
    sen = text.split(sep="\n")
    for i in sen:
        time.sleep(0.1)
        print(i)
    time.sleep(2)
    input(Fore.LIGHTGREEN_EX + "\nEnter For The Menu...")
    time.sleep(0.5)

def menu():
    print(Fore.LIGHTYELLOW_EX + "\n    Please Choose One Option ! [v1]")
    time.sleep(0.1)
    items = """
    [1] Start The Game
    [2] My Python Level
    [3] Answers
    [4] Edit Username
    [5] About Developer
    [0] Exit
    """
    sen = items.split(sep="\n")
    for i in sen:
        time.sleep(0.1)
        print(Fore.LIGHTWHITE_EX + i)

while True:
    clear()
    menu()
    select = input(Fore.LIGHTGREEN_EX + "    Enter One Number :" + Fore.LIGHTYELLOW_EX + " ")
    if select == "1":
        missions.missoins()
    elif select == "2":
        display_level()
    elif select == "3":
        show_ansers()
    elif select == "4":
        edit_username()
    elif select == "5":
        about_developper()
    elif select == "0":
        clear()
        exit(Fore.LIGHTCYAN_EX + "\n\n\nGood Bye\n\n\n")