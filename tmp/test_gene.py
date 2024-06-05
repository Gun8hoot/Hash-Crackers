#!/bin/python3

import hashlib
import itertools
import string
import time
from colorama import Fore as cl

def md5_hash_cracker(target_hash, max_length):
    # Define the possible characters (this example uses only lowercase letters and digits)
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    timed = time.perf_counter()
    print(f"\x1b[41m {timed} \033[00m")

    # Try all combinations of characters up to the specified maximum length
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.md5(guess.encode()).hexdigest()
            print(guess_hash, ':', guess)
            
            # Check if the generated hash matches the target hash
            if guess_hash == target_hash:
                print(time.perf_counter())
                return guess
    
    return None

# Example usage:
target_hash = '5d41402abc4b2a76b9719d911017c592'
max_length = 10
result = md5_hash_cracker(target_hash, max_length)

if result:
    print(f"The original string is: {result}")
else:
    print("Original string not found within the given length.")