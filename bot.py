from telegram import Updater
import os

from datetime import datetime

from bot_token import Token
from calendar_utils import greg2flawless as g2f, flawless_months

updater = Updater(token=Token)
dispatcher = updater.dispatcher

def now_handler(bot, update):
	fl_today = g2f(datetime.now().date())
	text = "It's the %dth day of %s(%d) %d."%(fl_today[2], flawless_months[fl_today[1]], fl_today[1], fl_today[0])
	bot.sendMessage(chat_id=update.message.chat_id, text=text)

def help_handler(bot, update):
	text = "This bot converts a gregorian date into a flawless date(a particular calendar based on regular months and years)"
	bot.sendMessage(chat_id=update.message.chat_id, text=text)
	
if __name__ == "__main__":
	dispatcher.addTelegramCommandHandler("now", now_handler)
	dispatcher.addTelegramCommandHandler("help", help_handler)
	
	# Get the port to bind to
	port = int(os.environ.get("PORT", 5000))
	# Start the updater listening on all public IPs
	updater.start_webhook("0.0.0.0", port)
