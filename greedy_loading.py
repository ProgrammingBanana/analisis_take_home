class GreedyLoading():
    # Constructor de GreedyLoading
    def __init__(self, carts, weights):
        self.carts = carts # Lista de carros ordenada descendentemente
        self.weights = weights # Lista de pesos ordenada descendentemente
        self.cart_weights = [] # Lista vacia
    
    def print_cart_weights(self):
        # Los carros y sus cargas se guardan en un diccionario,  y para poder imprimirlos se deben iterar por
        # los pares de "keys" y "values", el key siendo el carro y el value siendo la lista de cargas para cada carro,
        # y por cada carro iteramos por su lista de pesos para imprimir el carro y su peso
        for cart, weights in zip(self.carts,self.cart_weights):
            print(str(cart) +"-> (", end=" ")
            for i in range(len(weights)):
                if i != len(weights)-1:
                    print(str(weights[i]) +", ", end=" ")
                else:
                    print(str(weights[i]), end=" ")
            print(")")


    def greedy_load(self, cart):
        """ Aplica un algoritmo greedy para maximizar los pesos por carros y genera una lista de listas de pesos contenida en cart_weights
            ([[], [], [], ..., []]).  Por cada vez que se llama este metodo se anade una lista vacia al final de cart_weights

        Args:
            cart (int): Capacidad maxima del carro actual
        """
        # Accumulador de peso
        cart_weight = 0

        # Anade una lista vacia al final de cart_weights
        # Al final del metodo esta lista interior contendra los elementos que 
        # deberia cargar el carro correspondiente al indice donde se encuentra la lista 
        self.cart_weights.append([])
        
        index = 0
        while index < len(self.weights):
            # Si la suma del peso en el indice actual y el acumulador es igual al peso maximo
            if cart_weight + self.weights[index] == cart:
                # Añade el peso en el indice actual de la lista de pesos (self.weights) a la lista atada al carro en cart_weights
                # Como la lista atada fue la ultima en anadirse la accesamos usando -1 como el indice
                self.cart_weights[-1].append(self.weights[index])
                self.weights.pop(index) # Saca el peso de la lista de peso para no volver a contarlo
                break # Para el loop
            # Si el acumulador mas el peso en el indice actual en la lista de peso es menor que el peso maximo
            elif cart_weight + self.weights[index] < cart:
                # Añade el peso en el indice actual de la lista de pesos (self.weights) a la lista atada al carro en cart_weights 
                # Como la lista atada fue la ultima en anadirse la accesamos usando -1 como el indice
                self.cart_weights[-1].append(self.weights[index])
                # Suma el peso actual en la lista de pesos al acumulador
                cart_weight += self.weights[index]
                # Elimina el peso que acaba de verificar de la lista
                self.weights.pop(index)
                # Como pop elimina el elemento en el indice que se le manda, ahora self.weights[index] apuntaria al proximo valor de peso
                # Si no se reduce index en la proxima iteracion del loop no se consideraria el peso del elemento que le seguia al que se elimino
                index -= 1
            index += 1
            

    def load(self):
        """ Este metodo viaja por la lista de carros y por cada carro hace llamada al 
            metodo greedy_loading que se encarga preparar los carros y sus cargas.
            Luego imprime los carros y sus cargas en orden decendente
        """

        # Por cada carro en el arreglo de carts, que esta ordenado de forma descendente llamamos al metodo greedy_load
        # Mandando como argumento el peso maximo del carro actual. 
        for i in range(len(self.carts)):
            self.greedy_load(self.carts[i])

        self.print_cart_weights() # Imprime el diccionario
        


if __name__ == "__main__" :
    carts = list(map(int,input().split()))
    weights = list(map(int, input().split()))
    carts.pop(0)
    cart_loading = GreedyLoading(sorted(carts, reverse=True), sorted(weights, reverse=True))
    cart_loading.load()