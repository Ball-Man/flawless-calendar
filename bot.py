from telegram import Updater
import os

from datetime import datetime

from bot_token import Token
from calendar_utils import greg2flawless as g2f, flawless_months

updater = Updater(token=Token)
dispatcher = updater.dispatcher

def now_handler(bot, update):
	fl_today = g2f(datetime.now().date())
	text = "Today is\n  year:       %d\n  month:  %d %s\n  day:        %d\nin the flawless calendar."%(fl_today[0], fl_today[1], flawless_months[fl_today[1]], fl_today[2])
	bot.sendMessage(chat_id=update.message.chat_id, text=text)

if __name__ == "__main__":
	dispatcher.addTelegramCommandHandler("now", now_handler)
	
	# Get the port to bind to
	port = int(os.environ.get("PORT", 5000))
	# Start the updater listening on all public IPs
	updater.start_webhook("0.0.0.0", port)