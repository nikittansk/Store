class Product:
    def __init__(self, id: int, name: str, price: int, stock: int):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
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
t2 = Product(2, 'Твикс', 35, 10)
t3 = Product(3, 'Сникерс', 42, 53)
products = [t, t2, t3]

for p in products:
    print(p)

class Cart:
    products = []

    def add(self, id: int, name: str, price: int, stock: int):
        return products.append()











