from ._anvil_designer import userTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class user(userTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(properties.get('login_state'))
    # Any code you write here will run before the form opens.


    AccountState = properties.get("AccountState")
    accNo = AccountState[1]
    accState = AccountState[0]
    self.accountNo_set(accNo,accState)
    state = self.accountNo_check(accNo)
    self.rich_text_1.content= f"{state} \n {properties.get('login_state')}"
    

  def button_1_click(self, **event_args):
    open_form('Form1')
    set_url_hash("")

  def accountNo_set(self, accNo, accState):
    if accState:
      set_url_hash(f'#AccountNo={accNo[0]}')
    else:
      set_url_hash(f'#AccountNo=')

  def accountNo_check(self, accNo):
    print(get_url_hash(), f'AccountNo={accNo}')
    if get_url_hash() == f'AccountNo={accNo[0]}':
      return "YOU OWN THE DATABASE!"

    return "AccountNo NOT PASSED"
    
      