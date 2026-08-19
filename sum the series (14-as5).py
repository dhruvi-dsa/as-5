# sum the series

n=int(input("Enter n:"))

sum=0

for i in range(1,n+1):
    if i < n:
        print(f"{i}^2/{i}",end=" + ")
    else:
        print(f"{i}^2/{i}")

    sum = sum + (i**2)/i

    print("Sum =",sum)
