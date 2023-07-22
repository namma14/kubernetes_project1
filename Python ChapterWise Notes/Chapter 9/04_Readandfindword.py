file = open('this.txt','r')
output = file.read()
print(output)
if "twinkle" in output:
    print("twinkle is available in file this.txt")
else:
    print("Twinkle not available")
file.close