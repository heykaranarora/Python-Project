from tkinter import *
from tkinter import ttk

root=Tk()
e=Entry(root, width=50)
e.pack()

def myClick():
    myLabel= Label(root, text="Hello "+ e.get())
    myLabel.pack()

myButton= Button(root, text="Enter Your Name",command=myClick)
myButton.pack()

root.mainloop()
screen_root= Tk()
screen_root.title("Challenge Vs Challenge!!!")


screen_label= Label(screen_root, text="Challenge Vs Challenge!!!", font=('Helvetica',18))
screen_label.pack(pady=20)

def main_window():
    root=Tk()
    root.title('Challenge Vs Challenge', font=('Helvetica',120))

y=0
a=ttk.Notebook()
frame1=ttk.Frame(a)
frame2=ttk.Frame(a)
frame3=ttk.Frame(a)
frame4=ttk.Frame(a)
frame5=ttk.Frame(a)
frame6=ttk.Frame(a)
frame7=ttk.Frame(a)
frame8=ttk.Frame(a)
frame9=ttk.Frame(a)
frame10=ttk.Frame(a)

root=ttk.Frame(a)

def quiz(y):
    a.add(frame1, text="Q1")
    a.add(frame2, text="Q2")
    a.add(frame3, text="Q3")
    a.add(frame4, text="Q4")
    a.add(frame5, text="Q5")
    a.add(frame6, text="Q6")
    a.add(frame7, text="Q7")
    a.add(frame8, text="Q8")
    a.add(frame9, text="Q9")
    a.add(frame10, text="Q10")

    Label(frame1 , text="Total keywords in Python?",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame1, text="33" ,font=("Arial",30,"bold"),bg="light blue",command=a1_right).grid(row=3 ,column=1)
    Button(frame1, text="31" ,font=("Arial",30,"bold"),bg ="light green",command=a1_wrong).grid(row=3, column=2)
    Button(frame1, text="30" ,font = ("Arial", 30,"bold"),bg = "light green",command=a1_wrong).grid(row=3, column=3)

    Label(frame2, text="Output of 2**3?" ,font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame2, text="6", font=("Arial",30,"bold"),bg="light blue",command=a2_wrong).grid(row=3 ,column=1)
    Button(frame2, text="8", font=("Arial", 30, "bold"), bg="light green",command=a2_right).grid(row=3, column=2)
    Button(frame2, text="9", font=("Arial", 30, "bold"), bg="light pink",command=a2_wrong).grid(row=3, column=3)

    Label(frame3, text="Output of np.arrange(1,5)?", font=("Arial", 50, "bold")).grid(row=2, column=2)
    Button(frame3, text="[1,2,3,4]", font=("Arial", 30, "bold"), bg="light blue",command=a3_right).grid(row=3, column=1)
    Button(frame3, text="[0,1,2,3,4]", font=("Arial", 30, "bold"), bg="light green",command=a3_wrong).grid(row=3, column=2)
    Button(frame3, text="[1,2,3,4,5]", font=("Arial", 30, "bold"), bg="light pink",command=a3_wrong).grid(row=3, column=3)

    Label(frame4, text="keyword use to declare a function?", font=("Arial", 50, "bold")).grid(row=2, column=2)
    Button(frame4, text="define", font=("Arial", 30, "bold"), bg="light blue",command=a4_wrong).grid(row=3, column=1)
    Button(frame4, text="def", font=("Arial", 30, "bold"), bg="light green",command=a4_right).grid(row=3, column=2)
    Button(frame4, text="None", font=("Arial", 30, "bold"), bg="light pink",command=a4_wrong).grid(row=3, column=3)

    Label(frame5, text="Output of 2*12?", font=("Arial", 50, "bold")).grid(row=2, column=2)
    Button(frame5, text="24", font=("Arial", 30, "bold"), bg="light blue",command=a5_right).grid(row=3, column=1)
    Button(frame5, text="28", font=("Arial", 30, "bold"), bg="light green",command=a5_wrong).grid(row=3, column=2)
    Button(frame5, text="32", font=("Arial", 30, "bold"), bg="light pink",command=a5_wrong).grid(row=3, column=3)

    Label(frame6, text="Who developed Python Programming", font=("Arial", 50, "bold")).grid(row=1, column=1)
    Button(frame6, text="Rasmus Lerdof", font=("Arial", 30, "bold"), bg="light green", command=a6_wrong).grid(row=3, column=1)
    Button(frame6, text="Guido Van Rossum", font=("Arial", 30, "bold"), bg="light pink", command=a6_right).grid(row=7, column=1)


    Label(frame7, text="keywords in python are ", font=("Arial", 50, "bold")).grid(row=1, column=1)
    Button(frame7, text="Capatilized", font=("Arial", 30, "bold"), bg="light blue", command=a7_wrong).grid(row=3, column=1)
    Button(frame7, text="Lower Case", font=("Arial", 30, "bold"), bg="light green", command=a7_wrong).grid(row=3, column=2)
    Button(frame7, text="None", font=("Arial", 30, "bold"), bg="light pink", command=a7_right).grid(row=3, column=3)

    Label(frame8, text="Fullform of AD", font=("Arial", 50, "bold")).grid(row=1, column=1)
    Button(frame8, text="Anno Domini", font=("Arial", 30, "bold"), bg="light blue", command=a8_right).grid(row=3, column=1)
    Button(frame8, text="Anna Don", font=("Arial", 30, "bold"), bg="light green", command=a8_wrong).grid(row=3, column=2)
    Button(frame8, text="Anno Distorted", font=("Arial", 30, "bold"), bg="light pink", command=a8_wrong).grid(row=3, column=3)

    Label(frame9, text="Fullform Of AI", font=("Arial", 50, "bold")).grid(row=1, column=1)
    Button(frame9, text="Artificial Intelligence", font=("Arial", 30, "bold"), bg="light blue", command=a9_right).grid(row=3, column=1)
    Button(frame9, text="Armend Intelligence", font=("Arial", 30, "bold"), bg="light green", command=a9_wrong).grid(row=3, column=2)
    Button(frame9, text="Armstrong Intelligence", font=("Arial", 30, "bold"), bg="light pink", command=a9_wrong).grid(row=3, column=3)

    Label(frame10, text="What is output of 4+3%5?", font=("Arial", 50, "bold")).grid(row=1, column=1)
    Button(frame10, text="1", font=("Arial", 30, "bold"), bg="light blue", command=a10_wrong).grid(row=3, column=1)
    Button(frame10, text="2", font=("Arial", 30, "bold"), bg="light green", command=a10_wrong).grid(row=3, column=2)
    Button(frame10, text="7", font=("Arial", 30, "bold"), bg="light pink", command=a10_right).grid(row=3, column=3)





