from tkinter import *
from math import *
def lahenda():
    if (a.get()!=""and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b*-4*a_*c
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
        else:
            t="нету корней"
            vastus.configure(text=f"D={D}\{t}")
            a.configure(bg="lightblue")
            b.configure(bg="lightblue")
            c.configure(bg="lightblue")
    else:
        if a.get()=="": a.configure(bg="red")
        if b.get()=="": a.configure(bg="red")
        if c.get()=="": a.configure(bg="red")
aken=Tk()
aken.geometry("600x200")
aken.title("квадратные уравнения")
lbl=Label(aken,text="Решение квадратного уравнения",font="calibri 25",fg="white",bg="black")
lbl.pack()
vastus=Label(aken,text="решение",height=4,width=60,bg="gray")
vastus.pack(side=BOTTOM)
a=Entry(aken,font="calibri 26",fg="green",bg="lightblue",width=3)
a.pack(side=LEFT)
x2=Label(aken,text="x**2+",font="calibri 26", fg="green", padx=10)
x2.pack(side=LEFT)  

b=Entry(aken,font="calibri 26",fg="green",bg="lightblue",width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="calibri 26", fg="green", padx=10)
x.pack(side=LEFT)
c=Entry(aken,font="calibri 26",fg="green",bg="lightblue",width=3)
c.pack(side=LEFT)
y=Label(aken,text="=0",font="calibri 26", fg="green", padx=10)
y.pack(side=LEFT)
btn=Button(aken,text="решить", font="calibri 26",bg="green",command=lahenda)
btn.pack(side=LEFT)




aken.mainloop()