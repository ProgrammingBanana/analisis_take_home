class RabbitHole():

  # Constructor de la clase RabbitHole
  def __init__(self, board):
    self.board = board
    self.row = len(board)
    self.col = len(board[0])

  def print_burrow(self):
    """ Imprime la matriz
    """
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
    """ Compara x, y, z y  trata de devolver el string que no contenga "*"

    Args:
        x (string): String que devulve la llamada recursiva de que se mueve hacia arriba
        y (string): String que devulve la llamada recursiva de que se mueve hacia izquierda
        z (string): String que devulve la llamada recursiva de que se mueve hacia derecha

    Returns:
        [String]: Si todos son "*" devuelve "*", sino, devuelve el string que no sea "*"
    """
    if x == "*" and y == "*" and z =="*":
        return "*"
    elif x != "*":
        return x
    elif y != "*":
        return y
    else:
        return z
    
  # Dado que el origin diga que viene de la derecha, no verificaras la derecha y si viene de la izquierda no verfica la izquierda
  # Se creo el parametro origin para resolver el problema de recursion infinita.
  def rabbit_path_helper(self, row, col, origin):
    """ Funcion recursiva que encuentra el camino del inicio a la madriguera usando programacion dinamica

    Args:
        row (int): La fila que se esta verificando con el metodo
        col (int): La columna que se esta verificando con el metodo
        origin (string): Indica de donde proviene la llamada anterior para prevenir errores de recursion
                         Si viene de la izquierda la llamada recursiva recibira "left", si viene de la 
                         derecha la llamada recursiva recibira "right y de abajo recibira "down"

    Returns:
        [String]: Devuelve un string de la forma "* -> ... ->(n-1, m-1)" si no hay camino.
                  Devuelve un string de la forma "(0,0) -> (0,1) -> ... ->(n-1,m-1)"
    """
    
    # Si se pasa de los indices posibles o hay un obstaculo en el camino devuelve "*"
    if row < 0 or col < 0 or col >= self.col or self.board[row][col] == 'o':
        return "*"
    elif row == 0 and col == 0: # Devuelve el string "0,0" termina la recursion
        return "(0,0)" 
    else:
        # Estas tres opciones devuelven los mismo una concatenacion de todos los indices que tomo el conejo para llegaar a la madriguera

        # Si vino de la derecha verifica el de arriba y el de la izquierda (no vuelvas a la derecha)
        if origin == "right":
            # Comparamos la llamada recursiva para arriba y la llamada recursiva para 
            # izquierda y mandamos "*" donde mandariamos la llamada recursiva que 
            # volveria a la derecha ya que si volvemos a la derecha causaria problemas de recursion (recursion infinita)
            return self.compare_three(self.rabbit_path_helper(row-1, col, "down"),self.rabbit_path_helper(row, col-1, "right"), "*") + " -> (" +str(row) +"," +str(col) +")"
        # Si vino de la izquierda verifica el de arriba y el de la derecha (no vuelvas a la izquierda)
        elif origin == "left":
            # Comparamos la llamada recursiva para arriba y la llamada recursiva para 
            # la derecha y mandamos "*" donde mandariamos la llamada recursiva que 
            # volveria a la izquierda ya que si volvemos a la izquierda causaria problemas de recursion (recursion infinata)
            return self.compare_three(self.rabbit_path_helper(row-1, col, "down"), "*", self.rabbit_path_helper(row, col+1, "left")) + " -> (" +str(row) +"," +str(col) +")"
        # Dado que no venga de la derecha o la izquierda compara todos los posibles camino 
        else:
            # Esta comparacion ocurre cuando viene de abajo o en la primera llamada recursica y compara las tres posibilidades
            return self.compare_three(self.rabbit_path_helper(row-1, col, "down"), self.rabbit_path_helper(row, col-1, "right"), self.rabbit_path_helper(row, col+1, "left")) + " -> (" +str(row) +"," +str(col) +")"

  def rabbit_path(self):
    """ Este metodo llama al metodo "rabbit_path_helper" el cual devuelve un string del camino que toma el conejo
        Utilizando el string determina si no hay camino. Si hay camino, en el tablero se va marcando cada inidce 
        por el cual pasa con el numero 1

    Returns:
        String : Si no hay camino devuelve "There is no Path.
                 Si ha camino devuelve el camino de la forma "(0,0) -> (0,1) -> ... -> (M-1,N-1)"
    """
    
    # Llama a la funcion recursiva rabbit_path_helper y guarda el string que devuelve en path
    path = self.rabbit_path_helper(self.row-1, self.col-1, "end")

    # Si el string que devolvio rabbit_path_helper tiene asterisco, significa que no hay posible camino.
    if "*" in path:
        self.print_burrow() # Imprime la matriz sin cambio porque no hay camino
        print()
        return "There is no Path" # Devuelve el string "There is no Path"

    # Si hay un camino (no hay asterisco) creamos una lista de los substrings de los pares de indices por
    # donde necesita pasar el conejo replace reemplaza cada instancia del primer caracter por el segundo
    # caracter indicado. Split genera una lista de los substrings que estaban separados por el delimitador 
    # que se manda
    # luego de los replace: "00  01  11 ... n-1m-1" luego del split: ["01", "01", "11", ... "n-1m-1"]
    stripped_path = path.replace(")","").replace("->", "").replace("(","").replace(",","").split("  ")

    #Como stripped_path es una lista con strings de pares de indices que indican camino viajo por cada par de indice
    for indices in stripped_path:
        # Convierto los caracteres de indices a int y los utilizo para en la tabla ir por el camino encontrado y marcandolo con 1
        self.board[int(indices[0])][int(indices[1])] = 1

    self.print_burrow() # Imprime el tablero luego de marcar el camino
    print()
    return path # Devuelve el string del camino que escogio el conejo



if __name__ == "__main__" :
    print("\nRabbit 1 (Example of only down and right movement)")
    arr = [['A', 'o', 'o', 'o'],
            ['A', 'A', 'A', 'A'],
            ['o', 'o', 'A', 'o'],
            ['o', 'A', 'A', 'A'],
            ['o', 'o', 'o', 'A']]

    burrow = RabbitHole(arr)
    print(burrow.rabbit_path())

    print("\nRabbit 2 (Example of all possible movement, left, right and down)")
    arr = [['A', 'A', 'o', 'o'],
            ['o', 'A', 'A', 'A'],
            ['o', 'o', 'o', 'A'],
            ['o', 'A', 'A', 'A'],
            ['A', 'A', 'o', 'o'],
            ['o', 'A', 'A', 'A']]

    burrow = RabbitHole(arr)
    print(burrow.rabbit_path())

    print("\nRabbit 3 (Example of no possible path)")
    arr = [['A', 'A', 'o', 'o'],
            ['o', 'A', 'A', 'A'],
            ['o', 'o', 'o', 'A'],
            ['o', 'A', 'A', 'A'],
            ['o', 'o', 'o', 'o'],
            ['o', 'A', 'A', 'A']]

    burrow = RabbitHole(arr)
    print(burrow.rabbit_path())