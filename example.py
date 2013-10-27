import mint


email    = 'name@domain.com'
password = 'hello123'
coinbase = 'coinbase_api_key'

mint = mint.Mint(email, password)


# get list of bank accounts
print mint.get_accounts()

# get bank account details
print mint.get_account_details(accounts[0]['id'])

# fetch balance and transactions from bank accounts
print mint.update_accounts()

# get a list of transactions
print mint.get_transactions(tax_related=True)

# search transactions by given query
print mint.search_transactions('paid', tax_related=True)

# get a list of categories
print mint.get_categories()

# get montly budget details
print mint.get_budget('10/01/2013', '10/30/2013')

# show all properties
print mint.get_properties()

# add a new property
print mint.add_new_property('Bitcoin')

# update property value
print mint.update_property(3551373, 100)

# update bitcoin balance from coinbase
print mint.update_bitcoins(coinbase)



