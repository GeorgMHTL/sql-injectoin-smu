from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_click(self, **event_args):
    username = self.Username.text
    password = self.password.text
    if self.save.checked:
      login_state = anvil.server.call('login_save', username, password)
    else:
      login_state = anvil.server.call('login_unsave',username, password)
    
    # alert(login_state)
    open_form('user', login_state = login_state)

    
  
