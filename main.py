# -*- coding: utf-8 -*-
import sys
import random
import requests

sys.path.insert(0, sys.path[0] + '\\proto')
sys.path.insert(0, sys.path[0] + '/proto')
from telegram_proto import *
from hebrew_proto import *
from db_proto import *


'''
BOT_MODE
0 - standart
1 - wait to diary
2 - quiz
3 - life
4 - exit
'''

BOT_MODE = 0
EXIT_MODE = False


def check_updates():
    parameters_list = telebot.get_updates()
    if EXIT_MODE:
        return 1
    if not parameters_list:
        return 0
    for parameters in parameters_list:
        # if parameters[3] != ADMIN_ID:
        #     telebot.send_text(parameters[3], "Who the fuck is you?")
        #     continue
        run_command(*parameters)


def run_command(name, from_id, cmd, author_id, date):
    global BOT_MODE
    global EXIT_MODE
    print 1

    if cmd == '/help':
        telebot.send_text(from_id, 'No help today. Sorry, %s' % name)

    if cmd == '/start':
        telebot.send_text(from_id, "Start!")
        key, keyboard = get_keyboard()
        put_user_answer(from_id, key)
        telebot.send_photo(from_id, 'words/'+key + '.png')
        telebot.send_text_with_keyboard(from_id, "_", keyboard)

    else:
        print 2
        right_answer = get_user_answer(from_id)
        print right_answer
        if right_answer:
            if right_answer == cmd.encode('utf-8'):
                telebot.send_text(from_id, "Right!")
            else:
                telebot.send_text(from_id, "False, right answer: {0}".format(right_answer))
        else:
            telebot.send_text(from_id, "Start!")

        key, keyboard = get_keyboard()
        put_user_answer(from_id, key)
        telebot.send_photo(from_id, 'words/' + key + '.png')
        telebot.send_text_with_keyboard(from_id, "_", keyboard)




    # elif BOT_MODE == 3:
    #     sqlite_add(cmd, date)
    #     telebot.send_text(from_id, "{0}: {1}".format(cmd, human_time(date)))
    #     BOT_MODE = 0
    # elif cmd[:4] == '/add':
    #     try:
    #         cmd = str(cmd)
    #     except:
    #         telebot.send_text(from_id, 'Incorrect encoding')
    #     if len(cmd.split('/')) != 4:
    #         telebot.send_text(from_id, 'Incorrect input')
    #     operation = cmd.split('/')[2]
    #     operation_date = get_time(date, cmd.split('/')[3])
    #     sqlite_add(operation, operation_date)
    #     telebot.send_text(from_id, "{0}: {1}".format(operation, human_time(operation_date)))
    #
    # elif cmd[0:5] == '/stat':
    #     if len(cmd) == 5:
    #         pass
    #     else:
    #         new_date = str(cmd).split(' ')[1]
    #         [day, month, year] = new_date.split('.')
    #         date = unix_time(int(day), int(month), int(year))
    #
    #     left, right = get_bounds(date)
    #     stat = sqlite_get_stat(left, right)
    #     if stat == '':
    #         telebot.send_text(from_id, 'No data on this day: {0}'.format(human_time(date)))
    #     else:
    #         telebot.send_text(from_id, stat)
    #
    # elif cmd == '/exit':
    #     telebot.send_text_with_keyboard(from_id, 'Shut down?', [["Yes", "No"]])
    #     BOT_MODE = 4
    #
    # elif BOT_MODE == 4 and cmd == 'Yes':
    #     telebot.send_text(from_id, 'Finish by user {0} on {1}'.format(name, telebot.host))
    #     EXIT_MODE = True
    #
    # elif cmd[0:2] == '/d' and author_id in (ADMIN_ID, PIG_ID):
    #     d = Diary()
    #     if cmd == '/d':
    #         telebot.send_text_with_keyboard(from_id, 1, [["Day"], ["Week"], ["Backlog"], ["All"]])
    #     else:
    #         op = cmd.split(' ')[1]
    #         if op == '-':
    #             task_type = int(cmd.split(' ')[2])
    #             task_id = int(cmd.split(' ')[3])
    #             print task_id, task_type
    #             d.delete_id(task_type, task_id)
    #             output = unicode(str(d.return_list(task_type)), "CP1251")
    #             telebot.send_text(from_id, output)
    #             return
    #         if op == '+':
    #             task_type = int(cmd.split(' ')[2])
    #             task = cmd.split(' ', 3)[3]
    #             d.add_line(task_type, task.encode('CP1251'))
    #             output = unicode(str(d.return_list(task_type)), "CP1251")
    #             telebot.send_text(from_id, output)
    #     BOT_MODE = 1
    #     return
    #
    # elif BOT_MODE == 1:
    #     d = Diary()
    #     if cmd == 'Day':
    #         output = unicode(str(d.return_list(0)), "CP1251")
    #         telebot.send_text(from_id, output)
    #     if cmd == 'Week':
    #         output = unicode(str(d.return_list(1)), "CP1251")
    #         telebot.send_text(from_id, output)
    #     if cmd == 'Backlog':
    #         output = unicode(str(d.return_list(2)), "CP1251")
    #         telebot.send_text(from_id, output)
    #     if cmd == 'All':
    #         output = unicode(str(d), "CP1251")
    #         telebot.send_text(from_id, output)
    #     BOT_MODE = 0
    #
    # elif cmd[0:7] == '/magnet':
    #     telebot.send_text(from_id, "Not yet")
    #     return
    #     add_torrent(cmd[8:])
    #     telebot.send_text(from_id, "Done")
    # else:
    #     log_event('No action')
    #     BOT_MODE = 0


if __name__ == "__main__":
    telebot = Telegram()
    telebot.send_text(ADMIN_ID, "Run on {0}".format(telebot.host))
    while True:
        try:
            if check_updates() != 1:
                time.sleep(telebot.Interval)
            else:
                sys.exit()
        except KeyboardInterrupt:
            print 'Interrupt by user..'
            break
        except Exception, e:
            log_event(str(e))