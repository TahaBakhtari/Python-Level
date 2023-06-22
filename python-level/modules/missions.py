def missoins():
    from colorama import Fore
    import os, subprocess , platform , string , time

    def clear():
        os_virson = platform.uname()
        if "Windows" in os_virson:
            os.system("cls")
        else:
            os.system("clear")
    clear()

    def level_1():
        print(Fore.LIGHTCYAN_EX + "Please Enter The Output Of This Code")
        print("""
quiz number 1
        
    x = "mycode"
    print(x[6])
    -----------
    a = e
    b = Error
    c = d
    d = o
    """)
        answer = input(Fore.LIGHTGREEN_EX + "Enter Your Answer : ")
        if answer == "b":
            return 2.5
        else:
            return 0.0
        
    def level_2():
        clear()
        print(Fore.LIGHTCYAN_EX + "Please Enter The Output Of This Code")
        print("""
quiz number 2
        
    s = 2
    u = "13"
    print(s*u)
    -----------
    a = 26
    b = Error
    c = 1313
    d = 169
    """)
        answer = input(Fore.LIGHTGREEN_EX + "Enter Your Answer : ")
        if answer == "c":
            return 2.5
        else:
            return 0.0
    
    def level_3():
        clear()
        print(Fore.LIGHTCYAN_EX + "Please Enter The Output Of This Code")
        print("""
quiz number 3
        
    x = 13
    def san():
        x = 12

    san()
    print(x)
    -----------
    a = 13
    b = 12
    c = Error
    """)
        answer = input(Fore.LIGHTGREEN_EX + "Enter Your Answer : ")
        if answer == "a":
            return 2.5
        else:
            return 0.0
    
    def level_4():
        clear()
        print(Fore.LIGHTCYAN_EX + "Please Enter The Output Of This Code")
        print("""
quiz number 4
        
    a = 4
    def San():
        global a
        a = 9
    print(a)
    -----------
    a = 9
    b = 13
    c = Error
    d = 4
    """)
        answer = input(Fore.LIGHTGREEN_EX + "Enter Your Answer : ")
        if answer == "d":
            return 2.5
        else:
            return 0.0
        
    def level_5():
        clear()
        print(Fore.LIGHTCYAN_EX + """
   Quiz Number 5

+ Write a function that take number 4 
+ and raises it to the power of 2
+ and print the result
""")
        time.sleep(7)
        open("codes.py","w").write("")
        if "Windows" in platform.uname():
            os.system("codes.py")
        else:
            os.system("open codes.py")
        time.sleep(3)
        def check_answer():
            code = open("codes.py","r").read()
            if "def " in code and "(" in code and ")" in code:
                if "Windows" in platform.uname():
                    output = subprocess.getoutput("python codes.py")
                else:
                    output = subprocess.getoutput("python3 codes.py")
                os.remove("codes.py")
                if output == "16":
                    return 2.5
                else:
                    return 0.0
            else:
                return 0.0
        while True:
            answer = input(Fore.LIGHTGREEN_EX + "did you finish it ? [ y ] ").lower()
            if answer == "y" or answer == "yes":
                point = check_answer()
                return point
            else:
                return 0.0

    def level_6():
        clear()
        print(Fore.LIGHTCYAN_EX + """
   Quiz Number 6

+ Write a script that changes the data
+ in the following list to steering, separated by ","

data = [ "apple" , "banana" , "orange" ]
        """)
        time.sleep(7)
        open("codes.py","w").write("")
        if "Windows" in platform.uname():
            os.system("codes.py")
        else:
            os.system("open codes.py")
        time.sleep(3)
        def check_answer():
            code = open("codes.py","r").read()
            if ".join" in code:
                if "Windows" in platform.uname():
                    output = subprocess.getoutput("python codes.py")
                else:
                    output = subprocess.getoutput("python3 codes.py")
                if output == "apple,banana,orange":
                    return 2.5 
                else:
                    return 0.0
            elif "for " in code:
                return 1.0
            else:
                return 0.0
        while True:
            answer = input(Fore.LIGHTGREEN_EX + "did you finish it ? [ y ] ").lower()
            if answer == "y" or answer == "yes":
                point = check_answer()
                os.remove("codes.py")
                return point
            else:
                os.remove("codes.py")
                return 0.0
    
    def level_7():
        clear()
        print(Fore.LIGHTCYAN_EX + """
   Quiz Number 7

+ Write a script that take this password : /d;@345V
+ and if it was more than 6 and sepcial
+ words was in the password , return OK
        """)
        time.sleep(7)
        open("codes.py","w").write("")
        if "Windows" in platform.uname():
            os.system("codes.py")
        else:
            os.system("open codes.py")
        time.sleep(3)
        def check_answer():
            code = open("codes.py","r").read()
            if "if" in code and "6" in code and "for " in code and "in" in code:
                if "Windows" in platform.uname():
                    output = subprocess.getoutput("python codes.py")
                else:
                    output = subprocess.getoutput("python3 codes.py")
                if output.upper() == "OK":
                    return 2.5
                else:
                    return 0.0
            else:
                return 0.0
        while True:
            answer = input(Fore.LIGHTGREEN_EX + "did you finish it ? [ y ] ").lower()
            if answer == "y" or answer == "yes":
                point = check_answer()
                os.remove("codes.py")
                return point
            else:
                os.remove("codes.py")
                return 0.0  

    def level_8():
        clear()
        print(Fore.LIGHTCYAN_EX + """
   Quiz Number 8   

+ Write a script that takes a name that consists of 
+ several words and pastes the first letters of
+ each word together and prints the result in capital letters.
        """)
        time.sleep(7)
        open("codes.py","w").write("")
        if "Windows" in platform.uname():
            os.system("codes.py")
        else:
            os.system("open codes.py")
        time.sleep(3)

        def check_answer():
            code = open("codes.py","r").read()
            if "for " in code and ":" in code and "[0]" in code and ".upper()" in code:
                return 2.5
            else: 
                return 0.0
        while True:
            answer = input(Fore.LIGHTGREEN_EX + "did you finish it ? [ y ] ").lower()
            if answer == "y" or answer == "yes":
                point = check_answer()
                os.remove("codes.py")
                return point
            else:
                os.remove("codes.py")
                return 0.0
    point = level_1() + level_2() + level_3() + level_4() + level_5() + level_6() + level_7() + level_8()
    print(Fore.LIGHTGREEN_EX + "\n [!] Registered")
    open("setting/level.txt","w").write(f"{point} from 20")
    time.sleep(1)
