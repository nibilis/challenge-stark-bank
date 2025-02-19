import random
import starkbank

# Function that creates invoices with random values and people
# Receives amount of invoices to be created as a parameter (default value
# is a number between 8 and 13)
def create_invoices(amount = random.randrange(8,13)):
    names = ["Bob Esponja", "Patrick Estrela", "Lula Molusco", "Sandy Bochechas", 
             "Seu Sirigueijo", "Plankton", "Gary Caracol", "Homem Sereia", 
             "Mexilhãozinho", "Sra. Puff"]
    cnpj = ["88.556.907/0001-82", "74.938.383/0001-80", "70.447.391/0001-72", "50.965.631/0001-13",
            "01.330.901/0001-04", "69.974.083/0001-16", "67.090.715/0001-53", "29.079.176/0001-62",
            "54.917.485/0001-01", "15.290.832/0001-67"]
    
    names_size = len(names)
    
    for i in range(amount):
        # Getting a random person from the array
        random_person_index = random.randrange(0, names_size)
        invoices = starkbank.invoice.create([
            starkbank.Invoice(
                amount=random.randrange(20000, 50000),
                name=names[random_person_index],
                tax_id=cnpj[random_person_index]
            )
        ])