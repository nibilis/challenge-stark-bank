import random
import starkbank
from faker import Faker
from src.utils.constants import names_list

# Function that creates invoices with random values and people
# Receives amount of invoices to be created as a parameter (default value
# is a number between 8 and 13)
def create_invoices(number_invoices = random.randrange(8,13)):
    faker = Faker("pt-BR")
    person_dictionary = {name: faker.cnpj() for name in names_list}

    invoices_list = []
    
    for i in range(number_invoices):
        name, cnpj = random.choice(list(person_dictionary.items()))
        invoice = starkbank.invoice.create([
            starkbank.Invoice(
                amount=random.randrange(20000, 50000),
                name=name,
                tax_id=cnpj
            )
        ])
        invoices_list.append(invoice)
    return invoices_list