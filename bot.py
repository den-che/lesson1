from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import get_answer
from answers import answer

def start(bot,update):
    print("Вызван /start")
    bot.sendMessage(update.message.chat_id, text = "Привет, человек!")

def talk_to_me(bot,update):
    print("Пришло сообщение : " + update.message.text)
    bot.sendMessage(update.message.chat_id, text = get_answer(update.message.text, answer))

def run_bot():
    updater = Updater("289176178:AAF9KielZHS3zEulHp_Pg8aEkf9jzNXbRN8")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler([Filters.text],talk_to_me))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()