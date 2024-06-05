try:
    from colorama import Fore as cl
except ValueError:
    pass
import time, string, os, sys
import hashlib
import string
from module.writereport import writerep

banner = open("banner.txt", "r")
showbanner = banner.read()

def __report__(x):
    print("dir works")
    path = "report/"
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    cr_report = open(path + time.strftime('%d-%m-%Y') + "_report-crackers.txt", "w")
    report = cr_report.writelines(x)

    print(f"[!] Hash cracked found: {x}")

def dict_attack():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(cl.LIGHTGREEN_EX + showbanner + cl.RESET)
    while True:
        try:

            # Dictionary Attack vars
            hashpath = input(cl.LIGHTYELLOW_EX + "\n[!] Enter the full path of the hash file: " + cl.RESET)
            ophash = open(hashpath, "r")
            hashfile = ophash.read()
            PathWL = input(cl.LIGHTYELLOW_EX + "\n[!] Enter the full path of the wordlist file: " + cl.RESET)
            print(cl.YELLOW + f"\n[!] Your bruteforce result is write in the ./result/ directory" + cl.RESET)
            print(cl.YELLOW + f"[-] Your hash is : {hashfile}" + cl.RESET)
            opWL = open(PathWL,encoding=str('utf-8'))
            WL = opWL.readlines()
            m = hashlib.md5()
            count = 0
            encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']

            # Hash Cracking Loop
            for line in WL:
                count += 1
                m.update(line.encode())
                pipe = m.hexdigest()
                print(pipe)
                if pipe == hashfile:
                    __report__(line)
                    print(cl.LIGHTGREEN_EX + f'[!] Hash password found ! {hashfile}:{line}' + cl.RESET)
                    result = pipe + " : " + hashfile
                    print(result)
                else:
                    pass

            
        except FileNotFoundError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(cl.LIGHTGREEN_EX + showbanner + cl.RESET)
            print(cl.LIGHTRED_EX + f'\n[!] ERROR: Enter a valid path!' + cl.RESET)
        else:
            break