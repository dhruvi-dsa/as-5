#ATM system using while loop

balance=7000

while True:
    print("\n====== ATM =====")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")

    choice=int(input("Enter Choice:"))

    if choice == 1:
        print("Balance =",balance)
        
    elif choice == 2:
        amount=int(input("Enter your ammount:"))
        balance = balance + amount
        print("Money Deposited Successfully:")
        print("new balance =",balance)

    elif choice == 3:
        amount=int(input("Enter Withdrew ammount:"))
        balance = balance - amount
        print("Please Collect Your Money:")
        print("Reminder balance =",balance)

    elif choice == 4:
        print("Thank you for using ATM:")
        break

    else:
        print("Ivalid choice:")
    
