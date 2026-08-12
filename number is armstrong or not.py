#whethre a number is armstrong number

num=int(input("Enter numer:"))
temp=num
sum=0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not an armstrong number")
