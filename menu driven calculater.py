#Menu-driven calculater using a while loop

import sys
while True:
    print("\n....CALCULATER MENU....")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice=int(input("Enter choice:"))

    match choice:
     case 1:
         a=int(input("Enter first number:"))
         b=int(input("Enter second number:"))

         print("Result =",a+b)

     case 2:
         a=int(input("Enter first number:"))
         b=int(input("Enter second number:"))

         print("Result =",a-b)

     case 3:
         a=int(input("Enter first number:"))
         b=int(input("Enter second number:"))
         
         print("Result =",a*b)

     case 4:
         a=int(input("Enter first number:"))
         b=int(input("Enter second number:"))

         print("Result =",a/b)

     case 5:
         print("Thank You!")
         break

     case _:
         print("Invalid choice")
         
