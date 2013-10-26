## Mint - Unofficial Mint.com API


## Usage

```py
import mint

mint = Mint(username, password)
```


## Methods

### get_accounts()

```
print mint.get_accounts()
```

### get_account_details(account_id)

```
accounts = mint.get_accounts()
print mint.get_account_details(accounts[0]['id'])
```
