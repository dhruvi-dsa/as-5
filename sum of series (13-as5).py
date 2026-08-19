# sum the series

n=int(input("Enter n:"))

sum=0
for i in range(1,n+1):
   print(i,"/",i+1, end=" + ")
   sum = sum + i/(i+1)

   print("/nSum =",sum)
