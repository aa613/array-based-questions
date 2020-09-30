x=int(input("enter the no till where you want to sum the series"))
s=0
n=1
for a in range(x):
    s+=n**2
    n+=2
    print(s)