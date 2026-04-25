import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = (8216472814:AAEdb-q43nxbPVEG879z-YpTphfz2KRjQ2o)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text("Ты написал: " + text)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

print("Bot started")
app.run_polling()
