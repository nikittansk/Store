from product import Product

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
