# 📁 Telegram File Saver Bot

This is a simple Telegram bot built using Python and [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI). It allows **specific authorized users** to upload files (documents, photos, videos, and audio), which are then saved locally on the server. The bot also forwards a copy of the uploaded file to the bot owner.

---

## 🚀 Features

- Accepts documents, images, videos, and audio files
- Only allows pre-approved users to upload files
- Saves uploaded files to a local `downloads/` directory
- Sends file notifications and content to the bot owner
- Logs unauthorized access attempts

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/telegram-file-saver-bot.git
cd telegram-file-saver-bot
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pyTelegramBotAPI python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add:

```env
BOT_TOKEN=your_telegram_bot_token
MY_USER_ID=your_telegram_user_id
ALLOWED_USERS=12345678,98765432
```

> 💡 Use comma-separated user IDs for `ALLOWED_USERS`.

Also, make sure to add `.env` to your `.gitignore` file:

```bash
echo ".env" >> .gitignore
```

### 4. Run the Bot

```bash
python bot.py
```

You should see:

```
✅ Bot is up and listening for uploads...
```

---

## ✉️ Usage

- Send any **document**, **photo**, **video**, or **audio** to the bot.
- If you're authorized, your file will be saved in the `downloads/` directory.
- The bot will reply with a confirmation and forward the file to the owner's account.
- Unauthorized users will trigger a log like:

```
⚠️ Unauthorized access attempt by user: @username (ID: 12345678)
```

---

## 🔐 Security Notes

- Never expose your bot token in public repositories.
- Use environment variables or `.env` files instead of hardcoding sensitive data.
- Monitor unauthorized access via bot logs or console output.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this project and submit a pull request.

---

## 📬 Contact

If you have any issues or suggestions, feel free to open an issue or reach out on Telegram.
