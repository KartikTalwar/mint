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


### `mint.search_transactions(query, **kwargs)`


**Optional Paramters**

```py
# you can pick any of these
args = {
         "account_id" : 12345,
         "reimbursable" : False,
         "tax_related" : False,
         "vacation" : False,
         "loan" : False,
         "investment" : False,
         "start_date" : "09/01/13",
         "end_date" : "09/30/13",
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

### `mint.get_categories()`

```py
[
  {
    'id': 15,
    'isL1': True,
    'value': u'Travel',
    'children': [
                  {
                    'id': 1501,
                    'isL1': False,
                    'isStandard': True,
                    'value': u'Air Travel'
                  },
                  {
                    'id': 1502,
                    'isL1': False,
                    'isStandard': True,
                    'value': u'Hotel'
                  },
                  {
                    'id': 1503,
                    'isL1': False,
                    'isStandard': True,
                    'value': u'Rental Car & Taxi'
                  },
                  {
                    'id': 1504,
                    'isL1': False,
                    'isStandard': True,
                    'value': u'Vacation'}
                  ],
  },
  {
    'id': 20,
    'isL1': True,
    'value': u'Uncategorized',
    'children': [
                  {
                    'id': 2001,
                    'isL1': False,
                    'isStandard': True,
                    'value': u'Cash & ATM'
                  },
                  {
                    'id': 2002,
                    'isL1': False,
                    'isStandard': True,
                  'value': u'Check'
                  }
                ]
  }
]
```


### `mint.get_goals()`

```py
[
  {
    "imageUri": "https://images.mint.com/i/goal/type/small_emergencyfund.jpg",
    "hasUserImage": false,
    "budgetAmt": 100,
    "accounts": [
                  942160,
                  942045
                ],
    "percent": 108.42,
    "status": "met",
    "monthly_expense": 50,
    "targetAmt": 1000,
    "expectedAmt": 1000,
    "currentMonthAmt": 1014.7,
    "isLinked": "true",
    "period": 3,
    "currentAmount": 2000.48,
    "type": "6",
    "tip": "1 months behind",
    "id": 34297,
    "guid": "A870AA04E56C94A42EB6",
    "budgetType": "all",
    "projectedDate": 1382684400000,
    "name": "Emergency Fund",
    "targetDate": 1367391600000,
    "monthlyAmt": 100,
    "actions": [
                {
                  "isUser": false,
                  "id": 140632,
                  "title": "Make sure you're saving enough in your emergency fund",
                  "order": 1,
                  "created": 1359703209000,
                  "completed": 0
                },
                {
                  "isUser": false,
                  "id": 140633,
                  "title": "Save with a high-yield savings account",
                  "order": 2,
                  "created": 1359703209000,
                  "completed": 0
                },
                {
                  "isUser": false,
                  "id": 283081,
                  "title": "Consider an investment account",
                  "order": 2,
                  "created": 1375985296000,
                  "completed": 0
                }
              ]
  }
]
```

### `mint.get_budget()`

```py
{
  '24165': {
             'budgeted': [
                           {
                             'budget_amount': 60.0,
                             'budget_id': 9594395,
                             'category_id': 13,
                             'category_name': u'Bills & Utilities',
                             'is_income': False,
                             'is_transfer': False,
                             'remaining_amount': 0,
                             'remaining_balance': -20.01,
                             'total_spending': 80.01
                           },
                           {
                             'budget_amount': 50.0,
                             'budget_id': 9591425,
                             'category_id': 1,
                             'category_name': u'Entertainment',
                             'is_income': False,
                             'is_transfer': False,
                             'remaining_amount': 0,
                             'remaining_balance': 20.01,
                             'total_spending': 29.99
                           }
                         ],
            'summary': {
                         'budgeted': 110.0,
                         'total_spending': 110.00,
                         'unbudgeted': 0.0
                       },
            'unbudgeted': [
                            {
                              'amount': 0.0,
                              'category_id': 1574468,
                              'category_name': u'ATM Withdrawal'
                            }
                          ]
           }
}
```