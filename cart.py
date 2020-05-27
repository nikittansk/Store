from product import Product

from typing import List    #  from typing import List, Set, Tuple, Dict

class CartItem:
    def __init__(self, product, qty):
        self.__qty = qty
        self.__product = product

    @property
    def product(self):
        return self.__product
   
    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, qty):
        if qty > 0:
            self.__qty = qty
        else:
            print('Недопустимое значение')

class Cart:
    cartItems: List[int] = []

    def addProduct(self, product, qty):
        newItem = CartItem(product, qty)
        self.cartItems.append(newItem)

    def remove(self, productId):
        foundCartItem = next((i for i in self.cartItems if i.product.id == productId), None)
        self.cartItems.remove(foundCartItem)

    def changeQty(self, productId, newQty):
        foundCartItem = next((i for i in self.cartItems if i.product.id == productId), None)
        for i in self.cartItems:
            if foundCartItem.qty <= i.product.stock:
                foundCartItem.qty = newQty
            else:
                print('Такого кол-ва на складе нету')

    
    def getTotalPrice(self):
        total = 0
        for cartItem in self.cartItems:
            sum = cartItem.product.price * cartItem.qty
            total = total + sum
        return total

    def getReportData(self):
        result = []
        for item in self.cartItems:
            result.append([item.product.id, item.qty])
        return result
