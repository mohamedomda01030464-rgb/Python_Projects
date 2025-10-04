print("welcome to resturant system ")
name = input("please write your name : ")
print("hello ", name)
print("this is resturant menu : ")
print("""
1- Burger 🍔 - 50 LE
2- Pizza 🍕 - 70 LE
3- Fries 🍟 - 20 LE
4- Cola 🥤 - 15 LE
5- Water 💧 - 10 LE
""")
x = int(input("choose from menu : "))
if x == 1 :
    print("your order is Burger 🍔 - 50 LE")
elif x == 2 : 
    print("your order is Pizza 🍕 - 70 LE")
elif x == 3 : 
    print("your order is Fries 🍟 - 20 LE")
elif x == 4 : 
    print("your order is Cola 🥤 - 15 LE")
elif x == 5 : 
    print("your order is Water 💧 - 10 LE")
else :
    print("error")