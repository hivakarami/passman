import hashlib
import getpass
import string
import random

password_manage = {}


def generate_pass():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(20))
    return password

def create_acount():
    #print("debugging")
    username = input("Enter username: ")
    while(username in password_manage):
        username = input("userneme already exists, choose another username: ")

    while(True):
        x = input("if you want a strong password suggestion inter 1 otherwisr inter 2: ")
        if(x == '2'):
            while(True):
                password = getpass.getpass("Enter pasword: ")
                if(len(password) < 8):
                    print("password must contain at least 8 characters, try again")
                else:
                    break    
            break
        elif(x == '1'):
            password = generate_pass()
            print("your password is: " + password)
            break
        else:
            print("invalid input, try again")    

    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    password_manage[username] = hash_pass

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter pasword: ")
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    if(username in password_manage and password_manage[username] == hash_pass):
        print("Login successful!")
    else:        
        print("wronge usernamr or password")    

def main():
    x = '1'
    while(x == '1' or x == '2'):
        x = input("inter 1 to login, 2 to create an acount, and 0 to exist: ")
        if(x == '2'):
            #print("debugging")
            create_acount()
        elif(x == '1'):
            login()

if(__name__ == "__main__"):
    main()