import telebot

print("Hello World!")

print("bot starting")
bot = telebot.TeleBot('5012237406:AAGaFxMBx2p9GmuYx5HsCagAeAtkrTXJ-po')

me = bot.get_me()

@bot.message_handler(content_types=["text"])
def handle_text_messages(message):
     if(message.text == 'привіт'):
         bot.send_message(message.chat.id, "hi! my name is " + me.full_name)
     if(message.text == 'Як тебе звати?'):
         bot.send_message(message.chat.id, "Привіт, мене звати Іван")
     

bot.polling() 


    #if(message.text == "hi" ):
       # bot.send_message(message.chat.id, "привіт")
    #if(message.text == "/start"):


