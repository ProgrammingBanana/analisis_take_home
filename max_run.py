class MaxPath():
    # Constructor de MaxPath
    def __init__(self, board):
        self.board = board
        self.row = len(board)
        self.col = len(board[0])
    
    # Imprime la matriz
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
        """ Verifica el maximo de tres numeros

        Args:
            x (int): Valor 1 
            y (int): Valor 2
            z (int): Valor 3

        Returns:
            [int]: Devuelve el numero mas grande de los tres.
        """
        if x > y:
            return x if x > z else z
        else:
            return y if y > z else z
        
    def max_path_helper(self, row, col):
        """ Metodo recursivo que recibe fila y columna y va calculando el camino de maximmo valor

        Args:
            row ([int]): indice de fila
            col ([int]): indice de columna

        Returns:
            [int]: La suma del camino de mayor valor
        """
        # Si la fila o columna es menor que 0 devuelve -infinito
        if row < 0 or col < 0:
            return float('-inf')
        # Si se llego al inicio devuelve el valor del inicio
        elif row == 0 and col == 0:
            return self.board[0][0]
        else:
            # Devuelve la suma del valor maximo de las llamadas recursivas mas el valor en la posicion actual de la matriz
            return self.max(self.max_path_helper(row-1, col),self.max_path_helper(row, col-1), self.max_path_helper(row-1, col-1)) + self.board[row][col]

    # Metodo helper que llama al metodo max_path_helper indicandole la posicion del final
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