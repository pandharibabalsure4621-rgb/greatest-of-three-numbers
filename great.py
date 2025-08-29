numbers=input("Enter three numbers a,b,c:")
a,b,c=numbers.split(",")
a=int(a)
b=int(b)
c=int(c)
if a>b and a>c:
    print("a is largest")
elif(b>a and b>c):
    print("b is largest")
else:
    print("c is largest")
    