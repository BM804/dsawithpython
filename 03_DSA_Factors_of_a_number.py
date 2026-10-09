# 03_DSA_Factors_of_a_number
num1 = int(input("Enter the number ::"))
result = []
for i in range(1,num1//2+1):
    if num1 % i ==0:
        result.append(i)
result.append(num1)
print(f'Factors of {num1} are {result}')