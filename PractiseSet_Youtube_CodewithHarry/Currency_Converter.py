# write a prog for currency converter.
# Rs to dollor 1rs = 0.012 $ and Dollor to Rs, 1$ = 82.39
class CurrencyConverter: 
    global dollar     
    def dollarConverter(self):
        global dollar
        self.dollar = int(input("Enter the dollar amount you want to convert : "))
        rupees = self.dollar * 82.39
        print(f"The converted amount in rupees for {self.dollar}$ is {rupees}")
        return rupees
    def poundConverter():
        global pound
        pound = int(input("Enter the pounds you want to convert : "))
        return pound * 106.04
    def yenConverter():
        global yen
        yen = int(input("Enter the yens you want to convert : "))
        return yen * 0.59
    def euroConverter():
        global euro
        euro = int(input("Enter the euros you want to convert : "))
        return euro * 90.69
    def singaporedollarConverter():
        global sgd
        sgd = int(input("Enter the sgds you want to convert : "))
        return sgd * 61.40
cc =CurrencyConverter()

while (True):
        
        Welcome_Message = '''******* Welcome to Currency Converter*******
                                    1. Dollar
                                    2. Pound
                                    3. Yen
                                    4. Euro
                                    5. Signapore Dollar
                                    6. Exit'''
        print(Welcome_Message)
        choice = int(input("Pick your option: "))
        if choice ==1:
            cc.dollarConverter()
        elif choice == 6:
            print("Thanks for using Currency Converter !!")
            exit()


