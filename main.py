import telebot
import time
from DML import add_customer_black_list

API_TOKEN=""
telebot.apihelper.API_URL = 'http://tapi.bale.ai/bot{0}/{1}'
bot=telebot.TeleBot(API_TOKEN)



checks_time_num=dict()
def find_scam(cid):
    global checks_time_num
    now = time.time()
    if id not in checks_time_num:
        checks_time_num[cid]=[0,time.time()]
    if now-checks_time_num[cid][1] < 5:
        checks_time_num[cid][0] += 1
    if checks_time_num[cid][0] == 5+1:
        add_customer_black_list(cid)
    checks_time_num[id][1]=time.time()




def listener(messages):
    for m in messages:
        # print(m)
        find_scam(m.chat.id)
        register_user(m.chat.id, m.chat.first_name)
        if m.content_type == 'text':
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: {m.text}")
            logging.info(f"{m.chat.first_name} [{str(m.chat.id)}]: {m.text}")
        elif m.content_type == 'photo':
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: New photo recieved")
            logging.info(f"{m.chat.first_name} [{str(m.chat.id)}]: New photo recieved")
        elif m.content_type == 'document':
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: New document recieved")
            logging.info(f"{m.chat.first_name} [{str(m.chat.id)}]: New document recieved")
        elif m.content_type == 'voice':
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: New voice recieved")
            logging.info(f"{m.chat.first_name} [{str(m.chat.id)}]: New voice recieved")
        if check_black_list(m.chat.id)==False:
            print('it not in black list')
bot.set_update_listener(listener)  
