from Tkinter import *
import tkMessageBox
import random
import sqlite3
acc=0.0
c=1
c1=0
con=sqlite3.Connection('Shivank.db')
cur=con.cursor()
cur.execute("create table if not exists rps(name varchar2(10),yscore varchar2(5),cscore varchar2(5))")
#cur.execute("drop table rps")
con.commit()
root=Tk()
#root.geometry('600x500')
Label(root,text='Rock Paper Scissor',relief='ridge',font='times 50 bold',bg='medium blue').grid(row=0,column=0)
img=PhotoImage(file='rock.gif')
Label(root,image=img).grid(row=1,column=0,columnspan=2)
Label(root,text='Enter Your Name,Please',font='times 30 bold',bg='Slate Blue').grid(row=2,column=0)
n=Entry(root,font='times 20 bold',bg='light grey')
n.grid(row=3,column=0)#your name
user_score = 0
comp_score = 0
def fun1():
    global c1
    cur.execute("drop table rps")
    cur.execute("create table if not exists rps(name varchar2(10),yscore varchar2(5),cscore varchar2(5))")
    con.commit()
    #root.destroy()
    root=Tk()
    #root.geometry('500x400')
    Label(root,text='Hello '+n.get()+' \n Hit Your Choice!!',font='times 40 bold',bg='Slate Blue').grid(row=0,column=0)
    def Rock():
       
            
        global user_score, comp_score
        comp = random.randint(1,3)
    #print("your choice: Rock")
    #print("Comp choice: "+str(comp))
        if comp == 3:
            comp = "Scissor"
            user_score+=1
            Label(root,text="Congratulation!!, YOU WIN!! \n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score),font='times 10 bold',bg='gold').grid(row=4,column=0)
            
            
        elif comp==1: 
            comp = "Rock"
            Label(root,text="              IT'S A TIE!!                  \n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score),font='times 10 bold',bg='SteelBlue1').grid(row=4,column=0)                   
            
        else:
            comp = "Paper"
            comp_score+=1
            Label(root,text="                 YOU LOOSE!!          \n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score),font='times 10 bold',bg='orange red').grid(row=4,column=0)
            
        
    
    def paper():
        
           
        
       
        global user_score, comp_score
    
        comp = random.randint(1,3)
    #print("your choice: paper")
    #print("Comp choice: "+str(comp))
        if comp == 1:
            comp = "Rock"
            user_score+=1
            Label(root,text="Congratulation!!, YOU WIN!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score),font='times 10 bold',bg='gold').grid(row=4,column=0)
            
           # print acc
        elif comp==2:
            comp = "Paper"
            Label(root,text="          IT'S A TIE!!                     \n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score),font='times 10 bold',bg='SteelBlue1').grid(row=4,column=0)
            
        
        else:
            comp = "Scissor"
            comp_score+=1
            Label(root,text="               YOU LOSE!!           \n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score),font='times 10 bold',bg='orange red').grid(row=4,column=0)
            
        #acc=(user_score/int(c))*100.0
    def scissor():
        
            
        global user_score, comp_score
    
        comp = random.randint(1,3)
    #print("your choice: scissor")
    #print("Comp choice: "+str(comp))
        if comp == 2:
            comp = "Paper"
            user_score+=1
            Label(root,text="Congratulation!!,YOU WIN!!\n"+"Your Choice:Scissor"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score),font='times 10 bold',bg='gold').grid(row=4,column=0)
            
            
        elif comp==3:
            comp = "Scissor"
            Label(root,text="       IT'S A TIE!!                        \n"+"Your Choice:Scissor"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score),font='times 10 bold',bg='SteelBlue1').grid(row=4,column=0)  
           
        
        else:
            comp = "Rock"
            comp_score+=1
            Label(root,text="         YOU LOOSE!!                \n"+"Your Choice:Scissor"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score),font='times 10 bold',bg='orange red').grid(row=4,column=0)
            
       
    B1 =Button(root, text = "Rock",bg='red',height="4",width="4", command = Rock)
    #root['bg']='white'
    #okbutton=PhotoImage(file='72.gif')
    #B1=Button(root,image=okbutton,bg='white')
    #B1['border']='0'
    #B1.grid(row=1,column=0,sticky=N+S+E+W)
    #root['bg']='white'
    #okbutton=PhotoImage(file='papr.gif')
    #B2=Button(root,image='okbutton',bg='white')
    #B2['border']='0'
    #B2.grid(row=2,column=0,sticky=N+S+E+W)
    #root['bg']='white'
    #okbutton=PhotoImage(file='sc.gif')
    #B3=Button(root,image='okbutton',bg='white')
    #B3['border']='0'
    #B3.grid(row=3,column=0,sticky=N+S+E+W)
    #B1 =Button(root,  image= '72.gif',bg='red',height="4",width="4", command = Rock)
    B2 = Button(root, text = "Paper",bg='green',height="4",width="4", command = paper)
    B3 = Button(root, text = "Scissor",bg='blue',height="4",width="4", command = scissor)
    B1.grid(row=1,column=0,sticky=N+S+E+W)
    B2.grid(row=2,column=0,sticky=N+S+E+W)
    B3.grid(row=3,column=0,sticky=N+S+E+W)
def fun():
    if n.get()=='':
    	messagebox.showerror('missing input','please fill Name')
    else:
        fun1()    
b4=Button(root,text="SUBMIT",bg='tomato',height='1',width='1',command=fun)
b4.grid(row=4,column=0,sticky=N+S+E+W)
k=str(n.get())
cur.execute('insert into rps values(?,?,?)',(k,user_score,comp_score))
def score():
    k=str(n.get())
    cur.execute('insert into rps values(?,?,?)',(k,user_score,comp_score))
    con.commit()
    cur.execute('select * from rps')
    q=cur.fetchall()
    j=Tk()
    j.title('ScoreBoard')
    Label(j,text='Name',bg='chartreuse2',fg='black',font='Arial 20 bold').grid(row=0,column=0)
    Label(j,text=' ',bg='chartreuse2').grid(row=0,column=1)
    Label(j,text=' Your Score',bg='chartreuse2',fg='black',font='Arial 20 bold').grid(row=0,column=2)
    Label(j,text=' ',bg='chartreuse2').grid(row=0,column=3)
    Label(j,text=' Computer Score',bg='chartreuse2',fg='black',font='Arial 20 bold').grid(row=0,column=4)
    Label(j,text=' ',bg='chartreuse2').grid(row=0,column=5)

   
    j.config(background='chartreuse2')
    Label(j,text=str(q[0][0]),bg='chartreuse2',font='Arial 15 italic').grid(row=1,column=0)
    Label(j,text=' ',bg='chartreuse2').grid(row=1,column=1)
    Label(j,text=str(q[0][1]),bg='chartreuse2',font='Arial 15 italic').grid(row=1,column=2)
    Label(j,text=' ',bg='chartreuse2').grid(row=1,column=3)
    Label(j,text=str(q[0][2]),bg='chartreuse2',font='Arial 15 italic').grid(row=1,column=4)
    Label(j,text=' ',bg='chartreuse2').grid(row=1,column=5)
    
    def delete():
        cur.execute("drop table rps")
        j.destroy()
    Button(j,text='Reset',bg='black',fg='white',bd=4,command=delete).grid(row=2,column=3)
    j.mainloop()
    #return i
    #print acc
    #Label(frame,text=str(i)).grid(row=0,column=0)
    #e1.delete(0,END)
    con.commit()

#root.destroy()
Button(root,text='Scoreboard',bg='tomato',height='1',width='1',command=score).grid(row=5,column=0,sticky=N+S+E+W)



root.mainloop()
