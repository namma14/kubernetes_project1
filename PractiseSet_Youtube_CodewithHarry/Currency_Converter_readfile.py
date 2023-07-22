with open("PractiseSet_Youtube_CodewithHarry/currency_convertor.txt") as f:
    txtfile=f.readlines()
# print(txtfile)
currency_data = {}
for lines in txtfile:
    x=lines.split("\t")
    currency_data[x[0]] = x[1]
print(currency_data)

amount = int(input("Enter the amount you want to exchange from INR to Foriegn currency: "))
[print(i) for i in currency_data.keys()]
currency = input("Choose currency from options provided above: ")
# print(currency_data.keys())
# if currency in currency_data:
converted_amount = amount * float(currency_data[currency])

ForeignAmount= int(input("Enter the amount you want to exchange from Foriegn currency to INR: "))
Foriegncurrency = input("Enter Your currency: ")
[print(i) for i in currency_data.keys()]
ForiegnConverted_Amount = ForeignAmount * int(1/currency_data[currency])


print(f"The amount {amount} converted from INR to {currency} and converted amount is {converted_amount} {currency}")


