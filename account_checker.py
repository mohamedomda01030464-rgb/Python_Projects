
username = "1234@gmail.com"
password = "1234"
name = input("write your name : ").strip()
u = input("write username : ").strip().lower()
p = input("write password : ").strip()
if u == username and p == password:
    print("welcome, "+name)
elif u != username and p == password:
    print("username is wrong, "+name)
elif u == username and p != password:
    print("password is wrong, "+name)
else :
    print("username and password is wrong, "+name)
    
