print("                                   welcome to check email and password                                   ")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
email = input("*************enter your email : ")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
password = input("*************enter your password : ")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
if email == "mohamedomda@gmail.com" and password == "mamaaw01030464@@":
    print("                                   welcome                                   ")
elif email == "mohamedomda@gmail.com" and password != "mamaaw01030464@@":
    print("                                   password is invalid                                   ")
elif email != "mohamedomda@gmail.com" and password == "mamaaw01030464@@":
    print("                                   email is invalid                                   ")
else :
    print("                                   email and password is invalid                                   ")