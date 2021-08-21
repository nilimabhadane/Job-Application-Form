from tkinter import *
from tkinter import ttk
import sqlite3 as db

conn=db.connect("mydb.db")
cur=conn.cursor()
cur.execute('''create table if not exists data
(name varchar(10),age varchar(10),gender varchar(20),phno varchar(60),tk varchar(20),eq varchar(30),location varchar(20))''')
cur.close()
conn.commit()
conn.close()

def put():
    conn=db.connect("mydb.db")
    cur=conn.cursor()
    cur.execute("insert into data values('%s','%s','%s','%s','%s','%s','%s')"%(name.get(),age.get(),m.get(),phno.get(),tk.get(),eq.get(),location.get()))
    cur.close()
    conn.commit()
    conn.close()
    status.set('Registration successfuly....!!')

def mmm():
    a=gender.get()

    if(a==1):
        m.set("male")
    else:
        m.set("female")

def ccc():
    if CheckVar1.get()==1 and CheckVar2.get()==1:
        tk.set("Java and DotNet")
    elif CheckVar1.get()==1 and CheckVar2.get()==0:
        tk.set("Java")
    else:
        tk.set("DotNet")

            
            
        
top = Tk()
top.title("Job Application Form")
top.configure(background="Black")


name=StringVar()
age=StringVar()
gender=IntVar()
phno=StringVar()
m=StringVar()
tk=StringVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
eq=StringVar()
location=StringVar()
status=StringVar()


L1 = Label(top, text = "Name", bg="Black" , fg="white" , font="times 14").place(x=10,y=30)
E1 = Entry(top,width=30,bd =3,textvariable=name).place(x=300,y=30)

L2= Label(top, text = "Age",  bg="Black" , fg="white" , font="times 14").place(x=10,y=90)
E2 = Entry(top,width=30,bd =3,textvariable=age).place(x=300,y=90)


L3= Label(top, text = "Gender" , bg="Black" , fg="white" , font="times 14").place(x=10,y=150)

R1 = Radiobutton(top, text="Male", value=1,variable=gender,command=mmm,bg="black" , fg="blue" , font="times 14").place(x=300,y=150)

R2 = Radiobutton(top, text="female", value=2,variable=gender,command=mmm,bg="black" , fg="blue" , font="times 14").place(x=400,y=150)

L4= Label(top, text = "Phone Number", bg="Black" , fg="white" , font="times 14").place(x=10,y=210)
E4 = Entry(top,width=30,bd =3,textvariable=phno).place(x=300,y=210)


L5= Label(top, text = "Technologies Knows", bg="Black" , fg="white" , font="times 14").place(x=10,y=270)

C1 = Checkbutton(top, text = "Java", variable =CheckVar1, \
                 onvalue = 1, offvalue = 0,command=ccc,bg="Black" , fg="blue" , font="times 14").place(x=300,y=270)

C2 = Checkbutton(top, text = "DotNet",variable =CheckVar2, \
                 onvalue = 1, offvalue = 0,command=ccc,bg="Black" , fg="blue" , font="times 14").place(x=400,y=270)



L6= Label(top, text = "Educational Qualification", bg="Black" , fg="white" , font="times 14").place(x=10,y=400)
 
def click():
    action.configure(text="chosen color is : "+ numberChosen.get())

    action = ttk.Button(top, text="Click", command=click)
    action.grid(column=1,row=1)

numberChosen= ttk.Combobox(top, width=28, textvariable=eq)
numberChosen['values']=("Engineering","MCA","MBA","Graduation","MTECH","Mphil","Phd")
numberChosen.grid(column=0,row=1)
numberChosen.current()  
numberChosen.place(x=300,y=400)



L7= Label(top, text = "Location", bg="Black" , fg="white" , font="times 14").place(x=10,y=520)  
 
def click():
    action.configure(text="chosen color is : "+ numberChosen.get())

    action = ttk.Button(top, text="Click", command=click)
    action.grid(column=1,row=1)

numberChosen= ttk.Combobox(top, width=28, textvariable=location)
numberChosen['values']=("Dhule","Mumbai","Pune","Chennai","Delhi","Hyderabad")
numberChosen.grid(column=0,row=1)
numberChosen.current()  
numberChosen.place(x=300,y=520)

L8= Label(top, text = "",textvariable=status, bg="Black" , fg="blue" , font="times 14").place(x=100,y=650)  


frame = Frame(top).place(x=200,y=210)
b1= Button(frame, text="Submit",command=put,bg="white" , fg="blue" , font="times 14",width=20).place(x=100,y=600)



top.mainloop()
