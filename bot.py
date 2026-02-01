import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv(8508758212:AAH57JNhrIMScMfb0KM7gFeZf2wfzjievQE)
# User score storage
user_scores = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_scores[user_id] = 0
    await update.message.reply_text("🔥 Welcome to Piru Tap Game!\n\nTap karne ke liye /tap likho!")

async def tap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if user_id not in user_scores:
        user_scores[user_id] = 0

    user_scores[user_id] += 1
    score = user_scores[user_id]

    await update.message.reply_text(f"👆 Tap registered!\nYour score: {score}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tap", tap))

    print("Piru Bot Running...")
    app.run_polling()
