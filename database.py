from tkinter import *
import sqlite3

class showDatabase:
	def __init__(self, conn, root):
		self.con=conn
		self.cur=self.con.cursor()
		self.root = root
		self.root.title("Scoreboard")
		self.root.configure(height=675,width=675)
		self.root.config(background='white')
		self.root.resizable(0,0)

	def score(self):
		## Removing Null entries
		try:
			self.cur.execute("delete from rps where name = ''")
		except Exception as e:
			self.cur.execute("Create table rps(name varchar2(20), yscore number(10),cscore number(10))")
		
		## SELECTING ROWS BY DECREASING ORDER OF COMPUTER SCORE
		self.cur.execute('select * from rps order by cscore DESC')
		rows=self.cur.fetchall()
		
		## CREATING LABELS FOR COLUMN HEADERS
		Label(self.root,text= "Name".center(20),bg="SpringGreen2",fg='black',font='Arial 20 bold').grid(row=0,column=1, sticky='ew')
		Label(self.root,text="Your Score".center(20).center(20),bg="SpringGreen2",fg='black',font='Arial 20 bold').grid(row=0,column=2, sticky='ew')
		Label(self.root,text= "Computer Score".center(20) ,bg="SpringGreen2",fg='black',font='Arial 20 bold').grid(row=0,column=3, sticky='ew')
		
		## FETCHING EACH ROW
		for i in range(1,18):
			if i%2==0:
				color = "plum1"
			else:
				color = "PaleTurquoise1"
			if i < len(rows):
				name,yscore,cscore = rows[i-1][0],rows[i-1][1],row[i-1][2]
			else:
				name,yscore,cscore = "Empty", "", ""
			Label(self.root,text= str(name).center(20),borderwidth=1,bg=color,fg='black',font='Arial 20 bold').grid(row=i,column=1, sticky='ew')
			Label(self.root,text=str(yscore).center(20),borderwidth=1,bg=color,fg='black',font='Arial 20 bold').grid(row=i,column=2, sticky='ew')
			Label(self.root,text= str(cscore).center(20),borderwidth=1,bg=color,fg='black',font='Arial 20 bold').grid(row=i,column=3, sticky='ew')
		
		Button(self.root, text="Reset", bg="khaki1", fg="brown", command=self.delete).grid(row=19,column=2)
		self.root.update()
		print (self.root.winfo_geometry())
		self.root.mainloop()
	
	def delete(self):
		self.cur.execute("drop table rps")
		self.__init__(self.con, self.root)
		self.score()