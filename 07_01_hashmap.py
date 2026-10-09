n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]

m = [10, 11, 1, 9, 5, 67, 2]

hash_map = [0] *11
for num in n :
    hash_map[num] +=1

print(hash_map)

for num2 in m :
    if num2 < 1 or num2 >10:
        print(0)
    else:
        print(hash_map[num2]) 
