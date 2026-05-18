import telebot
import time
from config import API_TOKEN
from DML import add_customer_black_list


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
        if m.content_type == 'text':
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: {m.text}")
        elif m.content_type == 'photo':
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: New photo recieved")
        elif m.content_type == 'document':
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: New document recieved")
        elif m.content_type == 'voice':
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: New voice recieved")
bot.set_update_listener(listener)  




@bot.message_handler(func = lambda message: True)
def all_message_handler(message):
    cid=message.chat.id
    bot.send_message(cid,message.text)



print('bot_runnig')
bot.infinity_polling()