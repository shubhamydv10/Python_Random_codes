#print multiplication table of any number

n = eval(input("Enter a number : "))
for i in range (1,11):
    print(f'{n} x {i} = {n*i}')