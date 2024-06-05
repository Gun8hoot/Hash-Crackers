try:
    from colorama import Fore as cl
except ValueError:
    pass
import time, string, os, sys, itertools
import hashlib

banner = open("banner.txt", "r")
showbanner = banner.read()

def brutef_attack():
    # Banner
    os.system('cls' if os.name == 'nt' else 'clear')
    print(cl.LIGHTGREEN_EX + showbanner + cl.RESET)

    raw_hash = input("\n[!] Enter the hash to decode: ")
    result = bruteforcenow(raw_hash)
    if result:
        os.system("cls" if os.name == "nt" else "clear")
        print(cl.LIGHTGREEN_EX + showbanner + cl.RESET)
        print(cl.LIGHTRED_EX + f"[+] {raw_hash} : {result}" + cl.RESET)
        quit()
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(cl.LIGHTRED_EX + "[!] ERROR" + cl.RESET)

        
def bruteforcenow(enc_hash):
    # vars
    max_length = 30
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Generate character
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.md5(guess.encode()).hexdigest()
            print(guess_hash, ':', guess)
            if guess_hash == enc_hash:
                print(time.perf_counter())
                return guess

