from flask import Blueprint, request, current_app, jsonify

webhook_bp = Blueprint("webhook_bp", __name__)

# =====================================================
# GET - VERIFIKASI META (JANGAN DIUBAH)
# =====================================================
@webhook_bp.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == current_app.config["VERIFY_TOKEN"]:
        return challenge, 200

    return "Token mismatch", 403


# =====================================================
# POST - MENERIMA PESAN DARI META
# =====================================================
@webhook_bp.route("/webhook", methods=["POST"])
def webhook_post():
    data = request.get_json()
    print("INCOMING:", data)

    return jsonify({"status": "received"}), 200
