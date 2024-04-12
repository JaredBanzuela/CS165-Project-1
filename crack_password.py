import itertools
import string
from passlib.hash import md5_crypt
import multiprocessing


def passwrd_finder(first_letter, hash, salt, event):
    chars = 'abcdefghijklmnopqurstuvwxyz'
    max_length = 1

    for combination in itertools.product(chars, repeat=max_length - 1):        
        candidate = first_letter + "".join(combination)
        hashed_password = md5_crypt.using(salt=salt).hash(candidate)
        # print(f"Process for starting letter '{first_letter}' trying password:", candidate)
        if hashed_password == hash:
            event.set()
            print(f"Password found by process for starting letter '{first_letter}':", candidate)
            return candidate

if __name__ == "__main__":
    salt = "w2wGV6Vn"
    hash = "$1$w2wGV6Vn$Kw7FW.cpnlAQSpSpF25Xo/"
    end_event = multiprocessing.Event()
    first_letters = string.ascii_lowercase
    
    processes = []
    for first_letter in first_letters:
        process = multiprocessing.Process(target=passwrd_finder, args=(first_letter, hash, salt, end_event))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes finished.")
    salt = "hfT7jp2q"
    candidate = "czormg"
    hashed_password = md5_crypt.using(salt=salt).hash(candidate)
    print(hashed_password)