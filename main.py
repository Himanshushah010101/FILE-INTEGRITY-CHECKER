print("FILE INTEGRITY CHECKER")

# THIS PROGRAM WILL FIND A TEXT FILE HASH VALUES AND CHANGED OR TEMPERED BY ANYONE SO YOU CAN FIND EASILY HELP BY HASH VALUES!!!  

import hashlib

def calculate_hash(file_path):
    hash_algo = hashlib.sha256()

    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()
    except FileNotFoundError:
        return None

file = input("Enter file path: ")
hash_value = calculate_hash(file)

if hash_value:
    print("File Hash:", hash_value)
else:
    print("File not found!")

 
