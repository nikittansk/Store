from product import Product
from typing import List    #  from typing import List, Set, Tuple, Dict
import csv
import json
import datetime

class StorageItem(Product):
    def __init__(self, id: int, name: str, price: int, stock: int, period):
        self.__period = period
        super(StorageItem, self).__init__(id, name, price, stock)

    @property
    def period(self):
        return self.__period

    def __str__(self):
        return 'Номер товара:{:<2} Название:{:<15} Цена:{:<4} Доступное количество:{:<4} Период:{:<7}'.format(self.id, self.name, self.price, self.stock, self.__period)

class StorageProduct:
    def __init__(self, ProductId, SoldQuanity):
        self.__ProductId = ProductId
        self.__SoldQuanity = SoldQuanity

    @property
    def ProductId(self):
        return self.__ProductId


    @property
    def SoldQuanity(self):
        return self.__SoldQuanity

    @SoldQuanity.setter
    def SoldQuanity(self, SoldQuanity):
        if SoldQuanity > 0:
            self.__SoldQuanity = SoldQuanity
        else:
            print("Ошибка")


class Storage:
    __StorageProduct: List[StorageProduct] = []

    def addProduct(self, ProductId, SoldQuanity = 1):
        NewItem = StorageProduct(ProductId, SoldQuanity)
        if NewItem.SoldQuanity > 0:
            self.__StorageProduct.append(NewItem)
        else:
            print("Команда не выполнена")


    def remove(self, productId):
        foundCartItem = next((i for i in self.__StorageProduct if i.ProductId.id == productId), None)
        self.__StorageProduct.remove(foundCartItem)

    def changeQty(self, productId, newQty):
        foundCartItem = next((i for i in self.__StorageProduct if i.ProductId.id == productId), None)
        if newQty > 0:
            foundCartItem.SoldQuanity = newQty
        else:
            print("Команда не выполнена")
c = StorageItem(1, "Mamba", 1000, 3, 12)
c2 = StorageItem(2, "Pepsi", 33, 100, 1)
s = Storage()

s.addProduct(c)
s.addProduct(c2)

s.remove(1)

s.changeQty(2, -100)

print()

# # Чтение файла склада
# storages: List[StorageItem] = []
#
# with open('storage.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=';')
#     resultList = list(spamreader)
#     for d in resultList:
#         if resultList.index(d) == 0:
#             continue
#         str = StorageItem(int(d[0]), d[2], int(d[3]), int(d[1]), d[4])
#         storages.append(str)
#     for p in storages:
#         print(p)
# print()
#
# # Чтение отчета покупки
# result = []
#
# with open('result.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=';')
#     resultList = list(spamreader)
#     for d in resultList:
#         if resultList.index(d) == 0:
#             continue
#         result.append(d)
#     print(result)
#
# for p in result:
#     f = list(filter(lambda st: st.id == int(p[0]), storages))[0]
#     f.stock -= int(p[1])
#
# with open('storage.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=';')
#     spamwriter.writerow(['ID', 'Stock', 'Name', 'Price', 'Period'])
#     for s in storages:
#         spamwriter.writerow([s.id, s.stock, s.name, s.price, s.period])
#
# now = datetime.datetime.now()
# newStorages = []
# newStorages = list(filter(lambda st:( st.stock > 0 and (st.period == now.strftime("%m") or st.period == '')), storages))
#
# storagesJSON = []
#
# for item in newStorages:
#     productItem = {'id': item.id, 'name': item.name, 'stock': item.stock, 'price': item.price}
#     storagesJSON.append(productItem)
#
#
# with open('products.json', 'w') as write_file:
#     json.dump(storagesJSON, write_file)
#
# for p in storages:
#     print(p)


# Задание:
# 1. Проверка ID товара при вводе в программе для продаж
# 2. Добавить классы, рефакторинг






