import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
    PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
    WABA_ID = os.getenv("WABA_ID")

