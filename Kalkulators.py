from ast import operator
from distutils import command
from tkinter import*
from math import*
from unittest.util import strclass
mansLogs=Tk()
mansLogs.title("Kalkulators")
mansLogs.configure(background="orange")

#=============================================================================================================================================================================
def btnClick(number):
    current = e.get() #nolasa esošo skaitli
    e.delete(0,END) #nodzēš no sākuma līdz beigām
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) #ievieto displejā
    return 0

def show_point():
    if e.get()==".":
        pass
    else:
        e.insert(END,".")


def correct(inp):
    if inp == '':
        return True
    if ' ' in inp:
        return False
    try:
        float(inp)
    except ValueError: #catching error because strings cannot be converted to string
        return False
    else:
        return True

def btnCommand(command):
    global number #jāiegaumē skaitlis un darbība
    global mathOp # matemātisks operators
    mathOp=command #+,-,*,/
    global num1
    num1=float(e.get())
    e.delete(0,END)
    return 0



def Equals():
    num2=float(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="/":
        result=num1/num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp==",":
        result=num1+num2/10^num2.count()
    elif mathOp=="%":
        result= num1*0.01*num2
    elif mathOp=="|x|":
        result= modf(num1)
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def sq_rt():
    global operator
    global num1

    num1=float(e.get())
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)

def Log10():
    global operator
    global num1

    num1=float(e.get())
    num2=log10(num1)
    e.delete(0,END)
    e.insert(0,num2)

def Square():
    global num1

    num1=float(e.get())
    num2=num1*num1
    e.delete(0,END)
    e.insert(0,num2)

def Clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

#=============================================================================================================================================================================
reg = mansLogs.register(correct) #registering validation

e=Entry(mansLogs,width=13,font=("Arial black",23),validate='key',bg="lightblue",fg="orange", validatecommand=(reg, '%P'),bd=30)


e.grid(row=0,column=0,columnspan=3)

btn0=Button(mansLogs,bd=20, text="0",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(0))
btn1=Button(mansLogs,bd=20, text="1",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(1))
btn2=Button(mansLogs,bd=20, text="2",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(2))
btn3=Button(mansLogs,bd=20, text="3",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(3))
btn4=Button(mansLogs,bd=20, text="4",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(4))
btn5=Button(mansLogs,bd=20, text="5",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(5))
btn6=Button(mansLogs,bd=20, text="6",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(6))
btn7=Button(mansLogs,bd=20, text="7",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(7))
btn8=Button(mansLogs,bd=20, text="8",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(8))
btn9=Button(mansLogs,bd=20, text="9",padx="30",font=("Arial",20),pady="30",bg="cyan",fg="orange",command=lambda:btnClick(9))
btnTimes=Button(mansLogs,bd=20, text="*",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange", command=lambda:btnCommand("*"))
btnSlash=Button(mansLogs,bd=20, text="/",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange", command=lambda:btnCommand("/"))
btnMinus=Button(mansLogs,bd=20, text="-",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange", command=lambda:btnCommand("-"))
btnPlus=Button(mansLogs,bd=20, text="+",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange", command=lambda:btnCommand("+"))
btnPercent=Button(mansLogs,bd=20, text="%",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange", command=lambda:btnCommand("%"))
btnSqrt=Button(mansLogs,bd=20, text="√",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange", command=sq_rt)
btnClear=Button(mansLogs,bd=20, text="C",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange",command=Clear)
btnEquals=Button(mansLogs,bd=20, text="=",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange",command=Equals)
btnComma=Button(mansLogs,bd=20, text=",",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange",command=show_point)
btnLog10=Button(mansLogs,bd=20, text="Lg",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange",command=Log10)
btnSqr=Button(mansLogs,bd=20, text="^2",padx="30",font=("Arial",20),pady="30",bg="yellow",fg="orange",command=Square)


btnPercent.grid(row=5,column=0)
btnSqrt.grid(row=5,column=1)
btnLog10.grid(row=5,column=2)
btnSqr.grid(row=5,column=3)


btnComma.grid(row=4,column=0)
btn0.grid(row=4,column=1)
btnMinus.grid(row=4,column=2)
btnEquals.grid(row=4,column=3)


btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)
btnPlus.grid(row=3,column=3)


btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btnTimes.grid(row=2,column=3)


btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btnSlash.grid(row=1,column=3)


btnClear.grid(row=0,column=3)


mansLogs.mainloop() #atkārto ciklu vairrākkārtēji