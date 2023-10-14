#Making a simple calculator

print(">>>>>>>>>>>>>>MINI CALCULATOR<<<<<<<<<<<<<<<\n")

num1 = eval(input("Enter first number : "))
num2 = eval(input("Enter second number : "))

print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division ")

choice = int(input("Enter your choice from 1 to 4 : "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
else:
    print(num1/num2)

print("Thank You")


