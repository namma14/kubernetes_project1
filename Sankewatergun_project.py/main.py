# Creating a snake water gun game project
# rule1: snake and water - snake wins as snake can drink water
# rule2: water and gun - water is winner as gun will drown in water
# rule3: gun and snake - gun is winner as gun can shoot snake

# player1 = input("Player1: Choose Snake (s) Water(w) or Gun(g)?: ")
# player2 = input("Player2: Choose Snake (s) Water(w) or Gun(g)?: ")

# def game():
#     if player1 == player2:
#         print("Its a tie")
#     if (player1 == "s"):
#         if player2=="w":
#             print("Player1 wins")
#         elif player2 == "g":
#             print("Player 2 wins")

#     if (player1 == "w"):
#         if player2 == "s":
#             print("player2 wins")
#         elif player2== "g":
#             print("Player1 wins")

#     if (player1 == "g"):
#         if player2 == "s":
#             print("Player1 wins")
#         elif player2 == "w":
#             print("Player 2 wins")
# game()

# 2nd Method to write prog for sanek,water and gun
import random # random fucntion returns a randow value everytime it is called by programm
randNo = random.randint (1,3)
if randNo==1:
    computer ="s"
elif randNo == 2:
    computer = "w"
elif randNo == 3:
    computer = "g"
print(f"Computer Input: {computer}")

player = input("Player: Choose from Snake(s), Water(w), Gun (g): ")

def game (computer,player):
    if computer == player:
        return None
    elif computer == "s":
        if player == "w":
            return False
        elif player == "g":
            return True
    elif computer == "w":
        if player == "g":
            return False
        elif player == "s":
            return True
    elif computer == "g":
        if player == "s":
            return False
        elif player == "w":
            return True

output = game(computer,player)
if output == None:
    print("It's a Tie")
elif output == True:
    print("You Win!!")
else:
    print ("You Loose!!")