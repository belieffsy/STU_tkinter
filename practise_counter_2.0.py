from tkinter import *



#输入数字
def Enter(num):
    oldnum=result.get()
    if oldnum=='0':
        result.set(num)
    else:
        newnum=oldnum+num
        result.set(newnum)        
    
def Cmenu():
    var.set('')
    result.set('0')
    numlist.clear()
def CEmenu():
    result.set('0')
def Dmenu():
    num=result.get()
    if len(num)==1:
        result.set('0')
    else:
        result.set(num[0:len(num)-1])

#输入运算符+-*\       
def Eoperator(sign):
    num1=result.get()
    num2=var.get()
    if num2.endswith('1')or num2.endswith('2')or num2.endswith('3')or num2.endswith('4')or num2.endswith('5')or num2.endswith('6')or num2.endswith('7')or num2.endswith('8')or num2.endswith('9')or num2.endswith('0')or num2.endswith('.')or num2.endswith('²'):
        new=num1+sign
        var.set(new)      
    else:
        new=num2+num1+sign
        var.set(new)
    result.set('0')
    #numlist.append(sign)
    #print(numlist)
    #var.set(new)
    #result.set('0')

#X²
def Esquare():
    num1=result.get()
    num2=var.get()
    new=num2+num1+'²'
    var.set(new)
    x=float(num1)
    xx=x*x
    xt=str(xx)
    result.set(xt)

    test=new+'='+xt
    history.append(test)

#1/x
def Ereciprocal():
    num1=result.get()
    num2=var.get()
    new=num2+'1'+'/'+num1
    var.set(new)
    x=float(num1)
    x1=1/x
    xt=str(x1)
    result.set(xt)

    test=new+'='+xt
    history.append(test)
 
#√
def Esq():
    num1=result.get()
    num2=var.get()
    new=num2+'√'+num1
    var.set(new)
    x=float(num1)
    x1=x**0.5
    xt=str(x1)
    result.set(xt)

    test=new+'='+xt
    history.append(test)
#=    
def EEqual():
    num1=var.get()
    num2=result.get()
    numlist.append(num1)
    numlist.append(num2)
    #print(numlist)
    computrstr=''.join(numlist)
    endnum=eval(computrstr)
    result.set(endnum)
    var.set(computrstr)
    numlist.clear()

    res=str(endnum)
    test=num1+num2+'='+res
    history.append(test)
#
def History():
    if history==[]:
        messagebox.showinfo("提示", "当前还没有历史记录")
    else:
        root2=Tk()
        root2.title('历史记录')
        root2.geometry('400x200')
        t=Text(root2,font=('14'))
        for i in range(0,len(history)):
            t.insert(END,i+1)
            t.insert(END,') ')
            t.insert(END,history[i])
            t.insert(END,'\n\n')
            t.pack()
#
def ClearHistory():
    history.clear()


history=[]
numlist=[]

#主窗体
root=Tk()
root.title('计算器')
root.geometry('275x352')
var = StringVar()


var.set('')
t1=Label(root,width=24,textvariable = var,anchor='sw',font=('14'))
t1.grid(row=0,column=0,columnspan=8)#columnspan跨列显示 rowspan跨行显示

result = StringVar()
result.set('0')
t1=Label(root,width=14,textvariable = result,anchor='se',font=('微软雅黑','18'))
t1.grid(row=1,column=0,columnspan=8)
#2
Button(root,text=" ← ",command=Dmenu,width=5,height=2).grid(row=2)
Button(root,text=" CE ",command=CEmenu,width=5,height=2).grid(row=2,column=1)
Button(root,text=" C  ",command=Cmenu,width=5,height=2).grid(row=2,column=2)
Button(root,text=" ±  ",width=5,height=2).grid(row=2,column=3)
Button(root,text=" √  ",command=Esq,width=5,height=2).grid(row=2,column=4)
#3
button7=Button(root,text="7",command=lambda :Enter('7'),width=5,height=2)
button7.grid(row=3)
button8=Button(root,text="8 ",command=lambda :Enter('8'),width=5,height=2)
button8.grid(row=3,column=1)
button9=Button(root,text="9 ",command=lambda :Enter('9'),width=5,height=2)
button9.grid(row=3,column=2)
Button(root,text="/",command=lambda :Eoperator('/'),width=5,height=2).grid(row=3,column=3)
Button(root,text="X²",command=Esquare,width=5,height=2).grid(row=3,column=4)
#4
Button(root,text="4 ",command=lambda :Enter('4'),width=5,height=2).grid(row=4)
Button(root,text="5",command=lambda :Enter('5'),width=5,height=2).grid(row=4,column=1)
Button(root,text="6 ",command=lambda :Enter('6'),width=5,height=2).grid(row=4,column=2)
Button(root,text="* ",command=lambda :Eoperator('*'),width=5,height=2).grid(row=4,column=3)
Button(root,text="1/x",command=Ereciprocal,width=5,height=2).grid(row=4,column=4)
#5
Button(root,text="1",command=lambda :Enter('1'),width=5,height=2).grid(row=5)
Button(root,text="2",command=lambda :Enter('2'),width=5,height=2).grid(row=5,column=1)
Button(root,text="3",command=lambda :Enter('3'),width=5,height=2).grid(row=5,column=2)
Button(root,text="- ",command=lambda :Eoperator('-'),width=5,height=2).grid(row=5,column=3)
Button(root,text='= ',bg="orange",command=EEqual,width=5,height=5).grid(row=5,column=4,rowspan=2)
#6
Button(root,text="0 ",command=lambda :Enter('0'),width=11,height=2).grid(row=6,column=0,columnspan=2)
Button(root,text=".",command=lambda :Enter('.'),width=5,height=2).grid(row=6,column=2)
Button(root,text="+",command=lambda :Eoperator('+'),width=5,height=2).grid(row=6,column=3)

#菜单栏
menu=Menu(root)
root.config(menu=menu)

Vmenu=Menu(menu)
menu.add_cascade(label="查看(V)",menu=Vmenu)
Vmenu.add_command(label="标准计算器")
Vmenu.add_command(label="历史记录",command=History)
Vmenu.add_command(label="清空历史记录",command=ClearHistory)

Emenu=Menu(menu)
menu.add_cascade(label="编辑(E)",menu=Emenu)
Emenu.add_command(label="复制")
Emenu.add_command(label="粘贴")

Hmenu=Menu(menu)
menu.add_cascade(label="帮助(H)",menu=Hmenu)
Hmenu.add_command(label="查看关于帮助")
Hmenu.add_command(label="关于计算器")


root.mainloop()
