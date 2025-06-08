
import requests

# Telegram Bot Token
TOKEN = "8190551569:AAF_5Dp2DONImO6dCOdXfUR5byL6-qffaU0"

# Channel Chat ID
CHAT_ID = "-1002326910868"

# Message Content
MESSAGE = "🚨 توصية تجريبية من ShinjoSignalsBot\n💰 الربط شغال تمام يا مصطفى!\nالآن نبدأ بإرسال التوصيات تلقائيًا بإذن الله 🔥"

# Send the message
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": MESSAGE}
response = requests.post(url, data=data)

print("تم إرسال الرسالة:", response.text)
