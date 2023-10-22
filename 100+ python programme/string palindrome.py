#Check string is palindrome or not

a = input("Enter a word here : ")

rev = a[::-1]
if a == rev:
    print("It is plaindrome")
else:
    print("Is is not a palindrome")