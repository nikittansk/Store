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
        if price >= 0:
            self.__price = price
        else:
            print('Недопустимое значение')

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print('Недоступное значение')

    def __str__(self):
        return 'Номер товара:{} \tНазвание:{} \tЦена:{} \tКоличество:{}'.format(self.__id, self.__name, self.__price, self.__stock)
    
t = Product(1, 'Лейс', 100, 500)
print(t)



