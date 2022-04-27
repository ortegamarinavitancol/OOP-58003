from tkinter import *
window = Tk()
window.title("The Grid Manager")
window.geometry("500x400+20+10")

class MyWindow:
    def __init__(self,window):
        self.lbl1 = Label(window,text="Standard Calculator")
        self.lbl1.grid(row = 1,column = 1)
        self.lbl2 = Label(window,text="Input the 1st Number:")
        self.lbl2.grid(row=2,column=0)
        self.entry3 = Entry(window)
        self.entry3.grid(row=2, column=1, padx=4)
        self.lbl3=Label(window,text="Input the 2nd Number:")
        self.lbl3.grid(row=3,column=0)
        self.entry4 = Entry(window)
        self.entry4.grid(row=3, column=1, padx=4)

        self.lbl4 = Label(window, text='Choose among the operators', justify="left", bg="yellow")
        self.lbl4.grid(row=4, column=0)
        self.btn1=Button(window,text="Add(+)",width=10,command=self.add)
        self.btn1.grid(row=5,column=0)
        self.btn2=Button(window,text="Subtract(-)",width=10,command=self.subtract)
        self.btn2.grid(row=5, column=1, sticky=W)
        self.btn3 = Button(window,text="Multiply(*)",width=10,command=self.multiply)
        self.btn3.grid(row=5,column=2,sticky=W)
        self.btn4 = Button(window,width=10,text="Division(/)")
        self.btn4.grid(row=5,column=3,padx=5,sticky=E)
        self.btn4.bind('<Button-1>',self.div)

        self.lbl5=Label(window,text="Answer")
        self.lbl5.grid(row=6,column = 0)

        self.entry5=Entry(window)
        self.entry5.grid(row=6, column = 1)

    def add(self):
        self.entry5.delete(0,'end')
        number1=int(self.entry3.get())
        number2=int(self.entry4.get())
        answer=number1+number2
        self.entry5.insert(END,str(answer))

    def subtract(self):
        self.entry5.delete(0, 'end')
        number1 = int(self.entry3.get())
        number2 = int(self.entry4.get())
        answer = number1 - number2
        self.entry5.insert(END, str(answer))
    def multiply(self):
        self.entry5.delete(0, 'end')
        number1 = int(self.entry3.get())
        number2 = int(self.entry4.get())
        answer = number1 * number2
        self.entry5.insert(END, str(answer))

    def div(self,event):
        self.entry5.delete(0, 'end')
        number1 = int(self.entry3.get())
        number2 = int(self.entry4.get())
        answer = number1 / number2
        self.entry5.insert(END, str(answer))
mywin=MyWindow(window)

window.mainloop()
