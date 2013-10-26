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



if __name__ == '__main__':

  mint = Mint(os.environ['USER'], os.environ['PASS'])
  # accounts = mint.get_accounts()
  # account_detail = mint.get_account_details(accounts[0]['id'])
  update_accounts = mint.update_accounts()


  pp(update_accounts)
