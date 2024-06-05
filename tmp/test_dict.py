try:
    from colorama import Fore
except ValueError:
    pass
import hashlib

file = open("./wl")
wl = file.readline()

def dicte():
    for line in wl:
        count = 0
        count += 1
        md5 = hashlib.md5
        md5.update(line.encode())
        hashed = m.hexdigest()
        print(hashed)
        
def indv():
    try:
        word = ["root", "password", "password123", "notthat", "nothing", "void", "print", "ifelseelif", "S3Cur$D"]
        for x in range(9):
            y = 1
            md5 = hashlib.md5
            md5.update(word[y])
            hashed = md5.hexdigest()
        print(hashed)
    except KeyboardInterrupt:
        print("quit")

dicte()
print("\n\n---------------\n\n")
indv()