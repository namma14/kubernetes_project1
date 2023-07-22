# creating a game to make a perfect guess
import random
class PerfectGuess:
    global nofguess
    nofguess = 0
    def generatenum(self,n):
            global nofguess
            nofguess = 0
            num =random.randint(1,n)
            print(num)
            number = None
            while (number != num):  
                number = int(input("Make your Guess: "))
                if num<number:
                    print("Try Again,Pick a Lower Number")
                elif num>number:
                    print("Try Again,Pick a Higher number")
                else:
                    print("Congratulations !! Perfect Guess")
                nofguess += 1
            print("Total No of Guess",nofguess)
            return nofguess
 
pg = PerfectGuess()
pg.generatenum(50)

with open("hiscore.txt", "r") as f:
         hiscore = f.read()
         print("Hi-Score from file is",hiscore)

with open("hiscore.txt", "w") as f:
         if hiscore > str(nofguess):
              f.write(str(nofguess))


                