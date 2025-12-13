from flask import Blueprint, request, jsonify, current_app
from ..services.whatsapp_service import WhatsAppService

message_bp = Blueprint("message_bp", __name__)

# ==========================
# GET: WEBHOOK VERIFY
# ==========================
@message_bp.route("/webhook", methods=["GET"])
def verify_token():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == current_app.config["VERIFY_TOKEN"]:
        return challenge, 200

    return "Verification token mismatch", 403


# ==========================
# POST: RECEIVE MESSAGE
# ==========================
@message_bp.route("/webhook", methods=["POST"])
def webhook_post():
    data = request.get_json(silent=True)
    print("INCOMING DATA:", data)

    if not data:
        return "OK", 200

    if "entry" in data:
        for entry in data["entry"]:
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])

                if messages:
                    msg = messages[0]
                    sender = msg["from"]
                    text = msg.get("text", {}).get("body", "")

                    print("Pesan dari:", sender)
                    print("Isi:", text)

                    WhatsAppService.send_message(
                        to=sender,
                        message=f"Kamu mengirim: {text}"
                    )

    return "EVENT_RECEIVED", 200

