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


  def search_transactions(self, query, **kwargs):
    payload = {
                'queryNew'       : '',
                'query'          : query,
                'offset'         : 0,
                'filterType'     : 'cash',
                'comparableType' : 8,
                'acctChanged'    : 'T',
                'task'           :'transactions,txnfilters',
                'rnd'            : int(time.time())
              }

    if 'start_date' in kwargs:
      payload['startDate'] = kwargs['start_date']
    if 'end_date' in kwargs:
      payload['endDate'] = kwargs['end_date']
    if 'account_id' in kwargs:
      payload['accountId'] = kwargs['account_id']
    if 'reimbursable' in kwargs:
      if kwargs['reimbursable']:
        payload['query'] += ', tag:"Reimbursable"'
    if 'tax_related' in kwargs:
      if kwargs['tax_related']:
        payload['query'] += ', tag:"Tax Related"'
    if 'vacation' in kwargs:
      if kwargs['vacation']:
        payload['query'] += ', tag:"Vacation"'
    if 'investment' in kwargs:
      if kwargs['investment']:
        payload.update({'filterType' : 'investment'})
    if 'loan' in kwargs:
      if kwargs['loan']:
        payload.update({'filterType' : 'loan'})

    request = self.session.get('https://wwws.mint.com/app/getJsonData.xevent', params=payload).json()

    return request['set'][0]['data']


  def get_categories(self):
    get_url = 'https://wwws.mint.com/app/getJsonData.xevent?task=categories&rnd=%s' % int(time.time())
    request = self.session.get(get_url).json()

    return request['set'][0]['data']


  def get_goals(self):
    get_url = 'https://wwws.mint.com/app/getJsonData.xevent?task=goals&rnd=%s' % int(time.time())
    request = self.session.get(get_url).json()

    return request['set'][0]['data']['current']


  def get_budget(self, start_date=None, end_date=None):
    get_url = 'https://wwws.mint.com/getBudget.xevent?startDate=%s&endDate=%s&rnd=%s' % (start_date, end_date, int(time.time()))
    request = self.session.get(get_url).json()
    data = {}

    for month,values in request['data']['spending'].iteritems():
      data[month] = {}
      data[month]['budgeted'] = []
      data[month]['unbudgeted'] = []
      data[month]['summary'] = {
                                 'total_spending' : values['tot']['amt'],
                                 'budgeted' : values['tot']['bu'],
                                 'unbudgeted' : values['tot']['ub']
                               }
      for i in values['ub']:
        if 'pid' in i and i['cat'] != 0:
          data[month]['unbudgeted'].append({
                                        'amount' : i['amt'],
                                        'category_id' : i['cat'],
                                        'category_name' : self.get_category_from_id(i['cat'])
                                      })
      for j in values['bu']:
        data[month]['budgeted'].append({
                                      'is_transfer' : j['isTransfer'],
                                      'category_id' : j['cat'],
                                      'category_name' : self.get_category_from_id(j['cat']),
                                      'remaining_balance' : j['rbal'],
                                      'remaining_amount' : j['ramt'],
                                      'is_income' : j['isIncome'],
                                      'budget_amount' : j['bgt'],
                                      'budget_id' : j['id'],
                                      'total_spending' : j['amt']
                                    })

    return data


  def get_category_from_id(self, cid):
    if cid == 0:
      return 'Uncategorized'

    for i in self.get_categories():
      if i['id'] == cid:
        return i['value']
      if 'children' in i:
        for j in i['children']:
          if j['id'] == cid:
            return j['value']

    return 'Unknown'


  def add_new_property(self, name):
    payload = {
                'types' : 'pr',
                'accountName' : name,
                'accountValue' : 0.00,
                'associatedLoanRadio' : 'F',
                'isAdd' : 'T',
                'accountType' : 'a',
                'token' : self.token
              }

    request = self.session.post('https://wwws.mint.com/updateAccount.xevent', data=payload)

    return request.json()['response']

    # post_args = {"accountId": account_id, "types": "ot", "accountName": "Bitcoin",
    #             "accountValue": formatted_amount, "associatedLoanRadio": "No", "accountType": "3",
    #             "accountStatus": "1",  "token": token}
    # response = url_post("https://wwws.mint.com/updateAccount.xevent", post_args)
    # print "Updated Bitcoin account on mint with current balance: %s" % (formatted_amount)
    # return response

  def logout(self):
    if self.token:
      self.session.get('https://wwws.mint.com/logout.event?task=explicit')
      return True
    return False


if __name__ == '__main__':

  mint = Mint(os.environ['USER1'], os.environ['PASS1'])
  # accounts = mint.get_accounts()
  # account_detail = mint.get_account_details(accounts[0]['id'])
  # update_accounts = mint.update_accounts()
  # transactions = mint.get_transactions(tax_related=True)
  # transactions = mint.search_transactions('paid', tax_related=True)
  # categories = mint.get_categories()
  # budget = mint.get_budget('10/01/2013', '10/30/2013')
  add_prop = mint.add_new_property('Bitcoin')

  pp(add_prop)
