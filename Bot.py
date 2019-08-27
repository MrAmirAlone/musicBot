#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import re
import time
from time import sleep
import sys
import json
import os
import logging
import subprocess
import re
import requests
import random
from random import randint
import base64
import urllib
from urllib import urlretrieve as dw
import urllib2
import redis
import string
import math
import requests as req
reload(sys)
sys.setdefaultencoding("utf-8")
TOKEN = '863246970:AAEulUP76XSdw0b0RTj0QSH1x7m3Ni63ijU'
bot = telebot.TeleBot(TOKEN)
redis = redis.StrictRedis(host='127.0.0.1', port=6379, db=1, decode_responses=True)

f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n \033[01;34m Bot Username: {} \033[0m".format(bot.get_me().username)
i = "\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n \033[01;31m Bot Is Online Now! \033[0m"
print(f + u + i + c)
#######################################################################################

channel = -1001348292872

def random_char(y):
     return ''.join(random.choice(string.ascii_letters) for x in range(y))

#######################################################################################

@bot.message_handler(content_types=['text'])
def MusicBot(m):
        if m.from_user.id == 223870582 or m.from_user.id == 274081889:
                text = m.text
                if m.text == '/start':
                        startmsg = "ربات آماده کاره😃"
                        bot.send_message(m.chat.id,startmsg)
                elif re.match('(http|https)://.*.(mp3)$',text):
                        Mname = random_char(5)
                        dw(text,'./Music/'+str(Mname)+'-Music.mp3')
                        Kinline = types.InlineKeyboardMarkup()
                        Tsend = types.InlineKeyboardButton('بفرس😉',callback_data="sendM:"+str(Mname))
                        Kinline.add(Tsend)
                        C_send = types.InlineKeyboardButton('همینجا بفرس🤟',callback_data="sendMC:"+str(Mname))
                        Kinline.add(C_send)
                        C = types.InlineKeyboardButton('نفرس❌',callback_data="Cansel")
                        Kinline.add(C)
                        bot.send_message(m.chat.id,"فایل با فرمت *MP3* دانلود شد\nآیا مایلید به کانال ارسال شود؟",parse_mode='Markdown',reply_markup=Kinline)
                elif re.match('(http|https)://.*.(mp4)$',text):
                        Vname = random_char(5)
                        dw(text,'./Music/'+str(Vname)+'-Music.mp4')
                        Kinline = types.InlineKeyboardMarkup()
                        T_send = types.InlineKeyboardButton('بفرس😉',callback_data="sendV:"+str(Vname))
                        Kinline.add(T_send)
                        C_send = types.InlineKeyboardButton('همینجا بفرس🤟',callback_data="sendVC:"+str(Vname))
                        Kinline.add(C_send)
                        C = types.InlineKeyboardButton('نفرس❌',callback_data="Cansel")
                        Kinline.add(C)
                        bot.send_message(m.chat.id,"فایل با فرمت *MP4* دانلود شد\nآیا مایلید به کانال ارسال شود؟",parse_mode='Markdown',reply_markup=Kinline)

#######################################################################################

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

        if re.match('(sendM:).*',call.data):
                music = call.data.replace('sendM:','')
                bot.send_audio(channel, open('./Music/'+str(music)+'-Music.mp3'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="با موفقیت ارسال شد✅")
        if re.match('(sendV:).*',call.data):
                video = call.data.replace('sendV:','')
                bot.send_video(channel, open('./Music/'+str(video)+'-Music.mp4'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="با موفقیت ارسال شد✅")
        if call.data == "Cansel":
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اوکیه کنسل شد")
        if re.match('(sendMC:).*',call.data):
                music = call.data.replace('sendMC:','')
                bot.send_audio(call.message.chat.id, open('./Music/'+str(music)+'-Music.mp3'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="☝️")
        if re.match('(sendVC:).*',call.data):
                music = call.data.replace('sendVC:','')
                bot.send_video(call.message.chat.id, open('./Music/'+str(video)+'-Music.mp4'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="☝️")
#######################################################################################

bot.polling(True)
