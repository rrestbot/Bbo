from keep_alive import keep_alive
keep_alive()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8067847794:AAFk8_714M9CohQ6Dz-V4lYstloWTXL6hgE"
CHANNEL_ID = -1002831436891

# Optional: Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Bot চালু আছে! শুধু মেসেজ পাঠান, আমি চ্যানেলে পোস্ট করব।")

# Main Forwarding Logic
async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    hashtag = "\n\n#viral #hot #virallink"

    try:
        if msg.text:
            text = msg.text + hashtag
            sent = await context.bot.send_message(chat_id=CHANNEL_ID, text=text)

        elif msg.photo:
            caption = (msg.caption or "") + hashtag
            sent = await context.bot.send_photo(chat_id=CHANNEL_ID, photo=msg.photo[-1].file_id, caption=caption)

        elif msg.video:
            caption = (msg.caption or "") + hashtag
            sent = await context.bot.send_video(chat_id=CHANNEL_ID, video=msg.video.file_id, caption=caption)

        elif msg.document:
            caption = (msg.caption or "") + hashtag
            sent = await context.bot.send_document(chat_id=CHANNEL_ID, document=msg.document.file_id, caption=caption)

        elif msg.audio:
            caption = (msg.caption or "") + hashtag
            sent = await context.bot.send_audio(chat_id=CHANNEL_ID, audio=msg.audio.file_id, caption=caption)

        elif msg.voice:
            sent = await context.bot.send_voice(chat_id=CHANNEL_ID, voice=msg.voice.file_id, caption=hashtag)

        else:
            await msg.reply_text("❌ এই টাইপের মেসেজ সাপোর্ট করা হয় না।")
            return

        # Optional response to user
        await msg.reply_text("✅ তোমার মেসেজ  চ্যানেলে পোস্ট হয়েছে!")

    except Exception as e:
        await msg.reply_text(f"❌ Error: {str(e)}")

# Build bot app
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, forward_to_channel))

print("🚀 Bot is running...")
app.run_polling()
