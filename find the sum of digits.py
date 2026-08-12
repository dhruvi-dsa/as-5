#find the sum of digits

num=int(input("Enter number:"))

sum=0
while num>0:
 digit = num % 10
 sum = sum + digit
 num = num // 10

 print("sum of digits =",sum)
