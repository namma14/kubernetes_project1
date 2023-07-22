# print no from 1-20 which are not divisible by 3 or 5
#x=1
#while x<=20:
#    if x%3 != 0 or x%5!=0:
#       print(x)
#    x+=1
i=1
a=1
while i<=20:
    if ((a%3 == 0) and (a%5 == 0)) :
        a=a+1
    else:
        print(a)
        a=a+1
    i=i+1

#for i in range(1,20):
#    if i%3==0 and i%5==0:
#        continue
#    print(i)
#    i+=1