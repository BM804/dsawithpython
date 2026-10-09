# Checking a number is palindrome or not !!
a = int(input("Enter a number ::"))
num = a
b = 0
while num > 0 :
    temp = num % 10
    b = b * 10  + temp
    num = num//10
if a == b:
    print("palinrome..!!")
else:
    print("Not Palindrome")