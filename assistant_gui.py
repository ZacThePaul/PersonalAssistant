from tkinter import *
import random
import PA_func as pf
import sqlite3
import datetime
import Expressions as xp

sqlite_file = 'assistant.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
now = datetime.datetime.now()


def start_gui():
    master = Tk()
    master.geometry('450x400')
    master.title('Personal Assistant')
    dob_var = StringVar()
    dob_var.set('yyyy-mm-dd')

    def submit_info():
        all_good_count = 0  # checks to see if all boxes are good to be submitted (must equal 6)

        pf.create_assistant()  # creates assistant table
        pf.create_user()  # creates user table

        assist_name = assistant_entry.get()  # grabs the name the user input
        if len(assist_name) > 0:
            pf.name_assistant(assist_name)
            all_good_count += 1  # checks if there is input in the field and inserts the name into the table
        else:
            assistant_entry.configure({'background': 'orange red'})  # if there is no input, field turns red

        use_name = user_name_entry.get()  # names the user
        if len(use_name) > 0:
            pf.name_user(use_name)
            all_good_count += 1  # checks if there is input in the field and inserts the name into the table
        else:
            user_name_entry.configure({'background': 'orange red'})

        use_dob = user_dob_entry.get()
        if len(use_dob) > 0:
            pf.user_dob(use_dob)
            all_good_count += 1
        else:
            user_dob_entry.configure({'background': 'orange red'})

        use_city = user_city_entry.get()
        if len(use_city) > 0:
            pf.locate_user_city(use_city)
            all_good_count += 1
        else:
            user_city_entry.configure({'background': 'orange red'})

        use_state = user_state_entry.get()
        if len(use_state) > 0:
            pf.locate_user_state(use_state)
            all_good_count += 1
        else:
            user_state_entry.configure({'background': 'orange red'})

        use_zip = user_zip_entry.get()
        if len(use_zip) > 0:
            pf.locate_user_zip(use_zip)
            all_good_count += 1
        else:
            user_zip_entry.configure({'background': 'orange red'})

        if all_good_count == 6:
            master.quit()  # if all field are filled out satisfactorily, the program quits


    greet = Message(master, text='Welcome to your personal assistant!'
                                 '\n Please fill out the following areas.',
                    bg='brown', font=(None, 10), width=250, anchor=CENTER
                    )
    assistant_name = Label(master, text='Assistant\'s name: ')
    assistant_entry = Entry(master)

    user_name = Label(master, text='User\'s name: ')
    user_name_entry = Entry(master)

    user_dob = Label(master, text='User\'s date of birth: ')
    user_dob_entry = Entry(master, textvariable=dob_var)

    user_city = Label(master, text='User city: ')
    user_city_entry = Entry(master)

    user_state = Label(master, text='User state/province: ')
    user_state_entry = Entry(master)

    user_zip = Label(master, text='User zip-code: ')
    user_zip_entry = Entry(master)

    sumbit_button = Button(master, text='Submit', command=submit_info)

    ##

    greet.grid(row=0, column=1)

    assistant_name.grid(row=1, column=0, sticky=W)
    assistant_entry.grid(row=1, column=1, sticky=W)

    user_name.grid(row=2, column=0, sticky=W)
    user_name_entry.grid(row=2, column=1, sticky=W)

    user_dob.grid(row=3, column=0, sticky=W)
    user_dob_entry.grid(row=3, column=1, sticky=W)

    user_city.grid(row=4, column=0, sticky=W)
    user_city_entry.grid(row=4, column=1, sticky=W)

    user_state.grid(row=5, column=0, sticky=W)
    user_state_entry.grid(row=5, column=1, sticky=W)

    user_zip.grid(row=6, column=0, sticky=W)
    user_zip_entry.grid(row=6, column=1, sticky=W)

    sumbit_button.grid(row=8, column=2)

    mainloop()


def main_gui(username, city, temp):
    master = Tk()
    master.geometry('1050x800')
    master.title('Personal Assistant')
    # var = StringVar()

    # def printer():
    #     x = t.get()  # use this function to update user info. use sql commands through this
    #     print(x)

    ctime = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    cdate = Label(master, text=ctime, font=(None, 7), bg ='brown', width=10)
    hello = Message(master, text="Hi {}, the temperature in {} is"
                    " {}°ᶠ.\n{}".format(username, city, temp, random.choice(xp.temp_less_than_40) if int(temp) < 45 else random.choice(xp.temp_above_40)), font=(None, 20), bg='brown', width=333)
    sports = Message(master, text='sportssssssssssssssssssssssssssssssssssssssssssssssssss', font=(None, 20), bg='blue', width=333)
    stocks = Message(master, text='stockssssssssssssssssssssssssssssssssssssssssssss', font=(None, 20), bg='pink', width=333)

    hello.grid(row=0, column=2)
    sports.grid(row=0, column=1)
    stocks.grid(row=0, column=3)


    mainloop()

