'''Writing a prog to secure an exiting password 
replacing password alphbets with a set of characters.'''

secure = (('I','|'),('i','1'),('a','@'),('s','$'))

def securepassword(password):
    for a,b in secure:
        password=password.replace(a,b)
    return password

if __name__=="__main__":
    password = input("Enter Password: ")
    sp=securepassword(password)
    print(sp)

