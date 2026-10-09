nums=[5, 6, 7, 7, 1, 9, 1, 1, 5, 1, 1]
n = len(nums)
hash_map ={}
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)