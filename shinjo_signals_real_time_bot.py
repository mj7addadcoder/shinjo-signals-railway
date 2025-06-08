
import requests
import time

# Telegram Bot Config
TOKEN = "8190551569:AAF_5Dp2DONImO6dCOdXfUR5byL6-qffaU0"
CHAT_ID = "-1002326910868"

# Alpha Vantage API Key
ALPHA_KEY = "AXYEBCEBTPLOIB3H"

# Pairs to monitor
COINGECKO_PAIRS = {
    "bitcoin": "BTCUSD",
    "ethereum": "ETHUSD"
}

ALPHAVANTAGE_PAIRS = {
    "EURUSD": "EUR/USD",
    "XAUUSD": "XAU/USD"
}

def fetch_price_coingecko(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        r = requests.get(url)
        data = r.json()
        return float(data[coin_id]["usd"])
    except:
        return None

def fetch_price_alpha(pair):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={pair[:3]}&to_currency={pair[-3:]}&apikey={ALPHA_KEY}"
    try:
        r = requests.get(url)
        data = r.json()
        return float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    except:
        return None

def send_telegram_signal(pair, price, direction="سكالب تلقائي"):
    message = (
        f"🚨 توصية لحظية – {direction}\n"
        f"💱 الزوج: {pair}\n"
        f"💰 السعر الحالي: {price}\n"
        f"🧠 إشعار تلقائي مبني على السعر الحقيقي\n"
        f"📢 سكالب فعلي – راقب التنفيذ!\n"
        f"#ShinjoSignals"
    )
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def main():
    while True:
        # CoinGecko prices
        for coin_id, symbol in COINGECKO_PAIRS.items():
            price = fetch_price_coingecko(coin_id)
            if price:
                send_telegram_signal(symbol, price)

        # AlphaVantage prices
        for symbol, name in ALPHAVANTAGE_PAIRS.items():
            price = fetch_price_alpha(name)
            if price:
                send_telegram_signal(symbol, price)

        time.sleep(60)

if __name__ == "__main__":
    main()
