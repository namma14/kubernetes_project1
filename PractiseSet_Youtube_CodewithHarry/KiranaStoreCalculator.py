# write a prog to create kirana store calculcator.
# to add all of the amount entered by shopkeeper and calc total on click of enter
TotalAmount = 0
items_list = []
while (True):
    try:
        amount = input("Enter the amount of item: ")
        if amount.isnumeric():
            TotalAmount = int(amount)+TotalAmount
            items_list.append(amount)
            print("Total so far: ", TotalAmount)
        elif amount == 'Q':
            print("Thanks for using Calc")
            exit()
        else:
            print("Total Amount is: ", TotalAmount)
            break
    except ValueError:
        print("Enter valid value")

print("List of all items is: ")
for count,items in enumerate(items_list):
    print(count,items)