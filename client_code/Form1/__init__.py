from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.todo_card.align = "left"
    # Any code you write here will run before the form opens.

  def get_task_list(self):
    return anvil.server.call('get_task_list')

  def summit_buttton_click(self, **event_args):
    """This method is called when the button is clicked"""
    task = self.task_summit_text_box.text 
    if task == "":
      return

    anvil.server.call('add_task', task)
    self.task_summit_clear()
    return

  def task_summit_clear(self):
    self.task_summit_text_box.text = ""
    return

    
