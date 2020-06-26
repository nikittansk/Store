from product import Product

class CartItem:
    def __init__(self, product, qty):#productId
        self.__qty = qty
        self.__product = product
        #self.__productId = productId

    @property
    def product(self):
        return self.__product

    #@property
    #def productId(self):
        #return  self.__productId

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, qty):
        if qty > 0:
            self.__qty = qty
        else:
            print('Недопустимое значение')
