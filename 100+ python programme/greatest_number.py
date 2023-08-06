#check which number is greatest amoung three entered number

num1 = eval(input("enter first number :"))
num2 = eval(input("enter first number :"))
num3 = eval(input("enter first number :"))

if (num1>num2) and (num1>num3):
    print(f'{num1} is greatest')

elif(num2>num1) and (num2>num3):
    print(f'{num2} is greatest')

elif (num3>num2) and (num3>num1):
    print(f'{num3} is greatest')

else:
    print("Enter again")

