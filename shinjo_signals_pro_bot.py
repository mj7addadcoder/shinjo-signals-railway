
import requests
import time
import random

# Telegram Bot Token and Channel ID
TOKEN = "8190551569:AAF_5Dp2DONImO6dCOdXfUR5byL6-qffaU0"
CHAT_ID = "-1002326910868"

# List of dummy pairs to simulate monitoring
PAIRS = ["BTCUSD", "ETHUSD", "XAUUSD"]

# Fake function to simulate market condition
def check_market(pair):
    # Randomly simulate a "signal" with dummy logic
    if random.randint(0, 10) > 8:
        return {
            "pair": pair,
            "direction": random.choice(["شراء", "بيع"]),
            "entry": round(random.uniform(1000, 30000), 2),
            "tp": round(random.uniform(1000, 30000), 2),
            "sl": round(random.uniform(1000, 30000), 2),
            "reason": "شمعة اندفاع + كسر مستوى + تأكيد RSI"
        }
    return None

# Main loop to simulate checking signals every 60 seconds
def run_bot():
    while True:
        for pair in PAIRS:
            signal = check_market(pair)
            if signal:
                message = f"""
🚨 توصية لحظية – سكالب {signal['direction']}
💱 الزوج: {signal['pair']}
🎯 الدخول: {signal['entry']}
🎯 الهدف: {signal['tp']}
🛡️ الستوب: {signal['sl']}
🧠 معطيات: {signal['reason']}
📢 سكالب تلقائي – نفذ فورًا!
#ShinjoSignals
"""
                url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                data = {"chat_id": CHAT_ID, "text": message}
                requests.post(url, data=data)
        time.sleep(60)

if __name__ == "__main__":
    run_bot()
