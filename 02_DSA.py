# Armstrom number or not 
num1 = int(input("Enter a number>>!"))
num = num1
res= 0
while num > 0:
    temp = num % 10
    res = res + temp**len(str(num1))
    num = num//10
if num1==res:
    print("Yes,it is Palindrome..")
else:
    print("Not Palindrome.")