from tkinter import *
from tkinter import messagebox
import random
import sqlite3
import os
from database import showDatabase
from game import playGame

con=sqlite3.Connection('Shivank.db')
cur=con.cursor()
root=Tk()

Label(root,text='Rock Paper Scissor',relief='ridge',font='times 30 bold',fg='midnight blue', bg="white",borderwidth=0,highlightthickness = 0).place(x=30,y=180)
logo=PhotoImage(file='icons/logo.gif')
Label(root,image=logo, bg="white").place(x=120,y=10)
Label(root,text='( Ver 1.0 )',font='times 9 italic',bg='white', fg="VioletRed1").place(x=200,y=230, anchor=CENTER)
Label(root,text='Enter Your Name Please :',font='times 10 bold',bg='white', fg="VioletRed3").place(x=80,y=270, anchor=CENTER)
n=Entry(root,font='times 13 bold',bg='ivory',fg = "dark orange", width = 40)
n.place(x=5,y=280, height=25)#your name
user_score = 0
comp_score = 0

def play(userName):
	global c1, root, user_score,comp_score,n
	cur.execute("create table if not exists rps(name varchar2(10),yscore varchar2(5),cscore varchar2(5))")
	con.commit()
	gameObject = playGame(userName, con)
	temp_scores= gameObject.myGame()
	return temp_scores

def fun():
	global user_score,comp_score
	if n.get()=='':
		messagebox.showerror('missing input','please fill Name')
	else:
		temp_scores = play(n.get())
		user_score += temp_scores[0]
		comp_score += temp_scores[0]

b4=Button(root,text="SUBMIT",bg='misty rose',fg="blue4",height='1',width='4',command=fun)
b4.place(x=163,y=315)
k=str(n.get())
# cur.execute('insert into rps values(?,?,?)',(k,user_score,comp_score))

def score():
	k=str(n.get())
	# cur.execute('insert into rps values(?,?,?)',(k,user_score,comp_score))
	# con.commit()
	db = showDatabase(con)
	db.score()
	con.commit()

Label(root,text='Made With '+ u"\u2764" + ' of Open Source',relief='ridge',font='times 13 bold',fg='red', bg="white",borderwidth=0,highlightthickness = 0).place(x=80,y=400)

#root.destroy()root.title("Rock Paper Scissors")
Button(root,text='Scoreboard',bg='tomato',fg = "blue4",height='1',width='7',command=score).place(x=150,y=350)

## Changed Background
root.configure(bg="white")
## locks the window so that It does not look vague on expandng
root.resizable(0,0)
root.configure(height=430,width=400)
root.title("Rock Paper Scissors")
root.mainloop()
