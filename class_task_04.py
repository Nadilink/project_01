
#  Задача 4
#  Приведем плейлист песен в виде списка списков
#  Список my_favorite_songs содержит список названий и длительности каждого трека
#  Выведите общее время звучания трех случайных песен в формате
#  Три песни звучат XXX минут
#  Для того, чтобы задавать случайные значения, используйте модуль random 
#  import random
#  random для генерации случайных значений

import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairyrale', 5.28],
    ['Easy', 4.15],
    ['Beautifyl Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02]
]
time_n = []
for i in my_favorite_songs:
    time_n.append(i[1])
    random.shuffle(time_n)
print(f'Три песни звучат {sum(time_n[0:3])}')
 

# print("Три песни звучат ","минут", random.choices(my_favorite_songs, k=3))

# Отлично














