from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.delete_button.color = "white"
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def check_box_show(self, **event_args):
    """This method is called when the CheckBox is shown on the screen"""
    pass

  def text_box_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    pass

  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    task_id = self.item.get_id()
    anvil.server.call('delete_task', task_id)
    self.clear()
    return

  def check_box_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    checked = self.check_box.checked
    task_id = self.item.get_id()
    anvil.server.call('update_check', task_id, checked)
    return

    