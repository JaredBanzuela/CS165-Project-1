import itertools
import string
from passlib.hash import md5_crypt
import multiprocessing
from multiprocessing import Pool

chars = 'zyxwvutsrqponmlkjihgfedcba'
max_length = 6

def passwrd_finder(first_letter, hash, salt, event):
    try:
        tmp = md5_crypt.using(salt=salt)
        for combination in itertools.product(chars, repeat=max_length - 1):        
            candidate = first_letter + "".join(combination)
            hashed_password = tmp.hash(candidate)
            # print(f"Process for starting letter '{first_letter}' trying password:", candidate)
            if hashed_password == hash:
                event.set()
                print(f"Password found by process for starting letter '{first_letter}': " + candidate)
                return candidate
            if candidate == first_letter + "uuuuu":
                print(f"Process '{first_letter}' is 1/4 done.")
            if candidate == first_letter + "ggggg":
                print(f"Process '{first_letter}' is 3/4 done.")
            if candidate == first_letter + "ppppp":
                print(f"Process '{first_letter}' is 1/2 done.")
            if candidate == first_letter + "aaaaa":
                print(f"Process '{first_letter}' is done.")
    except KeyboardInterrupt:
        print(f"\nLast checked password for starting letter '{first_letter}': " + candidate + "\n")
    except SystemError:
        print(f"\nLast checked password for starting letter '{first_letter}': " + candidate + "\n")
    except SystemExit:
        print(f"\nLast checked password for starting letter '{first_letter}': " + candidate + "\n")


if __name__ == "__main__":
    salt = "w2wGV6Vn"
    hash = "$1$w2wGV6Vn$Kw7FW.cpnlAQSpSpF25Xo/"
    end_event = multiprocessing.Event()
    first_letters = string.ascii_lowercase
    # first_letters = 'abcdefghijklmnopqrstuvwx'
    
    processes = []
    for first_letter in first_letters:
        process = multiprocessing.Process(target=passwrd_finder, args=(first_letter, hash, salt, end_event))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes finished.")