ID = input("ID: ")
Password = input("Password: ")
if ID == "admin" and Password == "1234":
    print("Hello Customer, Welcome to my shop")
    print("----Item list----")
    print("1.egg 10 baht per unit")
    print("2.Chicken breast 299 baht per unit")
    print("3.pork 399 baht per unit")
    print("4.meat 200 baht per unit")
    Product = int(input("Please choose the item you want by type product number: "))
    Quantity = int(input("How much do you want: "))
    if Product == 1:
        price = 10
        total = price * Quantity
        print (total)
    elif Product == 2:
        price = 299
        total = price * Quantity
        print (total)
    elif Product == 3:
        price = 399
        total = price * Quantity
        print (total)
    elif Product == 4:
        price = 200
        total = price * Quantity
        print (total)
else:
    print ("Wrong username and password")

