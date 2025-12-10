import requests
from flask import current_app

class WhatsAppService:

    @staticmethod
    def send_message(to, message):
        url = f"https://graph.facebook.com/v19.0/{current_app.config['PHONE_NUMBER_ID']}/messages"

        headers = {
            "Authorization": f"Bearer {current_app.config['WHATSAPP_TOKEN']}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": message}
        }

        r = requests.post(url, headers=headers, json=data)
        print("RESPONSE WA:", r.text)
        return r.json()


