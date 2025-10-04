import random
print("welcome to rock, paper, scissors game ")
player =input("choose : rock or paper or scissors : ")
options = ["rock", "paper", "scissors"]
computer = random.choice(options)
print("computer choose, "+computer)
if computer == player :
    print("play again")
elif player == "rock":
    if computer == "paper":
        print("lose")
    elif computer == "scissors":
        print("win")
elif player == "paper":
    if computer == "rock":
        print("win")
    elif computer == "scissors":
        print("lose")
elif player == "scissors":
    if computer == "rock":
        print("lose")
    elif computer == "paper":
        print("win")
else :
    print("invalid")