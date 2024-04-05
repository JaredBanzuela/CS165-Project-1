from passlib.hash import md5_crypt

salt = "hfT7jp2q"
password = "zhgnnd"

hashed_password = md5_crypt.using(salt=salt).hash(password)
full_hash = "$1$hfT7jp2q$wPwz7GC6xLt9eQZ9eJkaq."

if (full_hash == hashed_password):
    print("match")
    print(full_hash + "\n" + hashed_password + "\n")
else:
    print("mismatch\n")
    print(full_hash + "\n" + hashed_password + "\n")