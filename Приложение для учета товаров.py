from storage import Storage
from storageitem import StorageItem
from typing import List    #  from typing import List, Set, Tuple, Dict
import csv
import json
import datetime



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

# Чтение отчета покупки
result = [] 

with open('result.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    resultList = list(spamreader)
    for d in resultList:
        if resultList.index(d) == 0:
            continue
        result.append(d)


# storage.csv - result.csv
for p in result:
    f = list(filter(lambda st: st.id == int(p[0]), storages))[0]
    f.stock -= int(p[1])


# Запись обновленного файла
with open('storage.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(['ID', 'Stock', 'Name', 'Price', 'Period'])
    for s in storages:
        spamwriter.writerow([s.id, s.stock, s.name, s.price, s.period])

for p in storages:
    print(p)

#Услови для создания JSON файла
now = datetime.datetime.now()
newStorages = []
newStorages = list(filter(lambda st:( st.stock > 0 and (st.period == now.strftime("%m") or st.period == '')), storages))


# Создание JSON файла
storagesJSON = []

for item in newStorages:
    productItem = {'id': item.id, 'name': item.name, 'stock': item.stock, 'price': item.price}
    storagesJSON.append(productItem)


with open('products.json', 'w') as write_file:
    json.dump(storagesJSON, write_file)

storage = Storage()

#Товар для расширения ассортимента склада
while True:
    firstInput = input("Введите номер товара: ")
    if(firstInput == 'Все' or firstInput == 'все'):
        break

    productId = int(firstInput)
    productName = input("Введите название товара: ")
    productPrice = int(input("Введите цену товара: "))
    productQty = int(input("Введите кол-во товара: "))
    productPeriod = int(input("Введите период: "))
    storage.addProduct(productId, productName, productPrice, productQty, productPeriod)

print()
# Задание:
# 1. Проверка ID товара при вводе в программе для продаж
# 2. Добавить классы, рефакторинг. Сделано

# Исправить:
# 1. В программе для продаж можно написать кол-во продукта отрицаемое. Сделано





