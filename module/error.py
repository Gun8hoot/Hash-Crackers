try:
    from colorama import Fore as cl
except ValueError:
    pass
import os
if os.name == 'nt':
    banner = open('banner_win.txt', "r")
    showbanner = banner.read()
else:
    banner = open('banner_unix.txt', "r")
    showbanner = banner.read()


def error_happen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(cl.LIGHTGREEN_EX + showbanner + cl.RESET)
    print(cl.LIGHTRED_EX + "\n[!] WARNING AN ERROR HAPPEN DURING THE CODE EXECUTION" + cl.RESET)

error_happen()