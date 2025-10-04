import random
print("welcome to guess game")
player = int(input("guess number from 1 to 10 : "))
option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computer = random.choice(option)
print("choice computer is : "+str(computer))
if computer > player :
    print("the number is greater than your choice")
elif computer < player :
    print("the number is less than your choice")
else :
    print("your guess is correct")