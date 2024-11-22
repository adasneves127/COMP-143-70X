import bcrypt

salt = bcrypt.gensalt()
print(salt)
password = b"password!"
hashed_pw = bcrypt.hashpw(password, salt)
print(hashed_pw)
password = b"Password!"
print(bcrypt.checkpw(password, hashed_pw))