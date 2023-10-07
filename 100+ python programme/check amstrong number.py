#check amstrong number

num = int(input("Enter a number : "))

sum = 0
temp = num

while temp > 0:
    digit = temp%10
    cube = digit ** 3
    sum = sum + cube
    temp //=10

if num == sum :
    print("The entered number is amstrong number")
else:
    print("The entered number is not amstrong number")
