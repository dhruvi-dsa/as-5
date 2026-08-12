#keep asking the user for a password until it is correct

correct_password = "dhruvi2812"

while True:
    password=input("Enter password:")

    if password == correct_password:
        print("correct password")
        break
    else:
        print("Wrong password,please try again")
