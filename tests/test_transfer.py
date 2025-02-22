import sys
import unittest
import starkbank

sys.path.insert(1, './src')
from config import project
from transfer import transfer_to_starkbank

starkbank.user = project

class TestTransfer(unittest.TestCase):
    def test_transfer_success(self):
        transfer = transfer_to_starkbank(1000)
        transfer = starkbank.transfer.get(transfer.id)

        self.assertEqual(transfer.status, "created")

if __name__ == '__main__': 
    unittest.main() 