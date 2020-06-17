from cartitem import CartItem
from typing import List    #  from typing import List, Set, Tuple, Dict


class Cart:
    __cartItems: List[CartItem] = []

    def addProduct(self, product, qty = 1):
        newItem = CartItem(product, qty)
        if newItem.qty <= newItem.product.stock:
            self.__cartItems.append(newItem)
        else:
            print('Такого кол-ва на складе нету')   

    def remove(self, productId):
        foundCartItem = next((i for i in self.__cartItems if i.product.id == productId), None)
        self.__cartItems.remove(foundCartItem)

    def changeQty(self, productId, newQty):
        foundCartItem = next((i for i in self.__cartItems if i.product.id == productId), None)
        for i in self.__cartItems:
            if newQty <= i.product.stock:
                foundCartItem.qty = newQty
            else:
                print('Такого кол-ва на складе нету')

    
    def getTotalPrice(self):
        total = 0
        for cartItem in self.__cartItems:
            if cartItem.product.stock >= cartItem.qty:
                sum = cartItem.product.price * cartItem.qty
                total = total + sum
        return total

    def getReportData(self):
        result = []
        for item in self.__cartItems:
            result.append([item.product.id, item.qty])
        return result
