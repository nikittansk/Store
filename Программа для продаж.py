import json
import csv

from product import Product
from cart import Cart
#from cartitem import CartItem



data = []

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
    
    foundProduct = next((i for i in products if i.id == productId), None)

    if foundProduct == None:
        print("Продукта с таким ID не существует")
        continue
   
    productQty = int(input("Введите количество: ")) 

    cart.addProduct(foundProduct, productQty)


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
# 5 - Если убрать с функции getTotalPrice условия, то будет происходить подсчет товара если он превышает кол-во имеющегося.  


#30 05
# 1 - Инкапсюлация для CartItems в class Cart - сделана
# 2 - Вынести отдельно модуль CartItem - сделано
# 3 - Добавить проверку в addProduct - сделано 


#Вопросы
# 1 - Праверить правильно ли я прописал взаимодецствие модулей и как не запутать при прописании к какому файлу какой import писать
# 2 - Почему если не прописывать условия в функции addProduct, то changeQty не работает? (Это потому что у нас прописано cart.addProduct? Если бы было прописано cart.changeQty тогда было бы все ок?) 
