# wirting a prog for lamda function
# sometimes we need to pass a function as an argument and lamda is used to do so
def func(a):
    a = a+5
    print(a)
func(10)

# defining lamda 
# syntax: lamda arguments: expressions

func = lambda a:a+5 # 'a' is the input and lamda function returns 'a+5' value
x = func(10)
print(x) 

# sqaure via lamda
sqr = lambda x:x*x
print(sqr(4))

# addition via lamda
sum = lambda a,b,c:a+b+c
print(sum(10,20,39))
