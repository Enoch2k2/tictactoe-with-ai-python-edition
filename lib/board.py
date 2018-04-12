class Board:
  def __init__(self, cells=[" ", " ", " ", " ", " ", " ", " ", " ", " "]):
    self.cells = cells

  def position(self, index):
    return self.cells[index]

  def position_taken(self, index):
    return self.position(index) == "X" or self.position(index) == "O"

  def valid_index(self, index):
    return index >= 0 and index <= 8

  def valid_move(self, index):
    return not(self.position_taken(index)) and self.valid_index(index)

  def update(self, index, player):
    self.cells[index] = player.token

  def display_board(self):
    print(" {0} | {1} | {2} ".format(self.cells[0], self.cells[1], self.cells[2]))
    print("-----------")
    print(" {0} | {1} | {2} ".format(self.cells[3], self.cells[4], self.cells[5]))
    print("-----------")
    print(" {0} | {1} | {2} ".format(self.cells[6], self.cells[7], self.cells[8]))

  def full(self):
    return len([cell for cell in self.cells if cell == " "]) == 0

  def reset(self):
    self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]