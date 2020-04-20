class Product:
    def __init__(self, id, name, price, stock):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price in range(0, 9999999999999999999999):
            self.__price = price
        else:
            price('Недопустимое значение')

    @property
    def stock(self):
        return self.__stock
    
    # def display_info(self):
    #     print(self.__str__())

    def __str__(self):
        return 'Номер товара:{} \tНазвание:{} \tЦена:{} \tКоличество:{}'.format(self.__id, self.__name, self.__price, self.__stock)
    
t = Product(1, 'Лейс', 100, 500)
t.price = -1000
print(t)



