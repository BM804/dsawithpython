# Recursion using parameters..
def func(a,b):
    if b==0:
        return
    print(a)
    func(a,b-1)
func(int(input("enter the number: ")),int(input("How many times: ")))