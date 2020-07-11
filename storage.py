import csv
from storageproduct import StorageProduct
from typing import List
from storageitem import StorageItem
import datetime
import json

class Storage:
    __StorageProduct: List[StorageProduct] = []
    __result = []
    __newStorages = []

    
    def fileReaderCsvStorage(self):
        with open('storage.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            resultList = list(spamreader)
            for d in resultList:
                if resultList.index(d) == 0:
                    continue
                string = StorageItem(int(d[0]), d[2], int(d[3]), int(d[1]), d[4])
                self.__StorageProduct.append(string)
        self.fileReaderCsvResult()
        self.fileUpdateCsv()
        self.fileWriterCsv()


    def fileReaderCsvResult(self):
        with open('result.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            resultList = list(spamreader)
            for d in resultList:
                if resultList.index(d) == 0:
                    continue
                self.__result.append(d)


    def fileUpdateCsv(self):
        for p in self.__result:
            if int(p[1])<0:
                print("Файл не валидный")
                break
            f = list(filter(lambda st: st.id == int(p[0]), self.__StorageProduct))[0]
            f.stock -= int(p[1])


    def fileWriterCsv(self):
        with open('storage.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';')
            spamwriter.writerow(['ID', 'Stock', 'Name', 'Price', 'Period'])
            for s in self.__StorageProduct:
                spamwriter.writerow([s.id, s.stock, s.name, s.price, s.period])
            for p in self.__StorageProduct:
                print(p)


    def addProduct(self, id, stock, name, price, period):
        newItem = StorageProduct(id, stock, name, price, period)
        if newItem.stock > 0:
            self.__StorageProduct.append(newItem)
            self.fileWriterCsv()
            self.fileWriterJson()
        else:
            print("Не верное кол-во товара")


    def remove(self, productId):
        foundCartItem = next((i for i in self.__StorageProduct if i.id == productId), None)
        self.__StorageProduct.remove(foundCartItem)
        self.fileWriterCsv()
        self.fileWriterJson()

    def changeQty(self, productId, newQty, newPrice):
        foundCartItem = next((i for i in self.__StorageProduct if i.id == productId), None)
        if newQty > 0 or newPrice > 0:
            foundCartItem.stock = newQty
            foundCartItem.price = newPrice
            self.fileWriterCsv()
            self.fileWriterJson()
        else:
            print("Команда не выполнена")


    def fileWriterJson(self):
        now = datetime.datetime.now()
        newStorages = list(filter(lambda st: (st.stock > 0 and (st.period == now.strftime("%m") or st.period == '')), self.__StorageProduct))
        for item in newStorages:
            productItem = {'id': item.id, 'name': item.name, 'stock': item.stock, 'price': item.price}
            self.__StorageProduct.append(productItem)
        with open('products.json', 'w') as write_file:
            json.dump(self.__StorageProduct, write_file)