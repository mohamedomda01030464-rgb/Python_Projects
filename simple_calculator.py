print("hellow this calculator ")
print(" choose 1 : + \n choose 2 : - \n choose 3 : * \n choose 4 : / ")
process = int(input("enter process number : "))
num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))
if process == 1:
    print("result : "+str(num1+num2))
elif process == 2:
    print("result : "+str(num1-num2))
elif process == 3:
    print("result : "+str(num1*num2))
elif process == 4:
    print("result : "+str(float(num1/num2)))
else:
    print("error")
