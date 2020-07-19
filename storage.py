import csv
from storageproduct import StorageProduct
from typing import List
from storageitem import StorageItem
import datetime
import json

class Storage:
    __StorageProducts: List[StorageProduct] = []
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
                self.__StorageProducts.append(string)
        self.readFileCsvResult()
        self.updateCsvFile()
        self.writeCsvStorage()


    def readFileCsvResult(self):
        with open('result.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            resultList = list(spamreader)
            for d in resultList:
                if resultList.index(d) == 0:
                    continue
                self.__result.append(d)


    def updateCsvFile(self):
        for p in self.__result:
            if int(p[1])<0:
                print("Файл не валидный")
                break
            f = list(filter(lambda st: st.id == int(p[0]), self.__StorageProducts))[0]
            f.stock -= int(p[1])


    def writeCsvStorage(self):
        with open('storage.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';')
            spamwriter.writerow(['ID', 'Stock', 'Name', 'Price', 'Period'])
            for s in self.__StorageProducts:
                spamwriter.writerow([s.id, s.stock, s.name, s.price, s.period])
            for p in self.__StorageProducts:
                print(p)


    def addProduct(self, id, stock, name, price, period):
        newItem = StorageProduct(id, stock, name, price, period)
        if newItem.stock > 0:
            self.__StorageProducts.append(newItem)
            self.writeCsvStorage()
            self.writeJsonFile()
        else:
            print("Не верное кол-во товара")


    def remove(self, productId):
        foundStorageProduct = next((i for i in self.__StorageProducts if i.id == productId), None)
        self.__StorageProducts.remove(foundStorageProduct)
        self.writeCsvStorage()
        self.writeJsonFile()

    def changeQty(self, productId, newQty, newPrice):
        foundStorageProduct = next((i for i in self.__StorageProducts if i.id == productId), None)
        if newQty > 0 or newPrice > 0:
            foundStorageProduct.stock = newQty
            foundStorageProduct.price = newPrice
            self.writeCsvStorage()
            self.writeJsonFile()
        else:
            print("Команда не выполнена")


    def writeJsonFile(self):
        jsonObjects = []
        now = datetime.datetime.now()
        newStorages = list(filter(lambda st: (st.stock > 0 and (st.period == now.strftime("%m") or st.period == '')), self.__StorageProducts))
        for item in newStorages:
            productItem = {'id': item.id, 'name': item.name, 'stock': item.stock, 'price': item.price}
            jsonObjects.append(productItem)
        with open('products.json', 'w') as write_file:
            json.dump(jsonObjects, write_file)