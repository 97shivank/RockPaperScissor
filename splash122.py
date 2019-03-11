from Tkinter import *
root=Tk()
#root.geometry('400x400')
def fun(e=0):
    root.destroy()
    
img1=PhotoImage(file='shiv.gif')
lb=Label(root,image=img1)
Label(root,text='NAME: SHIVANK SINGH',font='arial 40 bold').grid(row=1,column=0,sticky=N+S+E+W)
Label(root,text='ENROLLMENT NUMBER: 171B122',font='arial 20 bold').grid(row=2,column=0,sticky=N+S+E+W)
Label(root,text='BATCH: B5',font='arial 20 bold').grid(row=3,column=0,sticky=N+S+E+W)
Label(root,text='E-MAIL: 97SHIVANK@GMAIL.COM',font='arial 20 bold').grid(row=4,column=0,sticky=N+S+E+W)
Label(root,text='MOB NO:8004406877',font='arial 20 bold').grid(row=5,column=0,sticky=N+S+E+W)
lb.bind('<Motion>',fun)
lb.grid(row=0,column=0,sticky=N+S+E+W)
root.mainloop()
    
