# progaram to display user entered name followed by Good Afternoon!
# name= input("Enter your Name:")
# print(name,',', "Good AfterNoon!")

Name= input("Enter complainent's Name: \n",)
Date= input("Enter current date: \n")
letter = '''Dear name,
you are selected !
Date:date'''
letter = letter.replace("name" ,Name)
letter = letter.replace("date", Date)
print(letter)