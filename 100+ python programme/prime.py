#check prime number

n = int(input("enter a number : "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("the number is not prime")
            break

    else:
        print("the number is prime")
else:
    print("Enter positive number")