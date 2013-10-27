## Mint - Unofficial Mint.com API


## Usage

```py
import mint

mint = mint.Mint(email, password)
```


## Methods

### `mint.get_accounts()`

```py
[
  {
    'accountName': u'Savings Account',
    'currency': u'USD',
    'currentBalance': 100.00,
    'id': 3542428,
    'isActive': True,
    'lastUpdated': 1382826320000L
  },
  {
    'accountName': u'Chequing Account',
    'currency': u'USD',
    'currentBalance': 42.42,
    'id': 3542429,
    'isActive': True,
    'lastUpdated': 1382826320000L
  }
]
```

### `mint.get_account_details(account_id)`

```py
{
  'accountId': 3542428,
  'accountName': u'Savings Account',
  'accountStatus': u'1',
  'accountSystemStatus': u'ACTIVE',
  'accountType': u'bank',
  'accountTypeInt': 5,
  'addAccountDate': 1382823546000L,
  'closeDate': 1382823598000L,
  'currency': u'USD',
  'currentBalance': 100.00,
  'exclusionType': u'0',
  'fiLastUpdated': 1382826320000L,
  'fiLoginDisplayName': u'Bank Name',
  'fiLoginId': 1111540,
  'fiLoginStatus': u'OK',
  'fiLoginUIStatus': u'OK',
  'fiName': u'Bank Name',
  'id': 3542428,
  'interestRate': 0.0135,
  'isActive': True,
  'isClosed': False,
  'isError': False,
  'isHiddenFromPlanningTrends': True,
  'isHostAccount': False,
  'isTerminal': True,
  'klass': u'bank',
  'lastUpdated': 1382826320000L,
  'lastUpdatedInString': u'9 minutes',
  'linkCreationTime': None,
  'linkStatus': u'NOT_LINKED',
  'linkedAccount': None,
  'linkedAccountId': None,
  'name': u'Savings Account',
  'possibleLinkAccounts': [],
  'status': u'1',
  'usageType': None,
  'userName': None,
  'value': 100.00,
  'yodleeAccountId': 75037577614L,
  'yodleeAccountNumberLast4': u'XXXXXX4217',
  'yodleeName': u'Savings Account'
}
```

### `mint.update_accounts()`

```py
True
```

### `mint.logout()`

```py
True
```

### `mint.get_transactions(**kwargs)`


**Optional Paramters**

```py
# you can pick any of these
args = {
         "account_id" : 12345,
         "reimbursable" : False,
         "tax_related" : False,
         "vacation" : False,
         "loan" : False,
         "investment" : False
       }

mint.get_transactions(**args)
mint.get_transactions(investment=True)
mint.get_transactions(account_id=12345, tax_related=True)
```


```py
[
  {
    'account': u'Savings Account',
    'amount': u'$0.12',
    'category': u'Interest Income',
    'categoryId': 3005,
    'date': u'Jul 31',
    'fi': u'Bank Name',
    'hasAttachments': False,
    'id': 217642499,
    'isAfterFiCreationTime': False,
    'isCheck': False,
    'isChild': False,
    'isDebit': False,
    'isDuplicate': False,
    'isEdited': False,
    'isFirstDate': True,
    'isLinkedToRule': False,
    'isMatched': False,
    'isPending': False,
    'isPercent': False,
    'isSpending': True,
    'isTransfer': False,
    'labels': [],
    'manualType': 0,
    'mcategory': u'Interest Income',
    'merchant': u'Interest Paid',
    'mmerchant': u'Interest Paid',
    'note': u'',
    'numberMatchedByRule': 6,
    'odate': u'Jul 31',
    'omerchant': u'Interest Paid',
    'ruleCategory': u'',
    'ruleCategoryId': 0,
    'ruleMerchant': u'',
    'txnType': 0,
    'userCategoryId': None
  }
]
```


### `mint.get_transactions(query, **kwargs)`


**Optional Paramters**

```py
# you can pick any of these
args = {
         "account_id" : 12345,
         "reimbursable" : False,
         "tax_related" : False,
         "vacation" : False,
         "loan" : False,
         "investment" : False
       }

mint.search_transactions('paid', **args)
mint.search_transactions('paid', investment=True)
mint.search_transactions('paid', account_id=12345, tax_related=True)
```


```py
[
  {
    'account': u'Savings Account',
    'amount': u'$0.12',
    'category': u'Interest Income',
    'categoryId': 3005,
    'date': u'Jul 31',
    'fi': u'Bank Name',
    'hasAttachments': False,
    'id': 217642499,
    'isAfterFiCreationTime': False,
    'isCheck': False,
    'isChild': False,
    'isDebit': False,
    'isDuplicate': False,
    'isEdited': False,
    'isFirstDate': True,
    'isLinkedToRule': False,
    'isMatched': False,
    'isPending': False,
    'isPercent': False,
    'isSpending': True,
    'isTransfer': False,
    'labels': [],
    'manualType': 0,
    'mcategory': u'Interest Income',
    'merchant': u'Interest Paid',
    'mmerchant': u'Interest Paid',
    'note': u'',
    'numberMatchedByRule': 6,
    'odate': u'Jul 31',
    'omerchant': u'Interest Paid',
    'ruleCategory': u'',
    'ruleCategoryId': 0,
    'ruleMerchant': u'',
    'txnType': 0,
    'userCategoryId': None
  }
]
```
