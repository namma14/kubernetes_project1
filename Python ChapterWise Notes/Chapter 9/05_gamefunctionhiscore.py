def game():
    return 56

file = open('hello.txt','r')
# file.write (54)
readf = int(file.read())
# print(readf)


score = game()
# print(score)

if (readf <= score):
    with open('hello.txt','w') as f1:
        d=f1.write(str(score))
        print(d)
else:
    print(f"File has highest score {readf}")