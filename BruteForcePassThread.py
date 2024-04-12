import itertools
import string
import time
import threading
import concurrent.futures

# Password Cracker Code based off : https://github.com/lunarluvia/Brute-Force-Password-Cracker

# Define all characters to use in the password
chars = 'abcdefghijklmnopqurstuvwxyz'
rchars = 'zyxwvutsruqponmlkjihgfedcba'

# Define the password to be cracked
password = "abaaaa"

# Define the maximum password length to try
max_length = 6

# Track the start time of the password cracking process
start_time = time.time()

def passTask(char_string):
    # Try all possible combinations of characters up to max_length
    for length in range(6, max_length + 1):
        for combination in itertools.product(char_string, repeat=length):
            # Join the characters in the combination to form a password candidate
            candidate = "".join(combination)
            print("Trying password:", candidate)
            # Check if the candidate matches the password
            if candidate == password:
                # Track the end time of the password cracking process
                end_time = time.time()
                print("Password found:", candidate)
                # Calculate the time taken to crack the password
                time_taken = end_time - start_time
                print("Time taken:", time_taken, "seconds")
                # Terminate the password cracking process
                raise SystemExit

for combination in itertools.permutations(chars, r=6):
    candidate = "".join(combination)
    print("password:", candidate)

# pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
 
# pool.submit(passTask(rchars))
# pool.submit(passTask(rchars))

# The threading does not parallelize at all