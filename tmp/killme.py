import hashlib

def md5_hash_cracker(target_hash, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            for word in file:
                word = word.strip()  # Remove any trailing whitespace/newlines
                m = hashlib.md5()  # Create a new MD5 hash object
                m.update(word.encode())  # Update the hash object with the encoded word
                guess_hash = m.hexdigest()  # Get the hexadecimal digest of the hash
                
                # Check if the generated hash matches the target hash
                if guess_hash == target_hash:
                    return word
    except FileNotFoundError:
        print(f"The file {wordlist_file} was not found.")
        return None

    return None

# Example usage:
target_hash = '5d41402abc4b2a76b9719d911017c592'  # Hash for 'hello'
wordlist_file = './wl.txt'
result = md5_hash_cracker(target_hash, wordlist_file)

if result:
    print(f"The original string is: {result}")
else:
    print("Original string not found in the wordlist.")