
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number:"))

M = max(a,b)

while(True):
    if(M%a==0 and M%b==0):
        break
    M = M+1
print(f"The LCM of {a} and {b} is {M}")