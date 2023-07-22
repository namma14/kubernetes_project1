# string1= "Hello Bro"
# # str1 = string1.split()
# # print(str1[0])
# if "Hello" in string1:
#     newstr = string1.replace ("Hello", "Hi")
#     print(newstr.strip())

def repl_strip(str1,word):
    if word in str1:
        newstr=str1.replace(word, "Nalle")
        return newstr
    else:
        print("Word not found")
string1 = input("Enter your string")
word1 = input("Enter you word")
newstr1 = repl_strip(string1, word1)
print (newstr1.strip())