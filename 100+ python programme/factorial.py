#factorial using for loop

num = int(input("Enter a number : "))
fct = 1
if num < 0:
    print("The factorial of 0 does not exist")
if num == 0:
    print("The factorial of 0 is ", 1)

if num > 0:
    for i in range (1,num+1):
        fct = fct * i
print(f'The factorial of the entered number is {fct}')