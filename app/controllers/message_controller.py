from flask import Blueprint, request, jsonify, current_app
from ..services.whatsapp_service import WhatsAppService

message_bp = Blueprint("message_bp", __name__)

# =========================
#   GET VERIFICATION
# =========================
@message_bp.route("/webhook", methods=["GET"])
def webhook_verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    verify_token = current_app.config["VERIFY_TOKEN"]

    if mode == "subscribe" and token == verify_token:
        return challenge, 200
    else:
        return "Verification token mismatch", 403


# =========================
#   POST – RECEIVE MESSAGE
# =========================
@message_bp.route("/webhook", methods=["POST"])
def webhook_post():
    data = request.get_json()
    print("INCOMING DATA:", data)

    if data and "entry" in data:
        for entry in data["entry"]:
            changes = entry.get("changes", [])
            for change in changes:
                value = change.get("value", {})
                messages = value.get("messages", [])

                if messages:
                    msg = messages[0]
                    sender = msg["from"]
                    text = msg["text"]["body"] if "text" in msg else ""

                    print("Pesan dari:", sender)
                    print("Isi:", text)

                    # Kirim balasan otomatis
                    WhatsAppService.send_message(
                        to=sender,
                        message=f"Kamu mengirim: {text}"
                    )

    return "EVENT_RECEIVED", 200


# =========================
#   ROOT ROUTE
# =========================
@message_bp.route("/", methods=["GET"])
def home():
    return "WhatsApp Cloud API Bot Aktif!"
