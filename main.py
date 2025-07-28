import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8333899200:AAHuUXozAUEPNwg5pg7HFP6Z8oS0KN16MFk"  # Replace this with your real token

async def btcd_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.coingecko.com/api/v3/global"
    response = requests.get(url).json()
    dominance = response["data"]["market_cap_percentage"]["btc"]
    message = f"📊 Bitcoin Dominance: {dominance:.2f}%"
    await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("btcd", btcd_command))

print("Bot is running...")
app.run_polling()
