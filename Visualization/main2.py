"""
Текст задания:

Вам дан файл height_rus.csv, содержащий данные о росте жителей РФ, разделённые по полу.
Постройте график, отражающий распределение роста. Чтобы распределение было лучше видно,
задайте параметр непрозрачности для Series 'Girls' равный 0.7.

Используйте следующие заголовки:
для всего графика - 'Распределение роста девочек и мальчиков'
по оси Х - 'рост'
легенда - 'Пол:'

Код для студента:

import pandas as pd
import matplotlib.pyplot as plt

#данные для визуализации:
df = pd.read_csv('Visualization/height_rus.csv')

#функция для тестирования вашего графика:
def drawing(df):
    plt.figure()
    #отрисуйте гистограммы, задайте цаета, labels и непрозрачность:
    #для мальчиков
    ...
    #для девочек:
    ...
    #задайте подпись оси Х:
    ...
    #озаглавьте график:
    ...
    #добавьте легенду с подписью:
    ...
    return plt.gcf()

#не удалять, не изменять:
if __name__=='__main__':
    drawing(df)
    plt.show()
"""

import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

df = pd.read_csv('Visualization/height_rus.csv')

def drawing(df):
    plt.figure()
    plt.hist(df['Boys'], color='blue', label='мальчики')
    plt.hist(df['Girls'], color='red', alpha=0.7, label='девочки')
    plt.xlabel('рост')
    plt.title('Распределение роста девочек и мальчиков')
    plt.legend(title='Пол:')
    return plt.gcf()
