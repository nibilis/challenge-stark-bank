import sys
import unittest
import starkbank

sys.path.insert(1, './src')
from config import project
from invoice import create_invoices

starkbank.user = project

class TestInvoices(unittest.TestCase):
    def test_invoice_success(self):
        number_invoices = 2
        invoices = create_invoices(number_invoices)
        self.assertEqual(len(invoices), number_invoices)

if __name__ == '__main__': 
    unittest.main() 