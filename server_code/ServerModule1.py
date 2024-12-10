import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def get_task_list():
  tasks = app_tables.task.search()
  for task in tasks:
    print(task['check'], task['name'])
  return tasks

@anvil.server.callable
def add_task(name):
  app_tables.task.add_row(check=False, name=name)
  return