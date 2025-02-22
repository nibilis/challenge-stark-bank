import json
import unittest
import requests

webhook_url = "http://127.0.0.1:5000/webhook"

class TestTransfer(unittest.TestCase):
    def test_webhook_fail(self):
        data = { "status": "credited" }
        request = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

        self.assertEqual(request.status_code, 400)

    def test_webhook_parse_fail(self):
        data = { "status": "credited" }
        request = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json", "Digital-Signature": "52664148968648"})

        self.assertEqual(request.status_code, 500)

if __name__ == '__main__': 
    unittest.main() 