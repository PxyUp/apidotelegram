__author__ = 'pxy'
# -*- coding: utf-8 -*-
import telegram
import random
cgame={}
bot = telegram.Bot(token='token')
updates = bot.getUpdates()
if len(updates)>0:
    LAST_UPDATE_ID =updates[-1]['update_id']
else:
    LAST_UPDATE_ID=0

f=open('idlast.txt','w')
while 1:
    for j in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        mes_bot=str(j.message.text).lower()


        if j.message.chat.id in cgame.keys() :
            if str(j.message.text).isdigit():
                chislo=int(j.message.text)
                if chislo>cgame[j.message.chat.id]:
                    bot.sendChatAction(chat_id=j.message.chat.id,action='typing')
                    bot.sendMessage(chat_id=j.message.chat.id,text='Less')
                else:
                    if chislo<cgame[j.message.chat.id]:
                        bot.sendChatAction(chat_id=j.message.chat.id,action='typing')
                        bot.sendMessage(chat_id=j.message.chat.id,text='More')
                    else:
                        bot.sendMessage(chat_id=j.message.chat.id,text='Yes sir,you win!')
                        bot.sendChatAction(chat_id=j.message.chat.id,action='typing')
                        bot.sendSticker(chat_id=j.message.chat.id,sticker='BQADAgADQAADyIsGAAGMQCvHaYLU_AI')
                        del cgame[j.message.chat.id]
            else:
                if('/stop' not in mes_bot) and ('/start' not in mes_bot):
                    bot.sendMessage(chat_id=j.message.chat.id,text='Only digit')
        if 'привет' in mes_bot:
            bot.sendMessage(chat_id=j.message.chat.id,text='Hi,command list:')
            bot.sendMessage(chat_id=j.message.chat.id,text='/start - start new game')
            bot.sendMessage(chat_id=j.message.chat.id,text='/stop stop current game')
        if '/start' in mes_bot:
            if j.message.chat.id not in cgame.keys():
                bot.sendMessage(chat_id=j.message.chat.id,text='Let\'s play game')
                bot.sendChatAction(chat_id=j.message.chat.id,action='typing')
                bot.sendMessage(chat_id=j.message.chat.id,text='I thinked of a number between 1 and 100')
                cgame[j.message.chat.id]=random.randint(1,100)
                print('user:',j.message.chat.id,'connect')
            else:
                bot.sendMessage(chat_id=j.message.chat.id,text='You already play game')
        if '/stop' in mes_bot:
            if j.message.chat.id in cgame.keys():
                del cgame[j.message.chat.id]
                bot.sendMessage(chat_id=j.message.chat.id,text='Current game end')
            else:
                bot.sendMessage(chat_id=j.message.chat.id,text='You dont play now')
        LAST_UPDATE_ID = j.update_id + 1
        f.write(str(LAST_UPDATE_ID))
f.close()