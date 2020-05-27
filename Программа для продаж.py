import json
import csv

from product import Product
from cart import Cart
from cart import CartItem





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



print('К оплате:', cart.getTotalPrice(), 'руб.')


# 1 - сделать так, чтобы функция addProduct в классе Cart могла принимать не только продукт, но и его количество сразу.    
# 2 - добавить проверки на количество, а где не надо - убрать.    Сделано
# 3 - проставить типы, где нужно, разобраться как дать тип списку объектоав (cartItems)    Сделано
# 4 - вделить логику (классы Product, CartItem, Cart) в отдельнвый модуль (файл).          СДЕЛАНО
