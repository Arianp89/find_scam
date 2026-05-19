import telebot
import time
from config import API_TOKEN
from DML import add_customer_black_list


bot=telebot.TeleBot(API_TOKEN)



find_scam_data=dict()     #{cid:[len,time],...}
def find_scam(cid,maximum_time,maximum_watch):  
    global find_scam_data
    now = time.time()
    if cid not in find_scam_data:
        find_scam_data[cid]=[0,time.time()]
    if now-find_scam_data[cid][1] < maximum_time:
        find_scam_data[cid][0] += 1
        print(find_scam_data[cid][0])
    if find_scam_data[cid][0] == maximum_watch:
        add_customer_black_list(cid)
    find_scam_data[cid][1]=time.time()






def listener(messages):
    for m in messages:
        # print(m)
        find_scam(m.chat.id,3,5)
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