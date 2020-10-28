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


    
    def print_size(self):
        return self.row, self.col


arr = [['a', 'o', 'o', 'o'],
        ['a', 'a', 'a', 'a'],
        ['o', 'o', 'a', 'o'],
        ['o', 'a', 'a', 'a'],
        ['o', 'o', 'o', 'a']]

burrow = RabbitHole(arr)

burrow.print_burrow()
print(burrow.print_size())