from tkinter import *
import time
import random

root = Tk()
root.title("Let's Play !!")
root.configure(bg="white")
user_score = 0
comp_score = 0
logo=PhotoImage(file='icons/logo.gif')
iconRock = PhotoImage(file='icons/iconRock.png')
iconPaper = PhotoImage(file='icons/iconPaper.png')
iconScissors = PhotoImage(file='icons/iconScissors.png')
outputRock = PhotoImage(file='icons/outputRock.png')
outputPaper = PhotoImage(file='icons/outputPaper.png')
outputScissors = PhotoImage(file='icons/outputScissors.png')

Label(root,text='Hello Deepak Chauhan'+' Hit Your Choice!!',font='times 20 bold',bg='white',fg="SlateBlue2",width=52,height=1,anchor=CENTER).place(x=0, y=10)
Label(root,text='User Score: %d'%(user_score),font='times 20 bold',bg='white',fg="red",anchor=CENTER,width=24,height=1).place(x=0, y=65)
Label(root,text='Computer Score: %d'%(comp_score),font='times 20 bold',bg='white',fg="green4",anchor=CENTER,width=26,height=1).place(x=340, y=65)
Label(root,text='~ Result ~',font='times 20 bold',bg='pink',fg="midnight blue",anchor=CENTER,width=52,height=1).place(x=0, y=520)
Label(root,text='~ Choose ~',font='times 20 bold',bg='pink',fg="midnight blue",anchor=CENTER,width=52,height=1).place(x=0, y=410)
Label(root,image=logo,bg="white",height=300,width=250).place(x=30,y=100)
Label(root,image=logo,bg="white",height=300,width=250).place(x=400,y=100)

def Rock():
	global user_score, comp_score,logo,iconRock,iconPaper,iconScissors,outputRock,outputPaper,outputScissors
	comp = random.randint(1,3)
	Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
	if comp == 3:
		comp = "Scissor"
		user_score+=1
		for i in range(5):
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
		Label(root,text='User Score: %d'%(user_score),font='times 20 bold',bg='white',fg="red",anchor=CENTER,width=24,height=1).place(x=0, y=65)
		Label(root,text='YOU WON, Keep It Coming !!',font='times 15 bold',bg="white",fg="green",width=67,height=1,anchor=CENTER).place(x=0, y=560)
	elif comp==1: 
		comp = "Rock"
		for i in range(5):
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=400,y=100)
		Label(root,text="It's a TIE",font='times 15 bold',fg="saddle brown",bg="white",width=67,height=1,anchor=CENTER).place(x=0, y=560)
	else:
		comp = "Paper"
		comp_score+=1
		for i in range(5):
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
		Label(root,text='Computer Score: %d'%(comp_score),font='times 20 bold',bg='white',fg="green4",anchor=CENTER,width=26,height=1).place(x=340, y=65)
		Label(root,text='YOU LOST, Try Again',font='times 15 bold',bg="white",fg="red",width=67,height=1,anchor=CENTER).place(x=0, y=560)
	
def paper():
	global user_score, comp_score,logo,iconRock,iconPaper,iconScissors,outputRock,outputPaper,outputScissors
	comp = random.randint(1,3)
	Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
	if comp == 1:
		comp = "Rock"
		user_score+=1
		for i in range(5):
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=400,y=100)
		Label(root,text='User Score: %d'%(user_score),font='times 20 bold',bg='white',fg="red",anchor=CENTER,width=24,height=1).place(x=0, y=65)
		Label(root,text='YOU WON, Keep It Coming !!',font='times 15 bold',bg="white",fg="green",width=67,height=1,anchor=CENTER).place(x=0, y=560)
	elif comp==2:
		comp = "Paper"
		for i in range(5):
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
		Label(root,text="It's a TIE",font='times 15 bold',fg="saddle brown",bg="white",width=67,height=1,anchor=CENTER).place(x=0, y=560)
	else:
		comp = "Scissor"
		comp_score+=1
		for i in range(5):
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
		Label(root,text='Computer Score: %d'%(comp_score),font='times 20 bold',bg='white',fg="green4",anchor=CENTER,width=26,height=1).place(x=340, y=65)
		Label(root,text='YOU LOST, Try Again',font='times 15 bold',fg="red",bg="white",width=67,height=1,anchor=CENTER).place(x=0, y=560)
			
	
def scissor():
	global user_score, comp_score,logo,iconRock,iconPaper,iconScissors,outputRock,outputPaper,outputScissors
	comp = random.randint(1,3)
	Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
	if comp == 2:
		comp = "Paper"
		user_score+=1
		for i in range(5):
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
		Label(root,text='User Score: %d'%(user_score),font='times 20 bold',bg='white',fg="midnight blue",anchor=CENTER,width=24,height=1).place(x=0, y=65)
		Label(root,text='YOU WON, Keep It Coming !!',font='times 15 bold',bg="white",fg="green",width=67,height=1,anchor=CENTER).place(x=0, y=560)
	elif comp==3:
		comp = "Scissor"
		for i in range(5):
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
		Label(root,text="It's a TIE",font='times 15 bold',fg="saddle brown",bg="white",width=67,height=1,anchor=CENTER).place(x=0, y=560) 
		
	else:
		comp = "Rock"
		comp_score+=1
		for i in range(5):
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
			root.update()
			time.sleep(.1)
			Label(root,image=outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			Label(root,image=outputRock,bg="white",height=300,width=250).place(x=400,y=100)
		Label(root,text='Computer Score: %d'%(comp_score),font='times 20 bold',bg='white',fg="green4",anchor=CENTER,width=26,height=1).place(x=340, y=65)
		Label(root,text='YOU LOST, Try Again',font='times 15 bold',bg="white",fg="red",width=67,height=1,anchor=CENTER).place(x=0, y=560)
			
B1 = Button(root, image = iconRock,bg='white',height=50,width=50,borderwidth=0,highlightthickness = 0,command = lambda: Rock())
B2 = Button(root, image = iconPaper,bg='white',height=50,width=50,borderwidth=0,highlightthickness = 0,command = lambda: paper())
B3 = Button(root, image = iconScissors,bg='white',height=53,width=50,borderwidth=0,highlightthickness = 0,command = lambda: scissor())
	
B1.place(x=240,y=450)
B2.place(x=310,y=450)
B3.place(x=380,y=447)
root.resizable(0,0)
root.geometry('675x600')
root.mainloop()