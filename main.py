import telebot
import os

# === CONFIG ===
BOT_TOKEN = "7905146360:AAF1Rx127LgEk50Pf-hVYn9WkwMUoJDPsnA"
MY_USER_ID = "1152045784"  # e.g. "123456789"

# Only these user IDs can use the bot
ALLOWED_USERS = ["5986309933", "6338350971"]

SAVE_DIR = "downloads"

# === SETUP ===
bot = telebot.TeleBot(BOT_TOKEN)
os.makedirs(SAVE_DIR, exist_ok=True)


@bot.message_handler(content_types=['document', 'photo', 'video', 'audio'])
def handle_file(message):
    user_id = str(message.from_user.id)

    # Reject unauthorized users
    if user_id not in ALLOWED_USERS:
        bot.reply_to(message, "🚫 You're not authorized to use this bot.")
        bot.send_message(
            MY_USER_ID,
            f"🚨 Unauthorized access attempt by: {message.from_user.full_name} (ID: {user_id})"
        )
        return

    try:
        # Get file ID and name
        file_id = None
        file_name = None

        if message.document:
            file_id = message.document.file_id
            file_name = message.document.file_name
        elif message.photo:
            file_id = message.photo[-1].file_id
            file_name = f"{file_id}.jpg"
        elif message.video:
            file_id = message.video.file_id
            file_name = f"{file_id}.mp4"
        elif message.audio:
            file_id = message.audio.file_id
            file_name = message.audio.file_name or f"{file_id}.mp3"

        if not file_id:
            bot.reply_to(message, "❌ Unsupported file type.")
            return

        # Download and save the file
        file_info = bot.get_file(file_id)
        downloaded = bot.download_file(file_info.file_path)
        save_path = os.path.join(SAVE_DIR, file_name)
        with open(save_path, 'wb') as f:
            f.write(downloaded)

        # Notify sender
        bot.reply_to(message,
                     f"✅ File `{file_name}` saved!",
                     parse_mode="Markdown")

        # Send the file to you
        with open(save_path, 'rb') as f:
            sender = message.from_user.username or message.from_user.first_name or "unknown"
            bot.send_document(MY_USER_ID,
                              f,
                              caption=f"📥 File from @{sender}\n📄 {file_name}")

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {e}")


# Optional: start command to get user's ID
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 f"👋 Hello, your ID is `{message.from_user.id}`",
                 parse_mode="Markdown")


print("🤖 Bot is running...")
bot.polling()
