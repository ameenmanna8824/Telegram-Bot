x = "ameenmanna8824"
y = "3d4c4a5ea05940efabe546afd681cad9"

from Adafruit_IO import Client, Feed
aio = Client(x,y)

from telegram.ext import Updater, CommandHandler,MessageHandler, Filters 

def on(bot,update):
  chat_id = update.message.chat_id
  amn.create_data('telegram',Data(value=1))#telegram is the feed name
  bot.send_message(chat_id=chat_id,text = "LIGHT IS TURNED ON")
  
def off(bot,update):
  chat_id = update.message.chat_id
  amn.create_data('telegram',Data(value=0))#telegram is adafruit feed name
  bot.send_message(chat_id=chat_id,text ="LIGHT IS TURNED OFF")

updater = Updater('1561181436:AAEIjnS2JfEZTeeJVoahlDkVKO-o3MLujnU')

dp = updater.dispatcher #updater is object and .dispatcher is attribute
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
updater.start_polling() #updater is object and .start_polling() is method
updater.idle() #updater is object and .idle() is method
