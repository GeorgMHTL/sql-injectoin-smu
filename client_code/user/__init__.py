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

    set_url_hash("234324")
    

  def button_1_click(self, **event_args):
    open_form('Form1')
