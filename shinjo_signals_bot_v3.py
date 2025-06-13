import os
import requests
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TWELVE_API = os.getenv("TWELVE_API")

PAIR = "XAU/USD"

def get_price():
    url = f"https://api.twelvedata.com/price?symbol={PAIR}&apikey={TWELVE_API}"
    response = requests.get(url).json()
    return float(response['price'])

def send_signal(entry_price, direction, sl, tp1, tp2):
    message = f"""
🚀 توصية جديدة – Shinjo Signals

الزوج: {PAIR}
الاتجاه: {'شراء 🟢' if direction == 'buy' else 'بيع 🔴'}
نقطة الدخول: {entry_price}
الهدف الأول 🎯: {tp1}
الهدف الثاني 💰: {tp2}
وقف الخسارة ❌: {sl}

⚙️ أُرسلت تلقائيًا من ShinjoSignalsBot.
    """
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
        "chat_id": CHAT_ID,
        "text": message
    })

while True:
    try:
        price = get_price()
        direction = "buy"
        sl = round(price - 50, 2)
        tp1 = round(price + 50, 2)
        tp2 = round(price + 100, 2)
        send_signal(price, direction, sl, tp1, tp2)
        print("✅ توصية أُرسلت")
    except Exception as e:
        print("❌ خطأ:", e)
    time.sleep(60)
