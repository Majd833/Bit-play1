def setornot(number,n):
    if number&(1<<(n-1)):
        print("SET")
    else:
        print("NOT")
number=int(input("Enter the number"))
n=int(input("Enter bit number:"))
setornot(number,n)