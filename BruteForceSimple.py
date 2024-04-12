import itertools
import string
import time
from passlib.hash import md5_crypt

salt = "hfT7jp2q"
password = "zzzhhh"
full_hash = "$1$hfT7jp2q$ksyQH0vzd6XE0B6mJEq4//"

# Define all characters to use in the password
chars = 'abcdefghijklmnopqurstuvwxyz'
rchars = 'zyxwvutsruqponmlkjihgfedcba'

# Define the maximum password length to try
max_length = 6

# Track the start time of the password cracking process
start_time = time.time()

# Try all possible combinations of characters up to max_length
for length in range(6, max_length + 1):
    for combination in itertools.product(rchars, repeat=length):
        # Join the characters in the combination to form a password candidate
        candidate = "".join(combination)
        print("Trying password:", candidate)

        hashed_password = md5_crypt.using(salt=salt).hash(candidate)

        # Check if the candidate matches the password
        if full_hash == hashed_password:
            # Track the end time of the password cracking process
            end_time = time.time()
            print("Password found:", candidate)
            # Calculate the time taken to crack the password
            time_taken = end_time - start_time
            print("Time taken:", time_taken, "seconds")
            # Terminate the password cracking process
            raise SystemExit