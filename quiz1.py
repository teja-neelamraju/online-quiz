#This code create a Online quiz which can connects with remote database over XAMPP
#or on same machine.This randomly display questions from the questions in database
#and store the final result of participant in database with his/her registration ID
import tkinter as tk
from tkinter import messagebox
import sqlite3 as sq
import random
global count,qs,one,two,three,four,qnum
qnum=1
count=0
class gui:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root['bg']='#F0F4C3'
        self.root.resizable(False, False)
        self.t = tk.StringVar()
        self.t.set("00:00")
        self.lb = tk.Label(self.root, textvariable=self.t,bg='#F0F4C3',fg='#9E9D24')
        self.lb.config(font=("Courier 40 bold"))
        self.start()
        self.lb.place(x=860, y=150)
        self.f=tk.Frame(self.root,bg='#F0F4C3')
        self.f3=tk.Frame(self.root,bg='#F0F4C3')
        self.f.pack(side='top')
        self.v1=tk.StringVar()
        self.v1.set(None)
        self.logo = tk.PhotoImage(file="")
        self.lab1=tk.Label(self.f,text='Online-Quiz',font="Times 20 bold",fg='green',bg='#F0F4C3')
        self.lab2=tk.Label(self.f,text="Name of College",fg='green',font="Times 20 bold",bg='#F0F4C3')
        self.lab1.pack(side='top')
        self.lab2.pack(side='top')
        self.dum=tk.Label(self.root)
        self.dum.pack()
        self.c=tk.Canvas(self.root,height=5,width=self.root.winfo_screenwidth(),bg='#F0F4C3')
        self.co=0,5,self.root.winfo_screenwidth(),5
        self.c.create_line(self.co,fill='black',width=2)
        self.c.pack()
        self.c=tk.Canvas(self.root,height=125,width=self.root.winfo_screenwidth(),bg='#E0E0E0')
        self.c.pack(side='bottom')
        self.opt1 = tk.Frame(self.f3,bg='#F0F4C3')
        self.opt2 = tk.Frame(self.f3,bg='#F0F4C3')
        self.opt3 = tk.Frame(self.f3,bg='#F0F4C3')
        self.opt4 = tk.Frame(self.f3,bg='#F0F4C3')
        self.qid = tk.Frame(self.f3,bg='#F0F4C3')
        self.connection=sq.connect('table.db')#creating a database with 7 columns
        self.cur=self.connection.cursor()#namely qid,question,4columns and correct answer
        self.cur.execute("""select qid from quiz where qid=1""")
        self.ans= self.cur.fetchall()
        self.num=tk.Label(self.qid,text=self.ans,font="Times 20  bold",bg='#F0F4C3',fg='#AFB42B')
        self.num.pack(side='left')
        self.qid.pack(side='top')
        self.cur.execute("""select question from quiz where qid=1""")
        self.ans = self.cur.fetchone()
        self.qs = tk.Label(self.qid, text='.  '+self.ans[0], font="Times 20 bold",bg='#F0F4C3',fg='#AFB42B')
        self.qs.pack(side='right')
        self.qid.pack(side='top')
        self.cur.execute("""select opt1 from quiz where qid=1""")
        self.ans = self.cur.fetchall()
        self.one = tk.Radiobutton(self.opt1, text=self.ans, font="Times 20 bold",pady=20,value='one',variable=self.v1,bg='#F0F4C3')
        self.one.pack(side='right')
        self.opt1.pack(side='top')
        self.cur.execute("""select opt2 from quiz where qid=1""")
        self.ans = self.cur.fetchall()
        self.two = tk.Radiobutton(self.opt2, text=self.ans, font="Times 20 bold",value='two',variable=self.v1,bg='#F0F4C3')
        self.two.pack(side='right')
        self.opt2.pack(side='top')
        self.cur.execute("""select opt3 from quiz where qid=1""")
        self.ans = self.cur.fetchall()
        self.three = tk.Radiobutton(self.opt3, text=self.ans, font="Times 20 bold",pady=20,value='three',variable=self.v1,bg='#F0F4C3')
        self.three.pack(side='left')
        self.opt3.pack(side='top')
        self.three.deselect()
        self.cur.execute("""select opt4 from quiz where qid=1""")
        self.ans = self.cur.fetchall()
        self.four = tk.Radiobutton(self.opt4, text=self.ans, font="Times 20 bold",value='four',variable=self.v1,bg='#F0F4C3')
        self.four.pack(side='left')
        self.opt4.pack(side='top')
        self.f3.place(x=250,y=130)
        self.next=tk.Button(self.root,text='submit',font='times 20 italic',highlightcolor='#1B5E20',relief=tk.FLAT,bg='#F0F4C3')
        self.next.place(x=260,y=430)
        self.c=tk.Canvas(self.root,height=5,width=self.root.winfo_screenwidth())
        self.co=225,755,1070,755
        self.c.create_line(self.co,fill='black',width=3)
        self.c.pack(side='bottom')
        tk.mainloop()

    def reset(self):
        global count
        count = 1
        self.t.set('00:00')

    def start(self):
        global count
        count = 0
        self.start_timer()

    def start_timer(self):  #creating a timer
        global count
        self.timer()

    '''def stop(self):
        global count
        count=1'''

    def timer(self):
        global count
        if (count == 0):
            self.d = str(self.t.get())
            m, s = map(int, self.d.split(":"))

            # h = int(h)
            m = int(m)
            s = int(s)
            if (s < 59):
                s += 1
            elif (s == 59):
                s = 0
                if (m < 31):
                    m += 1
            if (m < 10):
                m = str(0) + str(m)
            else:
                m = str(m)
            if (s < 10):
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = m + ":" + s
            self.t.set(self.d)
            if (count == 0):
                self.root.after(1000,self.start_timer)
x=gui()
