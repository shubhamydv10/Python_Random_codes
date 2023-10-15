#Conversion of Decimal number to binary using recursion

def convertBinary(n):
    if n > 1:
        convertBinary(n//2)
    print(n%2,end = "")

n = int(input("Enter the number for conversion : "))

print( "The binary of the given number is ")
convertBinary(n)
