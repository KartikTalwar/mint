import os
import sys
import requests
from pprint import pprint as pp


class Mint:

  def __init__(self, email, password):
    self.email    = email
    self.password = password
    self.token    = None

    self.login()


  def login(self):
    payload  = {
                "username" : self.email,
                "password" : self.password,
                "task"     : "L",
                "nextPage" : "overview.event"
               }

    session  = requests.Session()
    response = session.post("https://wwws.mint.com/loginUserSubmit.xevent", data=payload).text
    js_token = response.split('javascript-token')[1].split('>')[0]
    js_token = js_token.split('value="')[1].split('"')[0]

    self.token = js_token



if __name__ == '__main__':

  mint = Mint(os.environ['USER'], os.environ['PASS'])
  pp(mint.login())
