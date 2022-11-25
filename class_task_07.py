






# Задача 7
# Есть словарь кодов товаров

titles = {
    'Кроссовки тип 3 - Adidas': '100000110',
    'Мячик тип 2 - Adidas': '100000146',
    'Кепка тип 1 - Adidas': '100000149',
    'Ремень тип 2 - Nike': '100000194',
    'Кроссовки тип 3 - Adidas - Adidas - Adidas': '100000224',
    'Шапка тип 5 - Puma': '100000280',
}

# Есть словарь списков словарей количества товаров на складе.

sales = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:

# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

# Вариант 1.

user_input = input('Введите искомый товар: ')
search_result = titles[user_input]

quantity = 0
for dict in sales[search_result]:
    quantity += dict['quantity']

price = 0
for dict in sales[search_result]:

    price += dict['price']
print(f'{user_input} - {quantity} шт, стоимость {price} руб')

# Вариант 2.

for n_titles in titles:
    key_titles = titles[n_titles]
    total_price = 0
    total_quantity = 0
    for quantity_price in sales[key_titles]:
        total_price = total_price + quantity_price["quantity"] * quantity_price["price"]
        total_quantity += quantity_price["quantity"]
    print(n_titles, "-", total_quantity, "шт, стоимостью", total_price, "рублей")







