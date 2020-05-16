import json
import csv

class Product:
    def __init__(self, id: int, name: str, price: int, stock: int):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print('Недопустимое значение')

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print('Недоступное значение')

    def __str__(self):
        return 'Номер товара:{:<2} Название:{:<15} Цена:{:<4} Доступное количество:{:<4}'.format(self.__id, self.__name, self.__price, self.__stock)

class CartItem:
    def __init__(self, product, qty):
        self.__qty = qty
        self.__product = product

    @property
    def product(self):
        return self.__product
   
    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, qty):
        if qty > 0:
            self.__qty = qty
        else:
            print('Недопустимое значение')

class Cart:
    cartItems = []

    def addProduct(self, product):
        newItem = CartItem(product, 1)
        self.cartItems.append(newItem)

    def remove(self, productId):
        foundCartItem = next((i for i in self.cartItems if i.product.id == productId), None)
        self.cartItems.remove(foundCartItem)

    def changeQty(self, productId, newQty):
        foundCartItem = next((i for i in self.cartItems if i.product.id == productId), None)
        foundCartItem.qty = newQty
    
    def geTotalPrice(self):
        total = 0
        for cartItem in self.cartItems:
            if cartItem.product.stock >= cartItem.qty:
                total = (total + cartItem.product.price) * cartItem.qty
            else:
                print('Такого кол-ва товара на складе нету')
        return total

    def getReportData(self):
        result = []
        for item in self.cartItems:
            result.append([item.product.id, item.qty])
        return result

try:
    with open('products.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
        data = json.load(fh) #загружаем из файла данные в словарь data
except:
    print("Файла не найдено с данными")

products = []

# Доступ к значению в словаре осуществляется с помощью [ключ]
# Например: словарь {"id": 1, "name": "Lays", "price": 100,  "stock": 500 }
# по ключу 'id' мы получим значение 1
for p in data:
    newProduct = Product(p['id'], p['name'], p['price'], p['stock']) 
    products.append(newProduct)

# Вывели ассортимент
for p in products:
    print(p)

cart = Cart()

# Выбор товаров для добавления в корзину
while True: 
    firstInput = input("Введите номер товара: ") 
    if(firstInput == "Все" or firstInput == "все"): 
        break 
    
    productId = int(firstInput)
    productQty = int(input("Введите количество: ")) 

    foundProduct = next((i for i in products if i.id == productId), None)

    cart.addProduct(foundProduct)
    cart.changeQty(productId, productQty)


with open('result.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    report = cart.getReportData()
    spamwriter.writerow(['ProductID', 'SoldQuanity'])
    for d in report:
        spamwriter.writerow(d)




# 1 - сделать так, чтобы функция addProduct в классе Cart могла принимать не только продукт, но и его количество сразу
# 2 - добавить проверки на количество, а где не надо - убрать
# 3 - проставить типы, где нужно, разобраться как дать тип списку объектоав (cartItems)
# 4 - вделить логику (классы Product, CartItem, Cart) в отдельнвый модуль (файл)