
#  Задача 3
#  Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
#  Результат проверки вывести на консоль
#  Если номер месяца некорректен - сообщить об этом

user_input = input('Введите номер месяца: ')
month = int(user_input)
print('Вы ввели', month)

if month in [1, 3, 5, 7, 8, 10, 12]:
    print('В этом месяце 31 день')

elif month in [4, 6, 9, 11]:
    print('В этом месяце 30 дней')

elif month in [2]:
    print('В этом месяце 28 дней')

else:
    print('Номер месяца некорректен')



# Отлично!
# Можно еще вот так!
# Решение 2
import calendar as cl  # используем модуль для получения функции

year_input = input("Введите год: ")
month_input = input("Введите номер месяца: ")

year = int(year_input)
month_ = int(month_input)
print(cl.monthrange(year, month_))
