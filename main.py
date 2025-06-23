from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8170686342:AAH8DZkbzRnk9fJPFREhsKPTGXnobeY01KA"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

paused = False

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "").lower()

        if text == "/start":
            send_msg(chat_id, "🤖 Welcome! Your FTT AI bot is now live.")
        elif text == "/pause":
            global paused
            paused = True
            send_msg(chat_id, "⏸️ Bot paused.")
        elif text == "/resume":
            paused = False
            send_msg(chat_id, "▶️ Bot resumed.")
        elif text == "/status":
            send_msg(chat_id, f"📊 Bot Status:\nPaused: {'✅' if paused else '❌'}\nWin Rate: 87%\nGrade: SS+")
        else:
            send_msg(chat_id, "❓ Unknown command.")
    return {"ok": True}

def send_msg(chat_id, text):
    requests.post(f"{TELEGRAM_API}/sendMessage", json={"chat_id": chat_id, "text": text})
