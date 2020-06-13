from product import Product
from typing import List    #  from typing import List, Set, Tuple, Dict
import csv


class StorageItem(Product):
    def __init__(self, id: int, name: str, price: int, stock: int, period: str):
        self.__period = period
        super(StorageItem, self).__init__(id, name, price, stock)

    @property
    def period(self):
        return self.__period

    def __str__(self):
        return 'Номер товара:{:<2} Название:{:<15} Цена:{:<4} Доступное количество:{:<4} Период:{:<7}'.format(self.id, self.name, self.price, self.stock, self.__period)


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


for p in storages:
    print(p)





# Задание:
# 1. Можно ли чтение этих двух файлов записать как то в одну функцию?








