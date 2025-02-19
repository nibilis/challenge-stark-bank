from config import project
import starkbank
import random

# Function that creates 8 to 12 invoices with random values
def create_invoices():
    names = ["Bob Esponja", "Patrick Estrela", "Lula Molusco", "Sandy Bochechas", 
             "Seu Sirigueijo", "Plankton", "Gary Caracol", "Homem Sereia", 
             "Mexilhãozinho", "Sra. Puff"]
    cnpj = ["88.556.907/0001-82", "74.938.383/0001-80", "70.447.391/0001-72", "50.965.631/0001-13",
            "01.330.901/0001-04", "69.974.083/0001-16", "67.090.715/0001-53", "29.079.176/0001-62",
            "54.917.485/0001-01", "15.290.832/0001-67"]
    
    for i in range(random.randrange(8,12)):
        invoices = starkbank.invoice.create([
            starkbank.Invoice(
                amount=random.randrange(20000, 50000),
                name=names[i],
                tax_id=cnpj[i]
            )
        ])


def transfer():
    pass

def __main__():
    # Setting up user
    starkbank.user = project

    # Setting error language
    starkbank.language = "en-US"

    create_invoices()

    print(starkbank.balance.get())

__main__()