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

  def compare_three(self, x, y, z):
    if x == "*" and y == "*" and z =="*":
        return "*"
    elif x != "*":
        return x
    elif y != "*":
        return y
    else:
        return z
    
  def rabbit_path_helper(self, row, col, origin):
    if row < 0 or col < 0 or col >= self.col or self.board[row][col] == 'o':
        return "*"
    elif row == 0 and col == 0:
        return "(0,0)"
    else:
        if origin == "right":
            return self.compare_three(self.rabbit_path_helper(row-1, col, "down"),self.rabbit_path_helper(row, col-1, "right"), "*") + " -> (" +str(row) +"," +str(col) +")"
        elif origin == "left":
            return self.compare_three(self.rabbit_path_helper(row-1, col, "down"), "*", self.rabbit_path_helper(row, col+1, "left")) + " -> (" +str(row) +"," +str(col) +")"
        else:
            return self.compare_three(self.rabbit_path_helper(row-1, col, "down"), self.rabbit_path_helper(row, col-1, "right"), self.rabbit_path_helper(row, col+1, "left")) + " -> (" +str(row) +"," +str(col) +")"

  def rabbit_path(self):
    path = self.rabbit_path_helper(self.row-1, self.col-1, "x")
    if "*" in path:
        return "There is no Path"
    stripped_path = path.replace(")"," ").replace("->", "").replace("(","").split("   ")
    for indices in stripped_path:
        self.board[int(indices[0])][int(indices[2])] = 1
    return path



if __name__ == "__main__" :
    print("Rabbit 1 (Example of only down and right movement)")
    arr = [['A', 'o', 'o', 'o'],
            ['A', 'A', 'A', 'A'],
            ['o', 'o', 'A', 'o'],
            ['o', 'A', 'A', 'A'],
            ['o', 'o', 'o', 'A']]

    burrow = RabbitHole(arr)
    print(burrow.rabbit_path())
    burrow.print_burrow()

    print("\nRabbit 2 (Example of all possible movement, left, right and down)")
    arr = [['A', 'A', 'o', 'o'],
            ['o', 'A', 'A', 'A'],
            ['o', 'o', 'o', 'A'],
            ['o', 'A', 'A', 'A'],
            ['o', 'A', 'o', 'o'],
            ['o', 'A', 'A', 'A']]

    burrow = RabbitHole(arr)
    print(burrow.rabbit_path())
    burrow.print_burrow()

    print("\nRabbit 3 (Example of no possible path)")
    arr = [['A', 'A', 'o', 'o'],
            ['o', 'A', 'A', 'A'],
            ['o', 'o', 'o', 'A'],
            ['o', 'A', 'A', 'A'],
            ['o', 'o', 'o', 'o'],
            ['o', 'A', 'A', 'A']]

    burrow = RabbitHole(arr)
    print(burrow.rabbit_path())
    burrow.print_burrow()