#!/usr/bin/python3
import os;
import telebot
import threading

print("Content-Type: text/html\n\n")

print("student_001_bot starting")
bot = telebot.TeleBot('5030399888:AAFHeK9JBNhLHbeBxNnbHOgfifyiNAtuZEY')

@bot.message_handler(content_types=["text"])
def repeat_all(message):
    bot.send_message(message.chat.id, 'привіт, я новий бот')
    
print("student_001_bot started")

def listener(messages):
    for m in messages:
        print(str(m))

bot.set_update_listener(listener)
bot.infinity_polling()


