from tkinter import *
import sqlite3

class showDatabase:
	def __init__(self, conn):
		self.con=conn
		self.cur=self.con.cursor()
		self.root = Tk()
		self.root.title("Scoreboard")
		self.root.config(background='white')

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
		Label(self.root,text= "Name".center(30),bg="SpringGreen2",fg='black',font='Arial 20 bold').grid(row=0,column=1, sticky='ew')
		Label(self.root,text="Your Score".center(30).center(30),bg="SpringGreen2",fg='black',font='Arial 20 bold').grid(row=0,column=2, sticky='ew')
		Label(self.root,text= "Computer Score".center(30) ,bg="SpringGreen2",fg='black',font='Arial 20 bold').grid(row=0,column=3, sticky='ew')
		
		## FETCHING EACH ROW
		for row in rows:
			if rows.index(row)%2==0:
				color = "plum1"
			else:
				color = "PaleTurquoise1"
			Label(self.root,text= str(row[0]).center(30),borderwidth=1,bg=color,fg='black',font='Arial 20 bold').grid(row=rows.index(row)+1,column=1, sticky='ew')
			Label(self.root,text=str(row[1]).center(30),borderwidth=1,bg=color,fg='black',font='Arial 20 bold').grid(row=rows.index(row)+1,column=2, sticky='ew')
			Label(self.root,text= str(row[2]).center(30),borderwidth=1,bg=color,fg='black',font='Arial 20 bold').grid(row=rows.index(row)+1,column=3, sticky='ew')

		Button(self.root, text="Reset", bg="khaki1", fg="brown", command=self.delete).grid(row=len(rows)+1,column=2)
		self.root.mainloop()
	
	def delete(self):
		self.cur.execute("drop table rps")
		self.root.destroy()
		self.__init__(self.con)
		self.score()