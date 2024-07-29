import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define a function to handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        message = update.message
        logger.info("Received message: %s", message.text)
        if message.text and message.text.lower().startswith("powered by telefeed"):
            try:
                await context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
                logger.info("Deleted message: %s", message.text)
            except Exception as e:
                logger.error("Failed to delete message: %s", e)
    elif update.channel_post:
        message = update.channel_post
        logger.info("Received channel post: %s", message.text)
        if message.text and message.text.lower().startswith("powered by telefeed"):
            try:
                await context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
                logger.info("Deleted channel post: %s", message.text)
            except Exception as e:
                logger.error("Failed to delete channel post: %s", e)
    else:
        logger.info("Received non-message update")



def main() -> None:
    # Replace 'YOUR_TOKEN_HERE' with your bot's API token
    application = ApplicationBuilder().token("7256509756:AAG3AtCWZ5nMyAgNLTIvlOZLRpRplgNufss").build()

    # Add a handler for all messages
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    application.run_polling()

if __name__ == '__main__':
    main()