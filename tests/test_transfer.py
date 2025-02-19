import starkbank
import sys

sys.path.insert(1, './src')
from config import project
from transfer import transfer_to_starkbank

starkbank.user = project

transfer_to_starkbank(5000)