def a1_right():
    Label(frame1,text="Correct",font=("Arial",40,"bold"), background="green",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="Marks obtained : 1", font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a1_wrong():
    Label(frame1,text="Incorrect",font=("Arial",40,"bold"), background="red",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="Marks obtained :0", font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a2_right():
    Label(frame2, text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame2, text="Marks obtained : 1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a2_wrong():
    Label(frame2,text="Incorrect",font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame2,text="Marks obtained :0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a3_right():
    Label(frame3,text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame3,text="Marks obtained:1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a3_wrong():
    Label(frame3, text="Incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=1,column=2)
    Label(frame3, text="Marks obtained :0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a4_right():
    Label(frame4, text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame4, text="Marks obtained:1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a4_wrong():
    Label(frame4, text="Incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame4, text="Marks obtained :0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a5_right():
    Label(frame5, text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame5, text="Marks obtained:1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a5_wrong():
    Label(frame5, text="Incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame5, text="Marks obtained :0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a6_right():
    Label(frame6, text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame6, text="Marks obtained:1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a6_wrong():
    Label(frame6, text="Incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame6, text="Marks obtained :0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a7_right():
    Label(frame7, text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame7, text="Marks obtained:1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a7_wrong():
    Label(frame7, text="Incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame7, text="Marks obtained :0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a8_right():
    Label(frame8, text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame8, text="Marks obtained:1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a8_wrong():
    Label(frame8, text="Incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame8, text="Marks obtained :0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a9_right():
    Label(frame9, text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame9, text="Marks obtained:1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a9_wrong():
    Label(frame9, text="Incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame9, text="Marks obtained :0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a10_right():
    Label(frame10, text="Correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame10, text="Marks obtained:1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

def a10_wrong():
    Label(frame10, text="Incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame10, text="Marks obtained :0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=1,column=3)

quiz(y)
a.pack()
a.mainloop()

root.mainloop()