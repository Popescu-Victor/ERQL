from typing import Final
import dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "TOKEN")

application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to ERQL!")

def handle_response(text: str) -> str:
    text = text.lower()
    rendered = text.split("$")
    response = f'Part 1 is "{rendered[0]}" and part 2 is "{rendered[1]}"'
    return response

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)


application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
application.run_polling()