x=float(input("enter the e^x x's value"))
n=int(input("enter the level of accuracy"))
e=1
z=1
if n==1:
    print(1)
else:
    for a in range(n-1):
        e+=(x**z)/z
        z+=1
        print(e)
    