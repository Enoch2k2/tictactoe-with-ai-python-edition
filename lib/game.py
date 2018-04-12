import os
import sys

cwd = os.getcwd()
sys.path.append(cwd + "/lib")

from human import *
from board import *

class Game:
  WIN_COMBINATIONS = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6],
  ]

  def __init__(self, player1 = Human("X"), player2 = Human("O"), board = Board()):
    self.player1 = player1
    self.player2 = player2
    self.board = board

  def turn(self):
    index = self.current_player().move(self.board)
    if self.board.valid_move(index):
      self.board.update(index, self.current_player())
      self.board.display_board()
    else:
      self.board.display_board()
      print("Invalid Choice")
      self.turn()

  def turn_count(self):
    count = 0
    for token in self.board.cells:
      if token == "X" or token == "O":
        count += 1
    return count

  def current_player(self):
    if self.turn_count() % 2 == 0:
      return self.player1
    else:
      return self.player2

  def won(self):
    for win_combo in self.WIN_COMBINATIONS:
      index1 = win_combo[0]
      index2 = win_combo[1]
      index3 = win_combo[2]
      position1 = self.board.cells[index1]
      position2 = self.board.cells[index2]
      position3 = self.board.cells[index3]
      if position1 == position2 and position2 == position3 and self.board.position_taken(index1):
        return win_combo
    return False
    
  def draw(self):
    return not(self.won()) and self.board.full()

  def over(self):
    return self.won() or self.draw()

  def winner(self):
    if not(self.won() == False):
      return self.board.cells[self.won()[0]]

  def play(self):
    while not(self.over()):
      self.turn()
    if not(self.won() == False):
      print("Congratulations {0}!".format(self.winner()))
    else:
      print("Cat's Game!")
    