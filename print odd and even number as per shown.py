#print odd and even number as per shown

print("Odd No. between 1-100\tEven No. between 1-100")

for i in range(1,101):
    if i%2!=0:
        print(i,end="\t\t")

    if i+1 < 100:
        print(i+1)
       
