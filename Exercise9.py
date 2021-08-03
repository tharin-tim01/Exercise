ID = input("ID: ")
Password = input("Password: ")
product_list = []
while True:
    if ID == "admin" and Password == "1234":
        print("Hello Customer, Welcome to my shop")
        print("----Item list----")
        print("1.egg 10 baht per unit")
        print("2.Chicken breast 299 baht per unit")
        print("3.pork 399 baht per unit")
        print("4.meat 200 baht per unit")
        print("5.calculate total")
        Product = int(input("Please choose the item you want by type product number: "))
        if Product == 1:
            Quantity = int(input("How much do you want: "))
            price = 10
            total = price * Quantity
            product_list.append(total)
        elif Product == 2:
            Quantity = int(input("How much do you want: "))
            price = 299
            total = price * Quantity
            product_list.append(total)
        elif Product == 3:
            Quantity = int(input("How much do you want: "))
            price = 399
            total = price * Quantity
            product_list.append(total)
        elif Product == 4:
            Quantity = int(input("How much do you want: "))
            price = 200
            total = price * Quantity
            product_list.append(total)
        elif Product == 5:
            total = 0
            for x in product_list:
                total += x
            print ("your total:",total)
            break
        else:
            print ("Wrong username and password")