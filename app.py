from flask import Flask, request
from dotenv import load_dotenv
import os
import requests
from responses import get_response   # ✅ response logic

# Load environment variables
load_dotenv()

# Get values from .env
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

app = Flask(__name__)

# 🔹 SEND MESSAGE FUNCTION (Module 6)
def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={ACCESS_TOKEN}"

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }

    response = requests.post(url, json=payload)

    print("Message sent:", response.status_code, response.text)


# 🔹 GET → Webhook Verification
@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Webhook verified!")
        return challenge, 200
    else:
        return "Verification failed", 403


# 🔹 POST → Receive Messages
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Full Data:", data)

    if data.get("object") == "instagram":
        for entry in data.get("entry", []):
            for msg in entry.get("messaging", []):

                # Avoid bot replying to itself
                if "message" in msg and not msg["message"].get("is_echo"):

                    sender_id = msg["sender"]["id"]
                    text = msg["message"].get("text")

                    print("Sender ID:", sender_id)
                    print("User Message:", text)

                    # ✅ Generate reply
                    reply = get_response(text)

                    print("Bot Reply:", reply)

                    # 🔥 SEND REPLY BACK TO INSTAGRAM
                    send_message(sender_id, reply)

    return "OK", 200


# 🔹 Run server
if __name__ == "__main__":
    app.run(port=5000, debug=True)