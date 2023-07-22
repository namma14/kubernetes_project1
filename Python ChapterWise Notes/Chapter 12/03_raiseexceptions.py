#writing a prog to riase a error exception
def incnumber(number):
        try:
         return int(number)+1
        except:
            raise ValueError("Enter Integer value")

a = incnumber('sad')
print(a)