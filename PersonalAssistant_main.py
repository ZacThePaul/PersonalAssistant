# NOTES *
# add personal stocks
# TURN THIS INTO A PERSONAL ASSISTANT

import PA_func as pf
import sqlite3
import assistant_gui

sqlite_file = 'assistant.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

pf.create_assistant()
if len(c.execute('SELECT assistant_name FROM assistant ').fetchall()) == 0:
    pf.greeting()

elif len(c.execute('SELECT assistant_name FROM assistant ').fetchall()) != 0:
    name = c.execute('SELECT assistant_name FROM assistant ').fetchall()[0][0]  # These zeroes are to remove parenthesis
    named = c.execute('SELECT named FROM assistant ').fetchall()[0]
    username = c.execute('SELECT name FROM  user').fetchall()[0][0]
    temp = pf.user_weather()
    city = c.execute('SELECT  city FROM user').fetchall()[0][0]
    gui = assistant_gui.gui(username, city, temp)

    gui()

    # print('Hi there {}, nice to see you again.'.format(username))
    # print('It looks like the temperature in your area is {} degrees right now'.format(temp))
    # if int(temp) < 40:
    #     print('little chilly, eh?')
    # elif int(temp) > 90:
    #     print('time for some AC')

# c.execute('DROP TABLE assistant')
# c.execute('DROP TABLE user')
