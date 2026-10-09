# 03_DSA_Factors_of_a_number optimal soluton
from math import sqrt
a = int(input("Enter the Number ::"))
num1 =a
factors =[]
for i in range(1,int(sqrt(num1))+1):
    if num1%i ==0:
        factors.append(i)
        if num1//i != i:
            factors.append(num1//i)
factors.sort()
print(factors)
