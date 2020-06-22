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

# class FoundStorageItem:
#     def __init__(self, ProductID, SoldQuanity):
#         self.__ProductID = ProductID
#         self.__SoldQuanity = SoldQuanity

#     @property
#     def ProductID(self):
#         return self.__ProductID
   
#     @property
#     def SoldQuanity(self):
#         return self.__SoldQuanity

#     @SoldQuanity.setter
#     def SoldQuanity(self, SoldQuanity):
#         if SoldQuanity > 0:
#             self.__SoldQuanity = SoldQuanity
#         else:
#             print('Недопустимое значение')


# class Storage:
#     __FoundStorageItem: List[FoundStorageItem] = []

#     def addProduct(self, ProductID, SoldQuanity):
#         newItem = FoundStorageItem(ProductID, SoldQuanity)
#         if newItem.SoldQuanity <= newItem.ProductID.stock: # Или должно быть if newItem.SoldQuanity > 0 тогда append
#             self.__FoundStorageItem.append(newItem)

# t = StorageItem(1, "Ментос", 1000, 10, 11)

# s = Storage()

# s.addProduct(t)

# print()
# Чтение файла склада
storages: List[StorageItem] = []

with open('storage.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    resultList = list(spamreader)
    for d in resultList:
        if resultList.index(d) == 0:
            continue
        str = StorageItem(int(d[0]), d[2], int(d[3]), int(d[1]), d[4])
        storages.append(str)
    for p in storages:
        print(p)
print()

# Чтение отчета покупки
result = [] 

with open('result.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    resultList = list(spamreader)
    for d in resultList:
        if resultList.index(d) == 0:
            continue
        result.append(d)
    print(result)

for p in result:
    f = list(filter(lambda st: st.id == int(p[0]), storages))[0]
    f.stock -= int(p[1])

with open('storage.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(['ID', 'Stock', 'Name', 'Price', 'Period'])
    for s in storages:
        spamwriter.writerow([s.id, s.stock, s.name, s.price, s.period])

now = datetime.datetime.now()
newStorages = []
newStorages = list(filter(lambda st:( st.stock > 0 and (st.period == now.strftime("%m") or st.period == '')), storages))

storagesJSON = []

for item in newStorages:
    productItem = {'id': item.id, 'name': item.name, 'stock': item.stock, 'price': item.price}
    storagesJSON.append(productItem)


with open('products.json', 'w') as write_file:
    json.dump(storagesJSON, write_file)

for p in storages:
    print(p)


# Задание:
# 1. Проверка ID товара при вводе в программе для продаж
# 2. Добавить классы, рефакторинг






