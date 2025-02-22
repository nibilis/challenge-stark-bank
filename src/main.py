import starkbank
from flask import Flask, request, abort
from config import project
from invoice import create_invoices
from transfer import transfer_to_starkbank

# Setting up flask app
app = Flask(__name__)

# Setting up user
starkbank.user = project

# Setting error language
starkbank.language = "en-US"


# Webhook route
@app.route("/webhook", methods=["POST"])
# Function that receives a webhook for an invoice data. If the event type
# is 'credited', it transfers the invoice value to the Stark Bank account
# and returns http code 200. If the event type is not 'credited', the function
# just returns 200
def webhook():
    # Checking if the request is sent by Stark Bank
    signature = request.headers.get("Digital-Signature")
    if not signature:
        return "Missing Digital-Signature", 400

    event = starkbank.event.parse(
        content=request.data.decode("utf-8"),
        signature=signature,
    )

    if event.log.type == "credited":
        transfer_to_starkbank(event.log.invoice.amount)
        print("Money was transferred to Stark Bank!")
        return "Success", 200
    else:
        return "", 200

# Cron job route
@app.route("/cron", methods=["POST"])
# Function that receives a request and calls the function to create
# invoices (8-12 by default). This function is scheduled to happen every
# 3 hours by a cron job
def cron_send_invoices():
    action = request.args.get("action")
    if action == "send_invoices":
        create_invoices()
        return "Invoices sent", 200
    return "Invalid action", 400

if __name__ == "__main__":
    app.run()