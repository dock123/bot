import telebot

TOKEN="980200600:AAE9GbfMjQcqtRWBG3VV_2PYgMixKydJVXA"
bot=telebot.Telebot(TOKEN)

@bot.message_handler(content_types=["text"])
def handler_text(message):
    if message.text=="/help":
        bot.send_message(message.from_user.id,"/money\n"
                                              "/money/(usd,eur)")

bot.polling(none_stop=True)
