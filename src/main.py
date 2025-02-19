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
def webhook():
    # Checking if the request is by POST method
    if request.method == "POST":
        # Checking if the request is sent by Stark Bank
        event = starkbank.event.parse(
            content=request.data.decode("utf-8"),
            signature=request.headers["Digital-Signature"],
        )
        # Checking the invoice status
        if event.log.invoice.status == "credited":
            transfer_to_starkbank(event.log.invoice.amount)
            print("Transferencia realizada!")
            return "success", 200
    else:
        abort(400)

if __name__ == "__main__":
    app.run()

    