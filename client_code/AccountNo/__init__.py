from ._anvil_designer import AccountNoTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AccountNo(AccountNoTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    url = anvil.js.window.location.href
    data = anvil.server.call('login_accNo',url)
    self.label_1.text = data
    

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    anvil.server.call('del_session')
    open_form('Form1')
    


