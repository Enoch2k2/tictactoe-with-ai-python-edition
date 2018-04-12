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
      Game(Computer("X"), Computer("O")).play()
      self.ask_to_play_again()
    elif user_input == "1":
      Game(Human("X"), Computer("O")).play()
      self.ask_to_play_again()
    elif user_input == "2":
      Game().play()
      self.ask_to_play_again()
    elif user_input.lower() == "exit":
      print("goodbye!")
    elif user_input.lower() == "100":
      computer_x = 0
      computer_y = 0
      cats_game = 0
      for num in range(100):
        board = Board()
        board.reset()
        game = Game(Computer("X"), Computer("O"), board)
        game.play()
        if not(game.won() == False):
          if game.winner() == "X":
            computer_x += 1
          else:
            computer_y += 1
        else:
          cats_game += 1
        del game
      print("Computer X WIN RATE: {0}".format(computer_x))
      print("Computer Y WIN RATE: {0}".format(computer_y))
      print("CATS GAMES: {0}".format(cats_game))
      self.ask_to_play_again()
    else:
      print("invalid choice")
      self.menu()

  def ask_to_play_again(self):
    user_input = input("Would you like to play again?(Y/N)\n")
    if user_input.lower() == "y":
      self.menu()
    else:
      print("Goodbye!")
