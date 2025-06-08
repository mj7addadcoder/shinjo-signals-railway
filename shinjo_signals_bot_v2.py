
import requests
import time
import random

# ==== Configuration ====
TOKEN = "8190551569:AAF_5Dp2DONImO6dCOdXfUR5byL6-qffaU0"
CHAT_ID = "-1002326910868"
ALPHA_VANTAGE_API = "AXYEBCEBTPLOIB3H"
COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

# ==== Helper Functions ====

def get_crypto_price(symbol):
    try:
        response = requests.get(f"{COINGECKO_URL}?ids={symbol}&vs_currencies=usd")
        return response.json()[symbol]["usd"]
    except:
        return None

def get_forex_price(pair):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={pair[:3]}&to_currency={pair[3:]}&apikey={ALPHA_VANTAGE_API}"
    try:
        response = requests.get(url)
        data = response.json()
        return float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    except:
        return None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    return requests.post(url, data=payload)

# ==== Main Logic ====
def generate_scalping_signal():
    pairs = [("BTCUSD", "bitcoin"), ("ETHUSD", "ethereum"), ("EURUSD", None), ("GBPUSD", None)]
    pair, crypto_id = random.choice(pairs)
    entry_price = None

    if crypto_id:
        entry_price = get_crypto_price(crypto_id)
    else:
        entry_price = get_forex_price(pair)

    if entry_price:
        sl = round(entry_price * 0.995, 4)
        tp1 = round(entry_price * 1.005, 4)
        tp2 = round(entry_price * 1.01, 4)
        message = (
            "🚨 *توصية سكالب لحظية – Shinjo Signals*
"
            f"💱 الزوج: `{pair}`
"
            f"💰 السعر الحالي: *{entry_price}*
"
            f"🎯 الهدف 1: `{tp1}`
"
            f"🎯 الهدف 2: `{tp2}`
"
            f"🛑 وقف الخسارة: `{sl}`
"
            "📊 نوع الصفقة: *شراء* (مثال)
"
            "🧠 ملاحظة: تم توليد الإشارة بناءً على تحليل فني تلقائي"
        )
        send_telegram_message(message)
    else:
        send_telegram_message("فشل في جلب السعر الحقيقي، تحقق من الاتصال أو المفاتيح.")

# Run once for now (production version would be a scheduler)
generate_scalping_signal()
