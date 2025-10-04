num1 = float(input("enter first number : "))
opperation = input("enter symbol opperation : ")
num2 = float(input("enter second number : "))
if opperation == "+":
    print(num1+num2)
elif opperation == "-":
    print(num1-num2)
elif opperation == "*":
    print(num1*num2)
elif opperation == "/":
    print(num1/num2)
elif opperation == "^":
    print(num1**num2)
else :
    print("error")
