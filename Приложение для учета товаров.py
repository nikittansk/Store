from product import Product

import csv


class Storage(Product):
    def __init__(self, period):
        self.__period = period

    @property
    def period(self):
        return self.__period


# Чтение файла склада
storage = []

with open('storage.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for d in spamreader:
        storage.append(d)

# Чтение отчета покупки
result = [] 

with open('result.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for d in spamreader:
        result.append(d)


print()





# Задание:
# 1. Можно ли чтение этих двух файлов записать как то в одну функцию?








