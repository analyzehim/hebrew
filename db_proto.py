import sqlite3
import datetime
import time
con = sqlite3.connect('hebrew_stat.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS `Hebrew`
            (`id` VARCHAR(100) PRIMARY KEY NOT NULL ,
            `name` VARCHAR(100),
            `right` INTEGER,
            `false` INTEGER);''')


user_dict = {}

def put_user_answer(from_id, right_answer):
    try:
        user_dict[from_id] = right_answer
    except:
        pass
    return

def add_user(from_id, name):
    cur.execute('''SELECT * FROM Hebrew Where id = {0}'''.format(from_id))
    if cur.fetchone():
        return True
    else:
        cur.execute('''INSERT INTO Hebrew(id, name, right, false) VALUES ('{0}','{1}','0','0')'''.format(from_id, name))
        return True


def get_user_answer(from_id):
    try:
        return user_dict[from_id]
    except:
        return False

def add_user_info(from_id, answer):
    if answer == 1:
        cur.execute('''UPDATE Hebrew SET right = right + 1 WHERE id={0}'''.format(from_id))
    else:
        cur.execute('''UPDATE Hebrew SET false = false + 1 WHERE id={0}'''.format(from_id))
    con.commit()
    return

add_user(1,"test")
add_user_info(1, 0)

