from ast import operator
from distutils import command
from tkinter import*
from math import*
from unittest.util import strclass
mansLogs=Tk()
mansLogs.title("Kalkulators")

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

def Mod():
    global operator
    global num1

    num1=float(e.get())
    num2=modf(num1)
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

e=Entry(mansLogs,width=13,font=("Arial Black",23),validate='key', validatecommand=(reg, '%P'))


e.grid(row=0,column=0,columnspan=3)

btn0=Button(mansLogs, text="0",padx="40",pady="40",command=lambda:btnClick(0))
btn1=Button(mansLogs, text="1",padx="40",pady="40",command=lambda:btnClick(1))
btn2=Button(mansLogs, text="2",padx="40",pady="40",command=lambda:btnClick(2))
btn3=Button(mansLogs, text="3",padx="40",pady="40",command=lambda:btnClick(3))
btn4=Button(mansLogs, text="4",padx="40",pady="40",command=lambda:btnClick(4))
btn5=Button(mansLogs, text="5",padx="40",pady="40",command=lambda:btnClick(5))
btn6=Button(mansLogs, text="6",padx="40",pady="40",command=lambda:btnClick(6))
btn7=Button(mansLogs, text="7",padx="40",pady="40",command=lambda:btnClick(7))
btn8=Button(mansLogs, text="8",padx="40",pady="40",command=lambda:btnClick(8))
btn9=Button(mansLogs, text="9",padx="40",pady="40",command=lambda:btnClick(9))
btnTimes=Button(mansLogs, text="*",padx="40",pady="40", command=lambda:btnCommand("*"))
btnSlash=Button(mansLogs, text="/",padx="40",pady="40", command=lambda:btnCommand("/"))
btnMinus=Button(mansLogs, text="-",padx="40",pady="40", command=lambda:btnCommand("-"))
btnPlus=Button(mansLogs, text="+",padx="40",pady="40", command=lambda:btnCommand("+"))
btnPercent=Button(mansLogs, text="%",padx="40",pady="40", command=lambda:btnCommand("%"))
btnSqrt=Button(mansLogs, text="√",padx="40",pady="40", command=sq_rt)
btnClear=Button(mansLogs, text="C",padx="40",pady="40",command=Clear)
btnEquals=Button(mansLogs, text="=",padx="40",pady="40",command=Equals)
btnComma=Button(mansLogs, text=",",padx="40",pady="40",command=show_point)
btnMod=Button(mansLogs, text="|x|",padx="40",pady="40",command=Mod)
btnSqr=Button(mansLogs, text="^2",padx="40",pady="40",command=Square)


btnPercent.grid(row=5,column=0)
btnSqrt.grid(row=5,column=1)
btnMod.grid(row=5,column=2)
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