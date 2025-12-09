import requests
import os

class WhatsAppService:

    @staticmethod
    def send_message(to, message):
        url = f"https://graph.facebook.com/v20.0/{os.getenv('PHONE_NUMBER_ID')}/messages"

        headers = {
            "Authorization": f"Bearer {os.getenv('WHATSAPP_TOKEN')}",
            "Content-Type": "application/json"
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": message}
        }

        response = requests.post(url, headers=headers, json=payload)
        print("SEND MESSAGE RESPONSE:", response.text)

        return response.json()

