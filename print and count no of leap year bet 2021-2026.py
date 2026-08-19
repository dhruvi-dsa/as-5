#print and count no of leap year bet 2021-2026

count=0

for year in range(2021,2027):
    if year % 400 == 0 or(year % 4 == 0 and year % 100!=0):
        print(year)
        count=count+1

    print("Number of leap year =",count)

