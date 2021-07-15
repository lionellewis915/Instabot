# Necessary Packages
from instapy import InstaPy as root
from instapy import smart_run as smart_r
from getpass import getpass as gp

from colorama import *
init(convert=True)

import os


os.system('cls')

def title(): # Onetime title screen subroutine   
    print(Fore.CYAN + "              /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$      /$$$$$$$   /$$$$$$  /$$$$$$$$")
    print("             |_  $$_/| $$$ | $$ /$$__  $$|__  $$__//$$__  $$    | $$__  $$ /$$__  $$|__  $$__/")
    print("               | $$  | $$$$| $$| $$  \__/   | $$  | $$  \ $$    | $$  \ $$| $$  \ $$   | $$   ")
    print("               | $$  | $$ $$ $$|  $$$$$$    | $$  | $$$$$$$$    | $$$$$$$ | $$  | $$   | $$   ")
    print("               | $$  | $$  $$$$ \____  $$   | $$  | $$__  $$    | $$__  $$| $$  | $$   | $$   ")
    print("               | $$  | $$\  $$$ /$$  \ $$   | $$  | $$  | $$    | $$  \ $$| $$  | $$   | $$   ")
    print("              /$$$$$$| $$ \  $$|  $$$$$$/   | $$  | $$  | $$    | $$$$$$$/|  $$$$$$/   | $$   ")
    print("             |______/|__/  \__/ \______/    |__/  |__/  |__/    |_______/  \______/    |__/   ")
    print(Fore.MAGENTA + "             Created By: Lionel Lewis 2021" + Fore.WHITE)
    print("")

def usage():
    print("[--creds, -c] Set Username and Password")
    print("[--help, -h] Displays usage instructions")
    print("[--likes, -l] Setup bot parameters for liking pictures")
    print("[--follow, -f] Setup bot parameters for following users")
    print("[--unfollow, -uf] Setup bot parameters for unfollowing users")
    print("[--exec, -e] Execute the program")

def creds():
    global usrName 
    global pswd

    try:
        usrName = input("Username: ")
        print(Fore.RED + "              > For security reasons the password will NOT be displayed as it is being typed <" + Fore.WHITE)
        pswd = gp()
        print("")
        print("Username: {0}, Password: {1}".format(usrName, pswd))
        
    except Exception as error:
        print(Fore.RED + "ERROR!" + Fore.WHITE, error)
    

def execute():
    session = root(username=usrName, password=pswd, headless_browser=True)


def likes():
    pass

def follow():
    pass

def unfollow():
    pass

if __name__ == '__main__':
    title()

    act = input(">>> ")

    if act == "--creds" or "-c":
        creds()
    elif act == "--help" or "-h":
        usage()
    elif act == "--likes" or "-l":
        likes()
    elif act == "--follow" or "-f":
        follow()
    elif act == "--unfollow" or "-uf":
        unfollow()
    elif act == "--exec" or "-e":
        execute()
    else:
        pass
