import starkbank

# Function that receives an amount as a parameter and transfers
# that amount to the Stark Bank S.A. account
def transfer_to_starkbank(amount):
    transfer = starkbank.transfer.create([
        starkbank.Transfer(
            amount = amount,
            bank_code="20018183",
            branch_code="0001",
            account_number="6341320293482496",
            name="Stark Bank S.A.",
            tax_id="20.018.183/0001-80",
            account_type="payment"
        )
    ])

    print(transfer)