#number divisible by 13

#using for loop
print("The number divisible by 13 are : ")

for i in range(1,100):
    if i % 13 == 0:
        print(i)


#using lambda function

l = [39,48,26,95,33,67,87]

result = list(filter(lambda x : x%13 ==0 , l))
print("The number divisible by 13 are ",result)