# Stark Bank Challenge

This repository was created to store my solution to the Stark Bank challenge. The challenge consisted of creating a project and webhook endpoint for an account that:
- Issues 8 to 12 invoices every 3 hours to random people
- Receives a webhook callback of the invoice credit and transfers that amount to a different account.

## My solution

My solution consists of a Flask application that listens for incoming webhooks from the Stark Bank API. If it receives a webhook event that says that an invoice has been credited, it transfers the invoice value to another account.
Additionally, the app supports cron jobs to schedule the creation of the invoices.