#Sum of Natural numbers from 1 to 10
sum =0
def func(sum,a,b):
    if a > b:
        print(sum)
        return
    
    func(sum+a,a+1,b)
func(sum,1,3)