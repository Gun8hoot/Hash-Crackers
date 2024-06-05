#!/bin/python3

import hashlib

word = ["root", "password", "password123", "notthat", "nothing", "void", "print", "ifelseelif", "S3Cur$D"]

def loop():
    word = ["root", "password", "password123", "notthat", "nothing", "void", "print", "ifelseelif", "S3Cur$D"]
    y = 0
    for x in range(9):
        m = hashlib.md5()
        m.update(word[y].encode())
        sha = m.hexdigest()
        print("|", word[y], " : ", sha, "   |")
        y += 1
def lfile():
    
    f = open("tmp/wl", "r")
    wl = f.readlines()
    count = 0
    for line in wl:
        m = hashlib.md5()
        m.update(line.encode())
        hashed = m.hexdigest()
        count += 1
        print("|", line, " : ", hashed, "    |")



print("+----------------------------------------------------+")
try:
    loop()
except ValueError:
    pass
lfile()
print("+----------------------------------------------------+")