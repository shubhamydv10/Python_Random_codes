#factorial using recursion

def fact(a):
    if a ==0:
        return 1
    else:
        return ((a)*fact(a-1))

a =int(input("Enter a number : "))
if a<= 0:
    print("Factorial of number less than 1 does not exists")
else:
    print("Factorial of given number is",fact(a))
