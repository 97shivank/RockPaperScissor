from tkinter import *
import time
import random
from updateScore import scoring

class playGame:

	def __init__(self, userName, conn, root):
		self.root = root
		self.user_name = userName
		self.scoreboard = scoring(conn)
		self.user_score, self.comp_score = self.scoreboard.getScore(userName)
		self.logo=PhotoImage(file='icons/logo.gif')
		self.iconRock = PhotoImage(file='icons/iconRock.png')
		self.iconPaper = PhotoImage(file='icons/iconPaper.png')
		self.iconScissors = PhotoImage(file='icons/iconScissors.png')
		self.outputRock = PhotoImage(file='icons/outputRock.png')
		self.outputPaper = PhotoImage(file='icons/outputPaper.png')
		self.outputScissors = PhotoImage(file='icons/outputScissors.png')
		self.user = PhotoImage(file='icons/user.png')
		self.computer = PhotoImage(file='icons/computer.png')

	def onExit(self):
		self.scoreboard.insertData(self.user_name,self.user_score, self.comp_score)
		self.root.destroy()
	
	def myGame(self):
		self.root.title("Let's Play !!")
		self.root.configure(bg="white")
		Label(self.root,text='Hello '+self.user_name+' Hit Your Choice!!',font='times 20 bold',bg='white',fg="SlateBlue2",width=52,height=1,anchor=CENTER).place(x=0, y=10)
		Label(self.root,text='User Score: %d'%(self.user_score),font='times 20 bold',bg='white',fg="red",anchor=CENTER,width=24,height=1).place(x=0, y=65)
		Label(self.root,text='Computer Score: %d'%(self.comp_score),font='times 20 bold',bg='white',fg="green4",anchor=CENTER,width=26,height=1).place(x=340, y=65)
		Label(self.root,text='~ Result ~',font='times 20 bold',bg='pink',fg="midnight blue",anchor=CENTER,width=52,height=1).place(x=0, y=520)
		Label(self.root,text='~ Choose ~',font='times 20 bold',bg='pink',fg="midnight blue",anchor=CENTER,width=52,height=1).place(x=0, y=410)
		Label(self.root,image=self.user,bg="white",height=300,width=250).place(x=30,y=100)
		Label(self.root,image=self.computer,bg="white",height=300,width=250).place(x=400,y=100)

		def Rock():
			comp = random.randint(1,3)
			Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
			if comp == 3:
				comp = "Scissor"
				self.user_score+=1
				for i in range(5):
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
				Label(self.root,text='User Score: %d'%(self.user_score),font='times 20 bold',bg='white',fg="red",anchor=CENTER,width=24,height=1).place(x=0, y=65)
				Label(self.root,text='YOU WON, Keep It Coming !!',font='times 15 bold',bg="white",fg="green",width=67,height=1,anchor=CENTER).place(x=0, y=560)
			elif comp==1: 
				comp = "Rock"
				for i in range(5):
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=400,y=100)
				Label(self.root,text="It's a TIE",font='times 15 bold',fg="saddle brown",bg="white",width=67,height=1,anchor=CENTER).place(x=0, y=560)
			else:
				comp = "Paper"
				self.comp_score+=1
				for i in range(5):
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
				Label(self.root,text='Computer Score: %d'%(self.comp_score),font='times 20 bold',bg='white',fg="green4",anchor=CENTER,width=26,height=1).place(x=340, y=65)
				Label(self.root,text='YOU LOST, Try Again',font='times 15 bold',bg="white",fg="red",width=67,height=1,anchor=CENTER).place(x=0, y=560)
			
		def paper():
			comp = random.randint(1,3)
			Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
			if comp == 1:
				comp = "Rock"
				self.user_score+=1
				for i in range(5):
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=400,y=100)
				Label(self.root,text='User Score: %d'%(self.user_score),font='times 20 bold',bg='white',fg="red",anchor=CENTER,width=24,height=1).place(x=0, y=65)
				Label(self.root,text='YOU WON, Keep It Coming !!',font='times 15 bold',bg="white",fg="green",width=67,height=1,anchor=CENTER).place(x=0, y=560)
			elif comp==2:
				comp = "Paper"
				for i in range(5):
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
				Label(self.root,text="It's a TIE",font='times 15 bold',fg="saddle brown",bg="white",width=67,height=1,anchor=CENTER).place(x=0, y=560)
			else:
				comp = "Scissor"
				self.comp_score+=1
				for i in range(5):
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
				Label(self.root,text='Computer Score: %d'%(self.comp_score),font='times 20 bold',bg='white',fg="green4",anchor=CENTER,width=26,height=1).place(x=340, y=65)
				Label(self.root,text='YOU LOST, Try Again',font='times 15 bold',fg="red",bg="white",width=67,height=1,anchor=CENTER).place(x=0, y=560)
					
			
		def scissor():
			comp = random.randint(1,3)
			Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
			if comp == 2:
				comp = "Paper"
				self.user_score+=1
				for i in range(5):
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
				Label(self.root,text='User Score: %d'%(self.user_score),font='times 20 bold',bg='white',fg="midnight blue",anchor=CENTER,width=24,height=1).place(x=0, y=65)
				Label(self.root,text='YOU WON, Keep It Coming !!',font='times 15 bold',bg="white",fg="green",width=67,height=1,anchor=CENTER).place(x=0, y=560)
			elif comp==3:
				comp = "Scissor"
				for i in range(5):
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
				Label(self.root,text="It's a TIE",font='times 15 bold',fg="saddle brown",bg="white",width=67,height=1,anchor=CENTER).place(x=0, y=560) 
				
			else:
				comp = "Rock"
				self.comp_score+=1
				for i in range(5):
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputPaper,bg="white",height=300,width=250).place(x=400,y=100)
					self.root.update()
					time.sleep(.1)
					Label(self.root,image=self.outputScissors,bg="white",height=300,width=250).place(x=30,y=100)
					Label(self.root,image=self.outputRock,bg="white",height=300,width=250).place(x=400,y=100)
				Label(self.root,text='Computer Score: %d'%(self.comp_score),font='times 20 bold',bg='white',fg="green4",anchor=CENTER,width=26,height=1).place(x=340, y=65)
				Label(self.root,text='YOU LOST, Try Again',font='times 15 bold',bg="white",fg="red",width=67,height=1,anchor=CENTER).place(x=0, y=560)
					
		B1 = Button(self.root, image = self.iconRock,bg='white',height=50,width=50,borderwidth=0,highlightthickness = 0,command = lambda: Rock())
		B2 = Button(self.root, image = self.iconPaper,bg='white',height=50,width=50,borderwidth=0,highlightthickness = 0,command = lambda: paper())
		B3 = Button(self.root, image = self.iconScissors,bg='white',height=53,width=50,borderwidth=0,highlightthickness = 0,command = lambda: scissor())
			
		B1.place(x=240,y=450)
		B2.place(x=310,y=450)
		B3.place(x=380,y=447)
		Label(self.root,text='Made With '+ u"\u2764" + ' of Open Source',relief='ridge',font='times 13 bold',fg='red', bg="white",borderwidth=0,highlightthickness = 0, height=1, width=75, anchor=CENTER).place(x=0,y=635)
		self.root.resizable(0,0)
		self.root.geometry('675x675')
		self.root.protocol("WM_DELETE_WINDOW", self.onExit)
		self.root.mainloop()
		return (self.user_score,self.comp_score)