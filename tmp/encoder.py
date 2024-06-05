import hashlib
string = "root"

md5 = hashlib.md5()
encoded = md5.update(string.encode())
hashed = md5.hexdigest()
print(hashed, "\n\n\n\n\n")

try:
    from colorama import Fore
except ValueError:
    pass


file = open("./wl")
wl = file.readline()

def dicte():
    for line in wl:
        count = 0
        count += 1
        md5.update(line.encode())
        hasha = md5.hexdigest()
        print(hasha)
        
def indv():
    word = ["root", "password", "password123", "notthat", "nothing", "void", "print", "ifelseelif", "S3Cur$D"]
    for x in range(9):
        y = 1
        md5 = hashlib.md5
        md5.update(word[y])
        hashed = md5.hexdigest()
        print(hashed)

dicte()
print("\n\n---------------\n\n")
indv()