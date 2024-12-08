import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def login_save(username, password):
    con = sqlite3.connect(data_files["data_base.db"])
    cur = con.cursor()
    query = "SELECT username, isAdmin FROM Users WHERE username = ? AND password = ?"
    cur.execute(query, (username, password))
    result = cur.fetchone()
    con.close()
    if result == None:
      return f"Login Fail: {query}"
    else:
      return f"Login Sucsess {query}"

@anvil.server.callable
def login_unsave(username,password):
  con = sqlite3.connect(data_files["data_base.db"])
  cur = con.cursor()
  print(username)
  query = f"SELECT username, isAdmin FROM Users WHERE username = '{username}' AND password = '{password}'"
  cur.execute(query)
  reslut = cur.fetchone()
  con.close()
  if reslut == None:
    return f"Login Fail: {query}"
  else:

    return f"Login Sucsess {query}"

@anvil.server.callable
def get_accountNo(username, password):
  con = sqlite3.connect(data_files["data_base.db"])
  cur = con.cursor()
  print(username)
  query = "SELECT AccountNo FROM Users WHERE username = ? AND password = ?"
  cur.execute(query, (username, password))
  reslut = cur.fetchone()
  if reslut == None:
    return [False , ' ']
  else:
    return [True, reslut]
  con.close()
  