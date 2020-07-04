from storageitem import StorageItem

class StorageProduct:
    def __init__(self, ProductId, SoldQuanity, ProductName, ProductPrice, ProductPeriod):
        self.__ProductId = ProductId
        self.__SoldQuanity = SoldQuanity
        self.__ProductName = ProductName
        self.__ProductPrice = ProductPrice
        self.__ProductPeriod = ProductPeriod

    @property
    def ProductId(self):
        return self.__ProductId

    @property
    def ProductName(self):
        return self.__ProductName

    @property
    def SoldQuanity(self):
        return self.__SoldQuanity

    @SoldQuanity.setter
    def SoldQuanity(self, SoldQuanity):
        if SoldQuanity > 0:
            self.__SoldQuanity = SoldQuanity
        else:
            print("Такого кол-во не было продано")

    @property
    def ProductPrice(self):
        return self.__ProductPrice

    @ProductPrice.setter
    def ProductPrice(self, ProductPrice):
        if ProductPrice > 0:
            self.__ProductPrice = ProductPrice
        else:
            print("Такой цены нету")

    @property
    def ProductPeriod(self):
        return self.__ProductPeriod

    @ProductPeriod.setter
    def ProductPeriod(self, ProductPeriod):
        if ProductPeriod < 13 or ProductPeriod > 0:
            self.__ProductPeriod = ProductPeriod
        else:
            print("Такого месяца нету")