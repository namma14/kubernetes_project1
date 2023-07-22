def num():
    try:
     n = int(input("Enter Number: "))
     n = n+1
     print(n)
    except Exception as e:
     print(e)
print(__name__) # value of __name__ in the same prog is __main__ which signifies that it is being called from same prog
'''but when printing the value of __name__ in the different program, where this
program is called then value is name of this prog i.e p06_try_main'''
'''__name__ module is used to check whether module is run directly or imported to another file based on value of __name__'''
if __name__ == "__main__": # __name__ is useful when we are calling/importing function from another python and we don't want to execute the fucntions twice
    num()
