"""
Вычислить возраст человека. Программа принимает с клавиатуры год рождения и выводит возраст на экран.
1.
2.	Пример:
3.	Ваша дата рождения:
4.	1990
5.	Вам 28 лет
6.

"""

start_date = int(input('Введите текущий год: '))
birthday_data = int(input('Введите год рождения: '))
result = start_date - birthday_data
print('Ваш возраст', result, 'лет')