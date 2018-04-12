import os
import sys

cwd = os.getcwd()
sys.path.append(cwd + "/lib")

from player import *

class Human(Player):
  def move(self, board):
    user_input = input("Please select 1-9:\n")
    return int(user_input) - 1