# NOTES **
# I want to add the ability to choose your news provider or choose multiple or all if so desired
# if search comes up empty, suggest similar words to user (synonyms.com)
# add the ability for Wikipedia pages on relevant subjects to the user search
# add the ability for the user to choose world or US news
# add personal stocks
# TURN THIS INTO A PERSONAL ASSISTANT

import PA_func as pf
import PA_var as pv
import time as t
import sqlite3

sqlite_file = 'assistant.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

initiated = 0


def greeting():
        assistant_name = ''
        print('...')
        t.sleep(2)
        initialize = ['Initiating startup sequence', ' ...', ' ...']
        for i in initialize:
            print(i, end='', flush=True)
            t.sleep(1)
        # t.sleep(1)
        # print('\n...')
        # t.sleep(1)
        # print('\n \n|| Welcome to your Personal Assistant ||')
        # print('I am a Python program written by ZacThePaul. If you have questions about my mind, at any prompt please enter \'iMind\'.')
        # print('You will be given a link to Github where my brains are stored!')
        # print('\nPlease take some time to chat with me, so I can get to know you.')
        # t.sleep(1)
        assistant_name += input('First, let\'s give me a name. What is my name? > ')
        # pf.create_assistant()
        pf.name_assistant(name=assistant_name)
        t.sleep(2)
        print('...')
        t.sleep(2)
        print('{}.. What an excellent name! I once knew a {}.\n'.format(assistant_name, assistant_name))
        user_name = input('What name do you go by?')
        t.sleep(.5)
        print(user_name, 'got it.')
        user_dob = input('What is your Date of Birth? (yyyy-mm-dd)')
        cuser_dob = pf.birthday(user_dob)
        bdaymonth = pf.bdayformat(cuser_dob)
        user_age = pf.user_age(cuser_dob)
        print('Okay you were born in', bdaymonth, 'of', cuser_dob[2], ', which makes you {} years old'.format(int(user_age)))
        pf.create_user()
        pf.name_user(user_name, user_dob)
        if int(user_age) == 23:
            print('~~~~~~~~Nobody likes you when you\'re 23~~~~~~~')





pf.create_assistant()
if len(c.execute('SELECT assistant_name FROM assistant ').fetchall()) == 0:
    greeting()
elif len(c.execute('SELECT assistant_name FROM assistant ').fetchall()) != 0:
    name = c.execute('SELECT assistant_name FROM assistant ').fetchall()[0][0]
    named = c.execute('SELECT named FROM assistant ').fetchall()[0]
    username = c.execute('SELECT name FROM  user').fetchall()[0][0]

    print('Hi there {}, nice to see you again.'.format(username))
    #print('The weather for today is going to be xxxxxx')

# c.execute('DROP TABLE assistant')
# c.execute('DROP TABLE user')
