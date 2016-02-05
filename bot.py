from telegram import Updater
import os

from bot_token import Token

updater = Updater(token=Token)
dispatcher = updater.dispatcher

def echo(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="' %s '"%update.message.text)

if __name__ == "__main__":
	dispatcher.addTelegramCommandHandler("echo", echo)
	
	# Get the port to bind to
	port = int(os.environ.get("PORT", 5000))
	# Start the updater listening on all public IPs
	updater.start_webhook("0.0.0.0", port)