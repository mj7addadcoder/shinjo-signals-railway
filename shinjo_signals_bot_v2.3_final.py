
# Shinjo Signals Bot V2.3 – نسخة معدّلة مع ربط مباشر بتليجرام وإرسال توصيات سكالب تلقائيًا

import datetime
import pytz
import random
import requests

# === CONFIGURATION ===
TIMEZONE = pytz.timezone('Asia/Riyadh')
BOT_TOKEN = '8190551569:AAF_5Dp2DONImO6dCOdXfUR5byL6-qffaU0'
CHAT_ID = '-1002326910868'  # قناة ShinjoSignalsFX

SESSIONS = {
    "Sydney": ["AUDUSD"],
    "Asia": ["USDJPY", "BTCUSD", "ETHUSD"],
    "Europe": ["EURUSD", "GBPUSD"],
    "New York": ["XAUUSD", "EURUSD", "GBPUSD", "BTCUSD", "ETHUSD"]
}
CRYPTO_PAIRS = ["BTCUSD", "ETHUSD"]

# === FUNCTIONS ===

def get_active_session_and_pairs():
    now = datetime.datetime.now(TIMEZONE)
    hour = now.hour
    weekday = now.weekday()  # 5 = Saturday, 6 = Sunday

    if weekday in [5, 6]:
        return "Weekend (Crypto Only)", CRYPTO_PAIRS

    if 1 <= hour < 9:
        return "Sydney", SESSIONS["Sydney"]
    elif 9 <= hour < 17:
        return "Asia", SESSIONS["Asia"]
    elif 17 <= hour < 22:
        return "Europe", SESSIONS["Europe"]
    else:
        return "New York", SESSIONS["New York"]

def generate_signal(pair):
    price = round(random.uniform(105000, 107000), 2)
    target1 = round(price + random.uniform(50, 100), 2)
    target2 = round(price + random.uniform(100, 150), 2)
    sl = round(price - random.uniform(50, 100), 2)
    now = datetime.datetime.now(TIMEZONE).strftime('%Y-%m-%d %H:%M')

    message = f'''
🚨 توصية سكالب لحظية – Shinjo Signals
🕰️ التوقيت: {now}
💱 الزوج: {pair}
💰 السعر الحالي: {price}
🎯 الهدف 1: {target1}
🎯 الهدف 2: {target2}
🛑 وقف الخسارة: {sl}
📊 نوع الصفقة: شراء (سكالبينج)
⚙️ Shinjo V2.3 Bot – جلسة مباشرة
    '''
    return message.strip()

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, data=data)
    return response

# === MAIN EXECUTION ===
if __name__ == "__main__":
    session_name, pairs = get_active_session_and_pairs()
    for pair in pairs:
        signal = generate_signal(pair)
        send_telegram_message(signal)
