# write a prog to check for spam messages based on keywords available in string/message
spamkeywords = ["make a lot of money", "buy now", "subscribe this", "clcik this"]
str1 = "if you want to get rich buy now our subscription"
if "buy now" in str1:
    print("Spam Message")
elif "make a lot of money" in str1:
    print("Spam Message")
elif "subscribe this" in str1:
    print("Spam Message")
elif "clcik this" in str1:
    print("Spam Message")
else:
    print("Not a spam")