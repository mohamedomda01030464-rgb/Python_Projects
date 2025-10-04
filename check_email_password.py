print("                                   welcome to check email and password                                   ")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
email = input("*************enter your email : ")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
password = input("*************enter your password : ")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
if email == "1234@gmail.com" and password == "1234":
    print("                                   welcome                                   ")
elif email == "1234@gmail.com" and password != "1234":
    print("                                   password is invalid                                   ")
elif email != "1234@gmail.com" and password == "1234":
    print("                                   email is invalid                                   ")
else :

    print("                                   email and password is invalid                                   ")
