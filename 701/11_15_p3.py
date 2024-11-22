import bcrypt

password = b'password!'
salt = bcrypt.gensalt()
print(salt)
hashed_pw = bcrypt.hashpw(password, salt)
print(hashed_pw)
password = b'Password!'
print(bcrypt.checkpw(password, hashed_pw))
