try:
    from colorama import Fore as cl
except ValueError:
    pass
import hashlib, string, os
from module.writereport import writerep

if os.name == 'nt':
    banner = open('banner_win.txt', 'r')
    showbanner = banner.read()
else:
    banner = open('banner_unix.txt', 'r')
    showbanner = banner.read()

def md5_encoderpy():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(cl.LIGHTGREEN_EX + showbanner + cl.RESET)
    password = input(cl.BLUE + "\n[!] Please enter the password to encode: " + cl.RESET)
    m = hashlib.md5()
    m.update(password.encode())
    encoded = m.hexdigest()
    print(cl.RED + f"[!] Your MD5 encoded password is : {encoded}\n\n" + cl.RESET)
    writerep(password, encoded)

