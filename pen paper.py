import tkinter as t
from random import randint as ri
x=ri(1,4)
if x==1:
    ci=["red","blue","green","blue","green","black","green"]
if x==2:
    ci=["blue","blue","red","blue","green","black","white"]
if x==3:
    ci=["red","blue","red","blue","red","black","yellow"]
if x==4:
    ci=["red","blue","red","blue","green","black","blue"]
    

f=t.Tk()
b1 = t.Button(f, bg='blue',activebackground=ci[0],width='50',height="20")
b1.place(x=50,y=80)
b2 = t.Button(f, bg='black',activebackground=ci[1],width='50',height="20")
b2.place(x=1200,y=80)
b3 = t.Button(f, bg='yellow',activebackground=ci[3],width='50',height="20")
b3.place(x=600,y=80)
b4 = t.Button(f, bg='red',activebackground=ci[4],width='50',height="20")
b4.place(x=50,y=600)
b5 = t.Button(f, bg='#54FA9B',width='50',height="20",activebackground=ci[5])
b5.place(x=1200,y=600)
b6 = t.Button(f, bg='#A877BA',activebackground=ci[6],width='50',height="20")
b6.place(x=600,y=600)
f.mainloop()