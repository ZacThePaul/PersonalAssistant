# NOTES *


import PA_func as pf
import sqlite3
import assistant_gui

sqlite_file = 'assistant.sqlite'
conn = sqlite3.connect(sqlite_file)  # instantiating a connection to the sqlite database
c = conn.cursor()

pf.create_assistant()  # creates the assistant table in the sqlite database if it's not already there

if len(c.execute('SELECT assistant_name FROM assistant ').fetchall()) == 0:
    assistant_gui.start_gui()  # if the assistant table is empty, it runs the greeting

elif len(c.execute('SELECT assistant_name FROM assistant ').fetchall()) != 0:
    name = c.execute('SELECT assistant_name FROM assistant ').fetchall()[0][0]  # These zeroes are to remove parenthesis
    named = c.execute('SELECT named FROM assistant ').fetchall()[0]
    username = c.execute('SELECT name FROM  user').fetchall()[0][0]
    temp = pf.user_weather()
    city = c.execute('SELECT city FROM user').fetchall()[0][0]
    #  if the assistant table is not empty, it instantiates all information in it (above)

    assistant_gui.main_gui(username, city, temp)

# c.execute('DROP TABLE assistant')
# c.execute('DROP TABLE user')
