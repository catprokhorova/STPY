"""
Текст задания:

Вам дан файл USD_EUR.csv с динмикой курса доллара и евро к рублю за 2021 и 2022 годы.
Постройте линейный график, отражающий эту динамику.
Используйте следующие заголовки:
title - 'Динамика курса доллара и евро по пятничкам'
по оси Х - 'пятнички'
по оси У - 'курс валюты в рублях'
легенда - 'валюты:'

Ваш график должен выглядеть так:
*графык*

Код для студента:

import pandas as pd
import matplotlib.pyplot as plt

#данные для визуализации:
df = pd.read_csv('Visualization/USD_EUR.csv')

#функция для тестирования вашего графика:
def drawing(df):
    #задаём размер фигуры:
    plt.figure().set_figwidth(15)
    #отрисуйте линии графика, задайте цаета и labels:
    ...
    ...
    #задайте подпись оси Х:
    ...
    #уберите даты с оси Х:
    ...
    #оставьте направляющие графика у оси У:
    ...
    #задайте подпись оси У:
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

#решение эксперта:
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Visualization/USD_EUR.csv')

def drawing(df):
    plt.figure().set_figwidth(15)
    plt.plot(df['DATE'], df['USD'], color='blue', label='USD')
    plt.plot(df['DATE'], df['EUR'], color='red', label='EUR')
    plt.xlabel('пятнички')
    plt.xticks([])
    plt.grid(axis = 'y')
    plt.ylabel('курс валюты в рублях')
    plt.title('Динамика курса доллара и евро по пятничкам')
    plt.legend(title='валюты:')
    return plt.gcf()
