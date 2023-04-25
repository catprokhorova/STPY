'''
«Расчёт базовых статистик – 2»

Мы собрали информацию о температуре за 30 дней в Цельсиях в городе N.
Рассчитайте базовые статистики:
максимальную величину,
минимальную величину, 
размах, 
дисперсию,
среднее,
медиану,
моду.
ВСЕ ЗНАЧЕНИЯ ПРИВЕСТИ К ЦЕЛОМУ ЧИСЛУ.

Код для студента:

import pandas as pd

temperature = [13, 15, 18, 17, 15, 13, 16, 18, 14, 11,
               14, 17, 11, 4, 6, 9, 11, 7, 7, 11, 
               13, 16, 15, 15, 18, 11, 10, 9, 12, 11]

t = pd.Series(temperature)

min_ = ...
max_ = ...
range_ = ...
disp = ...
mean = ...
median = ...
mode = ...
print(min_, max_, range_, disp, mean, median, mode, sep='\n')
'''

# Код эксперта:

import pandas as pd

temperature = [13, 15, 18, 17, 15, 13, 16, 18, 14, 11,
               14, 17, 11, 4, 6, 9, 11, 7, 7, 11, 
               13, 16, 15, 15, 18, 11, 10, 9, 12, 11]

t = pd.Series(temperature)

min_ = t.min()
max_ = t.max()
range_ = max_ - min_
disp = round(t.var())
mean = round(t.mean())
median = round(t.median())
mode = round(t.mode()[0])
print(min_, max_, range_, disp, mean, median, mode, sep='\n')

'''
Правильный ответ:

4
18
14
14
13
13
11
'''