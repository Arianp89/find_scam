import telebot
import time
import threading
from config import API_TOKEN
from DML import add_customer_black_list,came_customer_black_list
from DQL import get_black_list_list,get_customer_black,check_black_list


bot=telebot.TeleBot(API_TOKEN)

#add your message in line 27,31

find_scam_data=dict()     #{cid:[len,time],...}
def find_scam(cid,maximum_time,maximum_watch):  
    global find_scam_data
    now = time.time()
    if cid not in find_scam_data:
        find_scam_data[cid]=[0,time.time()]
    if now-find_scam_data[cid][1] < maximum_time:
        find_scam_data[cid][0] += 1
        print(find_scam_data[cid][0])
    if find_scam_data[cid][0]%maximum_watch==0:
        data=get_customer_black(cid)

        if cid not in get_black_list_list():
            add_customer_black_list(cid,time.time())
            bot.send_message(cid,'level one 1')
        elif data['STAGE']==1 and data['DON']=='yes':

            add_customer_black_list(cid,time.time(),2)
            bot.send_message(cid,'level 2')
        elif data['STAGE']==2 and data['DON']=='yes':
            add_customer_black_list(cid,time.time(),2)
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
    if check_black_list(cid) ==False:
        bot.send_message(cid,message.text)
    else:
        # it better do not answer
        pass



def check_find_scam_status(warring_1=60*15,warring_2=3600,sleep_time=60):  #warring_1=15 minute,warring_2=one hour,sleep_time=one minute
    while True:
        now = time.time()
        for cid in get_black_list_list():
            data=get_customer_black(cid) #get customer data from black list table 

            if data['STAGE']==1 and data['DON']=='no':
                if int(now-data['TIME'] ) > warring_1:
                    came_customer_black_list(cid)

            elif data['STAGE']==2 and data['DON']=='no':
                if int(now-data['TIME']) > warring_2:
                    came_customer_black_list(cid)
            
        time.sleep(sleep_time)
t2=threading.Thread(target=check_find_scam_status,args=())#one time in a day check for users that their 100 days is coming to end and send message to admin to check if they have registered project or not
t2.start() #if you like can add arg

print('bot_runnig')
bot.infinity_polling()