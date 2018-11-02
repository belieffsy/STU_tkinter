from tkinter import *

#输入数字1234567890.
def Enter(num):
    
    if happens==[]:
        oldnum=result.get()
        if oldnum=='0' and num!='.':
            result.set(num)
       
        elif '.'in oldnum and num=='.':
            messagebox.showinfo("提示", "当前已经有小数点了哦!")
        else:
            newnum=oldnum+num
            result.set(newnum)
    else:
        if num=='.':
            result.set('0'+num)
            happens.clear()
        else:
            happens.clear()
            result.set(num)
    
def Cmenu():
    var.set('')
    result.set('0')
    numlist.clear()
def CEmenu():
    result.set('0')
def Dmenu():
    num=result.get()
    num2=var.get()
    if len(num)==1 and num!='0':
        result.set('0')
    elif num=='0':
        var.set(num2[0:len(num2)-1])  
    else:
        result.set(num[0:len(num)-1])

#运算符+-*\       
def Eoperator(sign):
    num1=result.get()
    num2=var.get()
    
    if len(num2)!=0 and num2[-1]in('1','2','3','4','5','6','7','8','9','0','²'):
        new=num1+sign
        var.set(new)
        result.set('0')
        
        
    elif num1=='0':
        var.set('0'+sign)
    else:
        new=num2+num1+sign
        
        res=EEqual()
        var.set(new)
    
    #numlist.append(sign)
    #print(numlist)
    #var.set(new)
    #result.set('0')
    
#将大于10^13或小于10^(-13)的结果转化为科学计数法显示
def ScienceResult(res):
    if res>10000000000000:
        i=13
        res1=res/10000000000000
        while res1>=10:
            res1/=10
            i+=1
            
        if len(str(res1))>5 and int(str(res1)[5])>=5:
            res1+=0.001
        return str(res1)[0:5]+'E'+str(i)
    elif res<0.00000000000001 and res>0:
        i=-13
        res1=res*10000000000000
        while res1<1:
            res1*=10
            i+=1
        if len(str(res1))>5 and int(str(res1)[5])>=5:
            res1+=0.001
        return str(res1)[0:5]+'E'+str(i)
    elif res<0:
        if res<-10000000000000:
            i=13
            res1=res/10000000000000
            print(res1)
            while res1<=-10:
                res1/=10
                i+=1
            if len(str(res1))>6 and int(str(res1)[6])>=5:
                res1-=0.001
            return str(res1)[0:6]+'E'+str(i)
        else:
            if len(str(res))>18:
                if int(str(res)[14])>=5:
                    res+=0.000000000000001
            return str(res)[0:14]     
    else:
        if len(str(res))>17:
            if int(str(res)[13])>=5:
                res+=0.000000000000001
        return str(res)[0:13]

#X²
def Esquare():
    num1=result.get()
    num2=var.get()
    new=num2+num1+'²'
    new2=num1+'²'
    x=float(num1)
    xx=x*x
    if num2==''or num2[-1]in('1','2','3','4','5','6','7','8','9','0','²'):
        var.set(new2)
        res=ScienceResult(xx)
        result.set(res)

        test=new2+'='+res
        history.append(test)
        happens.append(res)
        
    else:
        var.set(new)
        result.set('')

#1/x
def Ereciprocal():
    num1=result.get()
    num2=var.get()
    new=num2+'1'+'/'+num1
    new2='1'+'/'+num1
    if num2==''or num2[-1]in('1','2','3','4','5','6','7','8','9','0','²'):
        var.set(new2)
        x=float(num1)
        x1=1/x
        res=ScienceResult(x1)
        result.set(res)

        test=new2+'='+res
        history.append(test)
        happens.append(res)

    else:
        var.set(new)
        result.set('')
 
#√
def Esq():
    num1=result.get()
    num2=var.get()
    new=num2+'√'+num1
    new2='√'+num1
    if num2==''or num2[-1]in('1','2','3','4','5','6','7','8','9','0','²'):
        var.set(new2)
        x=float(num1)
        x1=x**0.5
        res=ScienceResult(x1)
        result.set(res)

        test=new2+'='+res
        history.append(test)
        happens.append(res)
    else:
        var.set(new)
#=    
def EEqual():
    num1=var.get()
    num2=result.get()
    if '²' in num1:
        if '+' in num1 or '-'in num1 or'*'in num1 or'/'in num1:
            p1=r"(?<=\D)\d+?(?=²)"
            pattern1 = re.compile(p1)
            num=pattern1.findall(num1)[0]
            p2=r".+?(?=\d+?²)"
            pattern2 = re.compile(p2)
            num2=pattern2.findall(num1)[0]
            computrstr=''.join(num2+num+'*'+num)
            endnum=eval(computrstr)
            res=ScienceResult(endnum)
            result.set(res)
        
            test=num1+'='+res
            history.append(test)
            happens.append(res)
            
    elif '√'in num1:
        if '+' in num1 or '-'in num1 or'*'in num1 or'/'in num1:
            p1=r"(?<=\D)\d+?"
            pattern1 = re.compile(p1)
            num=pattern1.findall(num1)[0]
            p2=r".+?(?=√)"
            pattern2 = re.compile(p2)
            num2=pattern2.findall(num1)[0]
            computrstr=''.join(num2+num+'**'+'0.5')
            endnum=eval(computrstr)
            res=ScienceResult(endnum)
            result.set(res)
        
            test=num1+'='+res
            history.append(test)
            happens.append(res)
    elif '1/'in num1:
        if '+' in num1 or '-'in num1 or'*'in num1 or '/'in num1:
            numlist.append(num1)
            numlist.append(num2)
            computrstr=''.join(numlist)
            endnum=eval(computrstr)
            res=ScienceResult(endnum)
            result.set(res)
            var.set(computrstr)
            numlist.clear()

            test=num1+num2+'='+res
            history.append(test)
            happens.append(res)
            
            
    elif num1==''or num1.find('+')==-1 and num1.find('-')==-1 and num1.find('*')==-1 and num1.find('/')==-1:
        var.set(num2)
        test=num2+'='+num2
        history.append(test)
        happens.append(num2)
           
    else:
        if len(num1)!=0 and num1[-1]in('1','2','3','4','5','6','7','8','9','0'):
            result.set(num2)
            var.set(num1)
          
        else:
            numlist.append(num1)
            numlist.append(num2)
            computrstr=''.join(numlist)
            endnum=eval(computrstr)
            res=ScienceResult(endnum)
            result.set(res)
            var.set(computrstr)
            numlist.clear()

            test=num1+num2+'='+res
            history.append(test)
            happens.append(res)
            
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
class ClearHistory:
    def __init__(self):
        root3=self.root3=Tk()
        root3.title('提示')
        root3.geometry('320x110')
        l=Label(root3,text='     \n     是否确定删除历史记录?     \n',font=('14'))
        l.grid(row=3,columnspan=16)
        button=Button(root3,text="  确定  ",command=self.ok).grid(row=4,column=6)
        Button(root3,text="  取消  ",command=self.no).grid(row=4,column=8)
    def ok(self):
        history.clear()
        self.root3.destroy()
    def no(self):
        self.root3.destroy()

def About():
    root4=Tk()
    root4.title('About')
    root4.geometry('200x80')
    l=Label(root4,text="\n  author : fwx529707  \n").grid(row=1)
    

happens=[] #保存临时的计算结果

history=[] #历史记录

numlist=[] #记录计算过程

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
t1=Label(root,width=16,textvariable = result,anchor='se',font=('微软雅黑','16'))
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
Hmenu.add_command(label="About...",command=About)

root.mainloop()
