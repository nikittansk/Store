from storageproduct import StorageProduct
from typing import List

class Storage:
    __StorageProduct: List[StorageProduct] = []

    def addProduct(self, ProductId, ProductName, ProductPeriod, SoldQuanity = 1, ProductPrice = 1):
        NewItem = StorageProduct(ProductId, SoldQuanity, ProductName, ProductPrice, ProductPeriod)
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