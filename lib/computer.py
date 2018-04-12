import os
import sys
import random

cwd = os.getcwd()
sys.path.append("/lib")

from player import *

class Computer(Player):
  valid_moves = [0,1,2,3,4,5,6,7,8]
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

  def __init__(self, token):
    Player.__init__(self, token)
    self.opp_token = "O" if token == "X" else "X"

  def move(self, board):
    if self.win(board):
      return self.win(board)
    elif self.defend(board):
      return self.defend(board)
    elif self.take_middle(board):
      return self.take_middle(board)
    elif self.take_corner(board):
      return random.choice(self.take_corner(board))
    else:
      return random.choice(self.take_side(board))

  def win(self, board):
    for win_combo in self.WIN_COMBINATIONS:
      index1 = win_combo[0]
      index2 = win_combo[1]
      index3 = win_combo[2]

      position1 = board.cells[index1]
      position2 = board.cells[index2]
      position3 = board.cells[index3]

      if position1 == self.token and position2 == self.token and position3 == " ":
        return index3
      elif position1 == self.token and position3 == self.token and position2 == " ":
        return index2
      elif position2 == self.token and position3 == self.token and position1 == " ":
        return index1
    return False

  def defend(self,board):
    for win_combo in self.WIN_COMBINATIONS:
      index1 = win_combo[0]
      index2 = win_combo[1]
      index3 = win_combo[2]

      position1 = board.cells[index1]
      position2 = board.cells[index2]
      position3 = board.cells[index3]

      if position1 == self.opp_token and position2 == self.opp_token and position3 == " ":
        return index3
      elif position1 == self.opp_token and position3 == self.opp_token and position2 == " ":
        return index2
      elif position2 == self.opp_token and position3 == self.opp_token and position1 == " ":
        return index1
    return False

  def take_middle(self, board):
    if board.cells[4] == " ":
      return 4

  def take_corner(self, board):
    corners = [0,2,6,8]
    available = [corner for corner in corners if not(board.position_taken(corner))]
    return available if len(available) > 0 else False

  def take_side(self, board):
    sides = [1, 3, 5, 7]
    available = [side for side in sides if not(board.position_taken(side))]
    return available if len(available) > 0 else False