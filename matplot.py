import math as m

import matplotlib.pyplot as plt
a=[]
b=[]
x=-20
xa=[]
while x<20:
    y=m.sin(x)
    a=a+[x]
    b=b+[y]
    xa+=[0]
    x+=0.01
    
plt.plot(a,b)
plt.plot(a,xa)
plt.show()
x=input('enter to exit')