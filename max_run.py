class MaxPath():
    def __init__(self, board):
        self.board = board
        self.row = len(board)
        self.col = len(board[0])
    
    def print_arr(self):
        print('[', end="")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if(j == 0 and i != 0):
                    print(" ", end = "")
                print(self.board[i][j], end=" ")
            if i != len(self.board)-1:
                print("")
        print(']')

    def max(self, x, y, z):
        if x > y:
            return x if x > z else z
        else:
            return y if y > z else z
        
    def max_path_helper(self, row, col):
        if row < 0 or col < 0:
            return float('-inf')
        elif row == 0 and col == 0:
            return self.board[0][0]
        else:
            return self.max(self.max_path_helper(row-1, col),self.max_path_helper(row, col-1), self.max_path_helper(row-1, col-1)) + self.board[row][col]

    def max_path(self):
        return self.max_path_helper(self.row-1, self.col-1)


if __name__ == "__main__" :
    arr = [[4,8,1,3,4],
           [2,1,4,2,4],
           [3,4,0,1,1],
           [5,7,3,-1,3],
           [0,3,5,9,1],
           [1,4,8,0,1]]

    # arr = [[1,2,3],[4,8,2],[1,5,3]]
    max_arr = MaxPath(arr)
    max_arr.print_arr()
    print(max_arr.max_path())