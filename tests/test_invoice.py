import starkbank
import sys

sys.path.insert(1, './src')
from config import project
from invoice import create_invoices

starkbank.user = project

create_invoices(1)