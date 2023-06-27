import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;':,./<>?"

while True:
    try:
        length = int(input("Type the length of the password: "))
        qty = int(input("Type the quantity of passwords: "))
    except ValueError:
        print("Invalid value, try again.")
    else:
        for x in range(0, qty):
            Passwd = ""
            for x in range(0, length):
                passchar = random.choice(char)
                Passwd += passchar
            print(f"Password: {Passwd}")
        break
