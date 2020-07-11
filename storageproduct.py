from storageitem import StorageItem

class StorageProduct:
    def __init__(self, id: int, stock: int, name, price: int, period):
        self.__id = id
        self.__stock = stock
        self.__name = name
        self.__price = price
        self.__period = period

    @property
    def id(self):
        return self.__id

    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, stock):
        if stock > 0:
            self.__stock = stock
        else:
            print("Заданое кол-во нельзя записать")

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Данная цена не записана")

    @property
    def period(self):
        return self.__period
    
    @period.setter
    def period(self, period):
        if period < 13 or period > 0 or period == None:
            self.__period = period
        else:
            print("Данного месяца нету")

