#Genrate character and corresponding ASCII values in decimal,binay,hexa and octal table from 0-255

print("Char\tDecimal\tBinary\tHex\tOctal")

for i in range(256):
    print(chr(i),"\t",i,"\t",bin(i),"\t",hex(i),"\t",oct(i))
