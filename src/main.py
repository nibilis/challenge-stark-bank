from config import project
import os
import starkbank

def create_invoices():
    pass

def __main__():
    # Setting up user
    starkbank.user = project

    # Setting error language
    starkbank.language = "en-US"
    
    print(starkbank.balance.get())

__main__()