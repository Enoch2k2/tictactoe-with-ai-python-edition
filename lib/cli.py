import os
import sys

cwd = os.getcwd()
sys.path.append(cwd + "/lib")

from game import *
from human import *
from computer import *

class Cli:
  
  def start(self):
    print("Welcome to Tic Tac Toe!")
    self.menu()

  def menu(self):
    print("Please read through the following menu. Type Exit to exit the program.")
    user_input = input("How many players are going to play? 0, 1, or 2\n")
    if user_input == "0":
      print("playing a 0 player game!")
    elif user_input == "1":
      Game(Human("X"), Computer("O")).play()
    elif user_input == "2":
      Game().play()
    elif user_input.lower() == "exit":
      print("goodbye!")
    else:
      print("invalid choice")
      self.menu()