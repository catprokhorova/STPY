"""
Текст задания:

Вам дан файл 'gas_sales_2.csv', содержащий данные о продаже газа Южной Корее
за 20 лет. Также дана информация о средней температуре в каждый из месяцев.

Задание:
Рассчитайте коэффициенты корреляции Пирсона и Спирмана для столбцов
'Temperature' и 'Sum'. В библиотеке pandas для этого есть специальный метод. 
(ссылка https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
Используйте любой из полученных коэффициентов, чтобы
определить тип зависимости (положительная или отрицательная) и силу связи.

*табличка с интерпретацией*

Код для студента:

import pandas as pd

df = pd.read_csv('Correlation/gas_sales_2.csv')

#коэф. корреляции Пирсона:
p_coef = ...
    
#коэф. корреляции Спирмана:
s_coef = ...

#определение типа зависимости:
if ...
    print('Тип зависимости — положительная;')
elif ...
    print('Тип зависимости — отрицательная;')
else:
    print('Зависимомсть не обнаружена.')

#определение силы связи
if ...
    print('Очень слабая зависимость')
elif ...
    print('Слабая зависимость')
elif ...
    print('Средняя зависимость')
elif ...
    print('Высокая зависимость')
elif ...
    print('Очень высокая зависимость')

"""

#решение эксперта:
import pandas as pd

df = pd.read_csv('Correlation/gas_sales_2.csv')

p_coef = df[['Sum', 'Temperature']].corr()
s_coef = df[['Sum', 'Temperature']].corr(method='spearman')

if p_coef['Temperature'].to_list()[0] > 0:
    print('Тип зависимости — положительная;')
elif p_coef['Temperature'].to_list()[0] < 0:
    print('Тип зависимости — отрицательная;')
else:
    print('Зависимомсть не обнаружена.')

if 0 < abs(p_coef['Temperature'].to_list()[0]) <= 0.3:
    print('Очень слабая зависимость')
elif 0.3 < abs(p_coef['Temperature'].to_list()[0]) <= 0.5:
    print('Слабая зависимость')
elif 0.5 < abs(p_coef['Temperature'].to_list()[0]) <= 0.7:
    print('Средняя зависимость')
elif 0.7 < abs(p_coef['Temperature'].to_list()[0]) <= 0.9:
    print('Высокая зависимость')
elif 0.9 < abs(p_coef['Temperature'].to_list()[0]) <= 1:
    print('Очень высокая зависимость')

'''
Правильный ответ:

Тип зависимости — отрицательная;
Высокая зависимость
'''
