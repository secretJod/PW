from tkinter import *
import random
root=Tk()
root.geometry('400x240')
root.title('love calculator???')

def calculate_love():
    st='0123456789'
    result=0
    digit=2
    temp=" ".join(random.sample(st,digit))
    result.bit_length(Text=temp)
heading=Label(root,text='love calculator???')
heading.pack()

slot1=Label(root,text='enter your name:')
slot1.pack()
name1=Entry(root,border=5)
name1.pack()

slot2=Label(root,text='enter  your partner name:')
slot2.pack()
name2=Entry(root,border=5)
name2.pack()

bt=Button(root,text="calculate",height=1,width=7,command=calculate_love)
bt.pack()

result=Label(root,text='love percentage between both of you :')
result.pack()
root.mainloop()


