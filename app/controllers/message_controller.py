from flask import Blueprint, request, current_app, jsonify
from ..services.whatsapp_service import WhatsAppService

webhook_bp = Blueprint("webhook_bp", __name__)

# ====================
# GET VERIFY (Meta)
# ====================
@webhook_bp.route("", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == current_app.config["VERIFY_TOKEN"]:
        return challenge, 200
    
    return "Verification token mismatch", 403


# ====================
# POST HANDLER
# ====================
@webhook_bp.route("", methods=["POST"])
def webhook_post():
    data = request.get_json()
    print("INCOMING:", data)

    entry = data.get("entry", [])
    for e in entry:
        changes = e.get("changes", [])
        for c in changes:
            messages = c.get("value", {}).get("messages", [])
            if messages:
                msg = messages[0]
                sender = msg["from"]
                text = msg["text"]["body"]

                WhatsAppService.send_message(sender, f"Kamu mengirim: {text}")

    return "EVENT_RECEIVED", 200


# HOME TEST
@webhook_bp.route("/test", methods=["GET"])
def home():
    return "Webhook OK"
