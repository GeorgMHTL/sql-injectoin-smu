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
    self.rich_text_1.content= properties.get("login_state")

    AccountState = properties.get("AccountState")
    accNo = AccountState[0]
    accState = AccountState[1]
    self.accountNo_check(accNo,accState)
    
    ## set_url_hash('#AccountNo')
    

  def button_1_click(self, **event_args):
    open_form('Form1')

  def accountNo_check(self, accNo, accState):
    if accNo:
      set_url_hash(f'#AccountNo={accState}')
    else:
      set_url_hash(f'#AccountNo=')
    
      