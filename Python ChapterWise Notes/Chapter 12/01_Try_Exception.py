class Errorhandling:
    def error(self):
        while(True): 
            try: # try executes the conditon/logic statements before moving to exception part
                print("************************ \n")
                print("To quit please press (Q) \n")  
                number = input("Enter your number: ")
                if number == "Q":
                    break
                else:
                    number = int(number) 
                
                if number>10:
                    print("Number is greater than 10")
                else:
                    print("Number is smaller than 10")
            except Exception as k: # except function is expected with try statement. also except statement handles the error occurred in code and allows code to run without exiting
                print(f"Please enter Integer value, Error Mesage :-{k}")
        print("Thanks for playing")

        
E1 = Errorhandling()      
E1.error()