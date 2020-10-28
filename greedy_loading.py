from collections import defaultdict

class GreedyLoading():
    def __init__(self, carts, weights):
        self.carts = carts
        self.weights = weights
        self.cart_weights = defaultdict(list)
    
    def print_dict(self):
        for cart, weights in self.cart_weights.items():
            print(str(cart) +"-> (", end=" ")
            for i in range(len(weights)):
                if i != len(weights)-1:
                    print(str(weights[i]) +", ", end=" ")
                else:
                    print(str(weights[i]), end=" ")
            print(")")


    def greedy_load(self, cart):
        cart_weight = 0
        cart_weight_dict = {}
        cart_weight_dict.update({cart: []})
        index = 0
        while index < len(self.weights):
            if cart_weight + self.weights[index] == cart:
                self.cart_weights[cart].append(self.weights[index])
                cart_weight += self.weights[index]
                self.weights.pop(index)
                break
            elif cart_weight + self.weights[index] < cart:
                self.cart_weights[cart].append(self.weights[index])
                cart_weight += self.weights[index]
                self.weights.pop(index)
                index -= 1
            index += 1

        return cart_weight_dict
            

    def load(self):
        for cart in self.carts:
            self.greedy_load(cart)

        self.print_dict()
        


if __name__ == "__main__" :
    carts = list(map(int,input().split()))
    weights = list(map(int, input().split()))
    carts.pop(0)
    cart_loading = GreedyLoading(sorted(carts, reverse=True), sorted(weights, reverse=True))
    cart_loading.load()
