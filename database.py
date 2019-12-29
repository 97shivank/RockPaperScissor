from tkinter import *
import sqlite3

class showDatabase:
	def __init__(self, conn, root, home):
		self.con=conn
		self.cur=self.con.cursor()
		self.root = root
		self.root.title("Scoreboard")
		self.root.configure(height=675,width=675)
		self.root.config(background='white')
		self.root.resizable(0,0)
		self.back = PhotoImage(file = 'icons/back.png')
		self.nameLabel = Label(self.root,text= "Name".center(20),bg="SpringGreen2",fg='black',font='Arial 20 bold')
		self.yscoreLabel = Label(self.root,text="Your Score".center(20).center(20),bg="SpringGreen2",fg='black',font='Arial 20 bold')
		self.cscoreLabel = Label(self.root,text= "Computer Score".center(20) ,bg="SpringGreen2",fg='black',font='Arial 20 bold')
		self.resetButton = Button(self.root, text="Reset", bg="khaki1", fg="brown", command=self.delete)
		self.backButton = Button(self.root, image=self.back, bg="white", borderwidth=0,highlightthickness = 0, command= lambda :self.deleteWindow(home))
		self.labelList = []
		for i in range(1,18):
			if i%2==0:
				color = "plum1"
			else:
				color = "PaleTurquoise1"
			self.labelList.append([Label(self.root, text="".center(20), bg=color),Label(self.root, text="".center(20), bg=color),Label(self.root, text="".center(20), bg=color)])
			
	def createWindow(self):
		## CREATING LABELS FOR COLUMN HEADERS
		self.nameLabel.grid(row=0,column=1, sticky='ew')
		self.yscoreLabel.grid(row=0,column=2, sticky='ew')
		self.cscoreLabel.grid(row=0,column=3, sticky='ew')
		self.resetButton.grid(row=19,column=2, sticky='e')
		self.backButton.grid(row=19,column=2, sticky='w')
		# for i in range(1,18):
		# 	self.labelList[i-1][0].grid(row = i, column=1,sticky='ew')
		# 	self.labelList[i-1][1].grid(row = i, column=2,sticky='ew')
		# 	self.labelList[i-1][2].grid(row = i, column=3,sticky='ew')
		
	def score(self):
		## Removing Null entries
		print("making table")
		try:
			self.cur.execute("create table rps(name varchar2(10),yscore varchar2(5),cscore varchar2(5))")
		except Exception as e:
			pass
		
		## SELECTING ROWS BY DECREASING ORDER OF COMPUTER SCORE
		self.cur.execute('select * from rps order by cscore DESC')
		rows=self.cur.fetchall()
		print("created table")
		self.createWindow()
		# FETCHING EACH ROW
		for i in range(1,18):
			if i%2==0:
				color = "plum1"
			else:
				color = "PaleTurquoise1"
			if i < len(rows):
				name,yscore,cscore = rows[i-1][0],rows[i-1][1],rows[i-1][2]
			else:
				name,yscore,cscore = "Empty", "", ""
			self.labelList[i-1][0].configure(text = str(name).center(20),bg=color,fg='black',font='Arial 15')
			self.labelList[i-1][1].configure(text = str(yscore).center(20),bg=color,fg='black',font='Arial 15')
			self.labelList[i-1][2].configure(text = str(cscore).center(20),bg=color,fg='black',font='Arial 15')
			self.labelList[i-1][0].grid(row = i, column=1,sticky='ew')
			self.labelList[i-1][1].grid(row = i, column=2,sticky='ew')
			self.labelList[i-1][2].grid(row = i, column=3,sticky='ew')
		self.root.update()
		self.root.mainloop()
	
	def delete(self):
		self.cur.execute("drop table rps")
		self.__init__(self.con, self.root)
		self.score()

	def deleteWindow(self, home):
		self.nameLabel.grid_forget()
		self.yscoreLabel.grid_forget()
		self.cscoreLabel.grid_forget()
		self.resetButton.grid_forget()
		self.backButton.grid_forget()
		for i in range(1,18):
			self.labelList[i-1][0].grid_forget()
			self.labelList[i-1][1].grid_forget()
			self.labelList[i-1][2].grid_forget()
		home()