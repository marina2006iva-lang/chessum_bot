import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8925386870:AAFnPtKpPVI63sPl5rdQfHuYgJ7ZHpdwKt8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("♟️ Бот работает! Поздравляю!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
