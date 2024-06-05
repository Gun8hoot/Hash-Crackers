#!/bin/python3

# Import all python module
try:
    from colorama import Fore as cl
except ValueError:
    pass
import time, string, os, sys
import hashlib
import string
from module.Dictionary import dict_attack
from module.Bruteforce import brutef_attack

# Generals vars
path = ""
banner = open("banner.txt", "r")
showbanner = banner.read()

#
# Decoration
os.system('cls' if os.name == 'nt' else 'clear')
print(cl.LIGHTGREEN_EX + showbanner + cl.RESET)
print(cl.LIGHTRED_EX + "                           Made with ♥️" + cl.RESET)

# Main code
try:
    while True:
        print(cl.LIGHTCYAN_EX + "\n1) Dictionary attack\n2) Using Bruteforce attack\n3) Exit\n" + cl.RESET)
        choise = input(cl.GREEN + "[!] : ")
        if choise == '1':
            dict_attack()
            break
        elif choise == '2':
            brutef_attack()
        elif choise == '3':
            print(cl.LIGHTRED_EX + '\n[!] Goodbye' + cl.RESET)
            sys.exit(0)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(cl.LIGHTGREEN_EX + showbanner + cl.RESET)
            print(cl.LIGHTRED_EX + '\n[!] Please enter a valid choise.\n' + cl.RESET)

except KeyboardInterrupt:
    print(cl.LIGHTRED_EX + '\n\n[!] FATAL_ERROR: The script have been interrupt by the user' + cl.RESET)
    sys.exit(0)
