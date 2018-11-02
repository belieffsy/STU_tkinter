from tkinter import *

root=Tk()
root.title('计算器')
root.geometry('220x300')

def Enter(num):
    
    oldnum=var.get()
    if oldnum=='0':
        var.set(num)
    else:
        newnum=oldnum+num
        var.set(newnum)
        
    
def Cmenu():
    var.set('0')
    result.set('')
def CEmenu():
    var.set('0')
def Dmenu():
    num=var.get()
    if len(num)==1:
        var.set('0')
    else:
        var.set(num[0:len(num)-1])
def Eoperator(sign):
    num=var.get()
    #numlist.append(num)
    #numlist.append(sign)
    #computrstr=''.join(numlist)
    #print(numlist)
    if num=='0':
        var.set(sign)
    else:
        new=num+sign
        var.set(new)
def EEqual():
    num=var.get()
    numlist.append(num)
    print(numlist)
    computrstr=''.join(numlist)
    print(computrstr)
    endnum=eval(computrstr)
    result.set(endnum)
    var.set(computrstr)
    numlist.clear()
    print(numlist)


numlist=[]
var = StringVar()
var.set('0')
t1=Label(root,width=20,textvariable = var)
t1.grid(row=0,column=0,columnspan=8)#columnspan跨列显示 rowspan跨行显示

result = StringVar()
result.set('')
t1=Label(root,width=20,textvariable = result,anchor='se')
t1.grid(row=1,column=0,columnspan=8)
#2
Button(root,text=" ← ",command=Dmenu).grid(row=2)
Button(root,text=" CE ",command=CEmenu).grid(row=2,column=1)
Button(root,text=" C  ",command=Cmenu).grid(row=2,column=2)
Button(root,text=" ±  ").grid(row=2,column=3)
Button(root,text=" √  ").grid(row=2,column=4)
#3
button7=Button(root,text="  7  ",command=lambda :Enter('7'))
button7.grid(row=3)
button8=Button(root,text="  8  ",command=lambda :Enter('8'))
button8.grid(row=3,column=1)
button9=Button(root,text="  9  ",command=lambda :Enter('9'))
button9.grid(row=3,column=2)
Button(root,text="  /  ",command=lambda :Eoperator('/')).grid(row=3,column=3)
Button(root,text=" %  ").grid(row=3,column=4)
#4
Button(root,text="  4  ",command=lambda :Enter('4')).grid(row=4)
Button(root,text="  5  ",command=lambda :Enter('5')).grid(row=4,column=1)
Button(root,text="  6  ",command=lambda :Enter('6')).grid(row=4,column=2)
Button(root,text="  *  ",command=lambda :Eoperator('*')).grid(row=4,column=3)
Button(root,text="1/x ").grid(row=4,column=4)
#5
Button(root,text="  1  ",command=lambda :Enter('1')).grid(row=5)
Button(root,text="  2  ",command=lambda :Enter('2')).grid(row=5,column=1)
Button(root,text="  3  ",command=lambda :Enter('3')).grid(row=5,column=2)
Button(root,text="  -  ",command=lambda :Eoperator('-')).grid(row=5,column=3)
Button(root,text='''
  =  
    ''',bg="orange",command=EEqual).grid(row=5,column=4,rowspan=2)
#6
Button(root,text="       0       ",command=lambda :Enter('0')).grid(row=6,column=0,columnspan=2)
Button(root,text="  .   ",command=lambda :Enter('.')).grid(row=6,column=2)
Button(root,text="  + ",command=lambda :Eoperator('+')).grid(row=6,column=3)

print(numlist)


root,mainloop()

