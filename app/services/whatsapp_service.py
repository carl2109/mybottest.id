import requests
from flask import current_app

class WhatsAppService:

    @staticmethod
    def send_message(text):
        url = f"https://graph.facebook.com/v20.0/{current_app.config['PHONE_NUMBER_ID']}/messages"

        headers = {
            "Authorization": f"Bearer {current_app.config['WHATSAPP_TOKEN']}",
            "Content-Type": "application/json"
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": "<NOMOR_KAMU>",
            "type": "text",
            "text": {"body": text}
        }

        response = requests.post(url, json=payload, headers=headers)
        print("Response WA:", response.text)
        return response.text
