from tkinter import *
from tkinter import messagebox
import random
import sqlite3
import os
from database import showDatabase
from game import playGame

class rockPaperScissors:
	def __init__(self):
		self.con=sqlite3.Connection('Shivank.db')
		self.cur=self.con.cursor()
		self.root=Tk()
		self.title = Label(self.root,text='Rock Paper Scissor',relief='ridge',font='times 30 bold',fg='midnight blue', bg="white",borderwidth=0,highlightthickness = 0)
		self.logo = PhotoImage(file='icons/logo.gif')
		self.logo_image = Label(self.root,image=self.logo, bg="white")
		self.versionLabel = Label(self.root,text='( Ver 1.0 )',font='times 9 italic',bg='white', fg="VioletRed1")
		self.nameLabel = Label(self.root,text='Enter Your Name Please :',font='times 10 bold',bg='white', fg="VioletRed3")
		self.nameEntry = Entry(self.root,font='times 13 bold',bg='ivory',fg = "dark orange", width = 40)
		self.submitButton = None
		self.openSourceLabel = None
		self.scoreboardButton = None


	def play(self,userName):
		self.cur.execute("create table if not exists rps(name varchar2(10),yscore varchar2(5),cscore varchar2(5))")
		self.con.commit()
		self.wipe()
		gameObject = playGame(userName, self.con, self.root)
		temp_scores= gameObject.myGame()
		return temp_scores

	def fun(self):
		if self.nameEntry.get()=='':
			messagebox.showerror('missing input','please fill Name')
		else:
			temp_scores = self.play(self.nameEntry.get())

	def score(self):
		db = showDatabase(self.con)
		db.score()
		self.con.commit()

	def createHomeWinodw(self):
		self.title.place(x=30,y=180)
		self.logo_image.place(x=120,y=10)
		self.versionLabel.place(x=200,y=230, anchor=CENTER)
		self.nameLabel.place(x=80,y=270, anchor=CENTER)
		self.nameEntry.place(x=5,y=280, height=25)
		self.openSourceLabel.place(x=80,y=400)
		self.scoreboardButton.place(x=150,y=350)
		self.submitButton.place(x=163,y=315)

	def wipe(self):
		self.title.place_forget()
		self.logo_image.place_forget()
		self.versionLabel.place_forget()
		self.nameLabel.place_forget()
		self.nameEntry.place_forget()
		self.submitButton.place_forget()
		self.scoreboardButton.place_forget()
		self.openSourceLabel.place_forget()
		self.root.update()

	def game(self):
		self.submitButton = Button(self.root,text="SUBMIT",bg='misty rose',fg="blue4",height='1',width='4',command=self.fun)
		self.openSourceLabel = Label(self.root,text='Made With '+ u"\u2764" + ' of Open Source',relief='ridge',font='times 13 bold',fg='red', bg="white",borderwidth=0,highlightthickness = 0)
		self.scoreboardButton = Button(self.root,text='Scoreboard',bg='tomato',fg = "blue4",height='1',width='7',command=self.score)
		self.createHomeWinodw()
		## Changed Background
		self.root.configure(bg="white")

		## locks the window so that It does not look vague on expandng
		self.root.resizable(0,0)
		self.root.configure(height=675,width=675)
		self.root.title("Rock Paper Scissors")
		self.root.mainloop()

g = rockPaperScissors()
g.game()