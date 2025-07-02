from keep_alive import keep_alive
keep_alive()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8067847794:AAFk8_714M9CohQ6Dz-V4lYstloWTXL6hgE"
CHANNEL_ID = -1002831436891

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ বট চালু হয়েছে! যেকোনো মেসেজ (লেখা, ছবি, ভিডিও) পাঠাও, আমি চ্যানেলে শেয়ার করবো।")

async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg.text:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=msg.text)
    elif msg.photo:
        await context.bot.send_photo(chat_id=CHANNEL_ID, photo=msg.photo[-1].file_id, caption=msg.caption or "")
    elif msg.video:
        await context.bot.send_video(chat_id=CHANNEL_ID, video=msg.video.file_id, caption=msg.caption or "")
    elif msg.document:
        await context.bot.send_document(chat_id=CHANNEL_ID, document=msg.document.file_id, caption=msg.caption or "")
    elif msg.audio:
        await context.bot.send_audio(chat_id=CHANNEL_ID, audio=msg.audio.file_id, caption=msg.caption or "")
    elif msg.voice:
        await context.bot.send_voice(chat_id=CHANNEL_ID, voice=msg.voice.file_id, caption=msg.caption or "")
    else:
        await update.message.reply_text("❌ এই ধরনের মেসেজ চ্যানেলে পাঠানো যাচ্ছে না।")

    await update.message.reply_text("✅ তোমার মেসেজ চ্যানেলে পাঠানো হয়েছে!")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, forward_to_channel))  # সব ধরনের মেসেজ ধরছে

print("Bot is running...")
app.run_polling()
