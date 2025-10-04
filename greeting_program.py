print("welcome to greeting programe")
time = int(input("write the hour : "))
if time < 0 or time > 23 :
    print("error")
elif time <= 10 :
    print("صباح الخير ")
elif time <= 17 :
    print("مساء الخير")
elif time <= 23 :
    print("مساء سعيد")
