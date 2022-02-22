import numbers
from tkinter import*
mansLogs=Tk()
mansLogs.title("Shushi buh kuh")

def btnClick(number):
    current = e.get() #nolasa esošo skaitli
    e.delete(0,END) #nodzēš no sākuma līdz beigām
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) #ievieto displejā
    return 0

def btnCommand(command):
    global number #jāiegaumē skaitlis un darbība
    global mathOp # matemātisks operators
    mathOp=command #+,-,*,/
    global num1
    num1=int(e.get())
    e.delete(0,END)
    return 0

def Equals():
    num2=int(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="/":
        result=num1/num2
    elif mathOp=="*":
        result=num1*num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def Clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

e=Entry(mansLogs,width=13,font=("Arial Black",23))

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
btnClear=Button(mansLogs, text="C",padx="40",pady="40",command=Clear)
btnEquals=Button(mansLogs, text="=",padx="40",pady="40",command=Equals)
btnComma=Button(mansLogs, text=",",padx="40",pady="40")


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