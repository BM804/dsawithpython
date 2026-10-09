numa =[5, 6, 7, 7, 1, 9, 1, 1, 5, 1, 1] 
dict ={}
for i in range(0,len(numa)):
    if numa[i] in dict:
        dict[numa[i]] += 1
    else:
        dict[numa[i]] = 1
print(dict) 