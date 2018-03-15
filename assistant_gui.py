from tkinter import *
import PA_func as pf
import sqlite3
import datetime

sqlite_file = 'assistant.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
now = datetime.datetime.now()

def gui(username, city, temp):
    master = Tk()
    master.geometry('1000x800')
    master.title('Personal Assistant')
    # var = StringVar()

    # def printer():
    #     x = t.get()  # use this function to update user info. use sql commands through this
    #     print(x)

    ctime = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    cdate = Label(master, text=ctime, font=(None, 7), bg ='brown', width=10)
    hello = Message(master, text="Hi {}, the temperature in {} is {}°ᶠ.\n{}".format(username, city, temp, "Make sure to button up!" if int(temp) < 45 else "Beautiful weather, enjoy your day!"), font=(None, 20), bg='brown', width=333)
    sports = Message(master, text='sportssssssssssssssssssssssssssssssssssssssssssssssssss', font=(None, 20), bg='blue', width=333)
    stocks = Message(master, text='stockssssssssssssssssssssssssssssssssssssssssssss', font=(None, 20), bg='pink', width=333)
    # b = Button(master, text='Stocks', height="2", width="15", bg="red", command=printer)
    #
    # t = Entry(master, textvariable=var)
    hello.grid(row=0, column=2)
    # if int(temp) > 40:
    #     cdate.grid(row=1, column=1)
    sports.grid(row=0, column=1)
    stocks.grid(row=0, column=3)
    # t.pack(side="left")
    # b.pack(side="left")

    mainloop()

