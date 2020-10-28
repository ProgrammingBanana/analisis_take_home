class RabbitHole():
  def __init__(self, board):
    self.board = board
    self.row = len(board)
    self.col = len(board[0])

  def print_burrow(self):
    print('[', end="")
    for i in range(len(self.board)):
        for j in range(len(self.board[i])):
            if(j == 0 and i != 0):
                print(" ", end = "")
            print(self.board[i][j], end=" ")
        if i != len(self.board)-1:
            print("")
    print(']')

    def compare(self, x, y):
        if x == "*" and y == "*":
            return "*"
        return y if x == "*" else x
        
    def rabbit_path_helper(self, row, col):
        if row < 0 or col < 0 or self.board[row][col] == 'o':
            return "*"
        elif row == 0 and col == 0:
            return "(0,0)"
        else:
            return self.compare(self.rabbit_path_helper(row-1, col),self.rabbit_path_helper(row, col-1)) + " -> (" +str(row) +"," +str(col) +")"

    def rabbit_path(self):
        path = self.rabbit_path_helper(self.row-1, self.col-1)
        return path if "*" not in path else "There is no path" 

    def print_size(self):
        return self.row, self.col


if __name__ == "__main__" :
    arr = [['A', 'o', 'o', 'o'],
            ['A', 'A', 'A', 'A'],
            ['o', 'o', 'A', 'o'],
            ['o', 'A', 'A', 'A'],
            ['o', 'o', 'o', 'A']]

    burrow = RabbitHole(arr)
    burrow.print_burrow()
    print(burrow.rabbit_path())