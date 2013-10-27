import os
import sys
import json
import time
import requests
from pprint import pprint as pp


class Mint:

  def __init__(self, email, password):
    self.email    = email
    self.password = password
    self.token    = None
    self.session  = requests.Session()
    self.accounts = []

    self.login()


  def login(self):
    payload  = {
                "username" : self.email,
                "password" : self.password,
                "task"     : "L",
                "nextPage" : "overview.event"
               }

    response = self.session.post("https://wwws.mint.com/loginUserSubmit.xevent", data=payload).text
    js_token = response.split('javascript-token')[1].split('>')[0]
    js_token = js_token.split('value="')[1].split('"')[0]

    self.token = js_token


  def get_accounts(self):
    if not self.token:
      return 'Not logged in'

    payload = json.dumps(
                [
                  {
                    "args":
                      {
                         "types":
                           [
                             "BANK",
                             "CREDIT",
                             "INVESTMENT",
                             "LOAN",
                             "MORTGAGE",
                             "OTHER_PROPERTY",
                             "REAL_ESTATE",
                             "VEHICLE",
                             "UNCLASSIFIED"
                           ]
                      },
                    "id": "115485",
                    "service": "MintAccountService",
                    "task": "getAccountsSorted"
                  }
                ]
              )

    post_url = "https://wwws.mint.com/bundledServiceController.xevent?token="+self.token
    response = self.session.post(post_url, data={"input": payload})
    response = json.loads(response.text)["response"]
    accounts = response["115485"]["response"]

    self.accounts = accounts
    return_keys   = ['id', 'accountName', 'currency', 'currentBalance', 'isActive', 'lastUpdated']

    return [dict(((k,account[k]) for k in return_keys) ) for account in self.accounts]


  def get_account_details(self, account_id):
    for account in self.accounts:
      if account['id'] == account_id:
        return account

    return {}


  def update_accounts(self):
    post_url = 'https://wwws.mint.com/refreshFILogins.xevent'
    payload  = {"token" : self.token}
    send_req = self.session.post(post_url, data=payload)

    status  = False
    counter = time.time()

    while status is False:
      check_url = 'https://wwws.mint.com/userStatus.xevent?rnd=%s' % int(time.time())
      check_req = self.session.get(check_url).json()['isRefreshing']

      time.sleep(0.5)

      if not check_req:
        status = True
      if time.time() - counter > 60:
        break

    return status


  def get_transactions(self, **kwargs):
    payload = {
                'queryNew'       : '',
                'offset'         : 0,
                'filterType'     : 'cash',
                'comparableType' : 8,
                'acctChanged'    : 'T',
                'task'           :'transactions,txnfilters',
                'rnd'            : int(time.time())
              }

    if 'account_id' in kwargs:
      payload['accountId'] = kwargs['account_id']
    if 'reimbursable' in kwargs:
      if kwargs['reimbursable']:
        payload['query'] = 'tag:"Reimbursable"'
    if 'tax_related' in kwargs:
      if kwargs['tax_related']:
        payload['query'] = 'tag:"Tax Related"'
    if 'vacation' in kwargs:
      if kwargs['vacation']:
        payload['query'] = 'tag:"Vacation"'
    if 'investment' in kwargs:
      if kwargs['investment']:
        payload.update({'filterType' : 'investment'})
    if 'loan' in kwargs:
      if kwargs['loan']:
        payload.update({'filterType' : 'loan'})

    request = self.session.get('https://wwws.mint.com/app/getJsonData.xevent', params=payload).json()

    return request['set'][0]['data']


  def logout(self):
    if self.token:
      self.session.get('https://wwws.mint.com/logout.event?task=explicit')
      return True
    return False


if __name__ == '__main__':

  mint = Mint(os.environ['USER'], os.environ['PASS'])
  accounts = mint.get_accounts()
  # account_detail = mint.get_account_details(accounts[0]['id'])
  # update_accounts = mint.update_accounts()
  transactions = mint.get_transactions(tax_related=True)
  # transactions = mint.get_transactions(account_id=accounts[0]['id'])

  pp(transactions)
