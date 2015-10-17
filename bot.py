# -*- coding: utf-8 -*-
import telegram
import random
cgame={}
bot = telegram.Bot(token='')
updates = bot.getUpdates()
if len(updates)>0:
    LAST_UPDATE_ID =updates[-1]['update_id']
else:
    LAST_UPDATE_ID=0

f=open('idlast.txt','w')
while 1:
    for j in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        mes_bot=str(j.message.text).lower()
        game_id=j.message.chat.id
        if game_id in cgame.keys() :
            if str(j.message.text).isdigit():
                chislo=int(j.message.text)
                if chislo>cgame[game_id]:
                    bot.sendChatAction(chat_id=game_id,action='typing')
                    bot.sendMessage(chat_id=game_id,text='Less')
                else:
                    if chislo<cgame[game_id]:
                        bot.sendChatAction(chat_id=game_id,action='typing')
                        bot.sendMessage(chat_id=game_id,text='More')
                    else:
                        bot.sendMessage(chat_id=game_id,text='Yes sir,you win!')
                        bot.sendChatAction(chat_id=game_id,action='typing')
                        bot.sendSticker(chat_id=game_id,sticker='BQADAgADQAADyIsGAAGMQCvHaYLU_AI')
                        del cgame[game_id]
            else:
                if('/stop' not in mes_bot) and ('/start' not in mes_bot):
                    bot.sendMessage(chat_id=game_id,text='Only digit')
        if 'привет' in mes_bot:
            bot.sendMessage(chat_id=game_id,text='Hi,command list:')
            bot.sendMessage(chat_id=game_id,text='/start - start new game')
            bot.sendMessage(chat_id=game_id,text='/stop stop current game')
        if '/start' in mes_bot:
            if game_id not in cgame.keys():
                bot.sendMessage(chat_id=game_id,text='Let\'s play game')
                bot.sendChatAction(chat_id=game_id,action='typing')
                bot.sendMessage(chat_id=game_id,text='I thinked of a number between 1 and 100')
                cgame[game_id]=random.randint(1,100)
                print('user:',game_id,'connect')
            else:
                bot.sendMessage(chat_id=game_id,text='You already play game')
        if '/stop' in mes_bot:
            if game_id in cgame.keys():
                del cgame[game_id]
                bot.sendMessage(chat_id=game_id,text='Current game end')
            else:
                bot.sendMessage(chat_id=game_id,text='You dont play now')
        LAST_UPDATE_ID = j.update_id + 1
        f.write(str(LAST_UPDATE_ID))
f.close()
