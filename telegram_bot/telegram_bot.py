from typing import Final
import dotenv
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters


def start_telegram_bot():

    TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "TOKEN")

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("I am accute bot!")

    async def first_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("This is the first message!")

    def handle_response(text: str) -> str:
        text = text.lower()
        print(text)  
        return text

    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message_text = update.message.text 
        handle_response(message_text)        
        
    if __name__ == "__main__":
        app = Application.builder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        print("Bot is running...")
        app.run_polling()