from product import Product

class StorageItem(Product):
    def __init__(self, id: int, name: str, price: int, stock: int, period):
        self.__period = period
        super(StorageItem, self).__init__(id, name, price, stock)

    @property
    def period(self):
        return self.__period

    def __str__(self):
        return 'Номер товара:{:<2} Название:{:<15} Цена:{:<4} Доступное количество:{:<4} Период:{:<7}'.format(self.id, self.name, self.price, self.stock, self.__period)