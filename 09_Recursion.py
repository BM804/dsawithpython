#Print number n to number m:
def func(a,b):
    if a>b:
        return
    print(a)
    func(a+1,b)
func(int(input("Enter Start number:")),int(input("Enter end number:")))