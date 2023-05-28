"""
Текст задания:



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

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Visualization/height_rus.csv')

def drawing(df):
    plt.figure()
    plt.hist(df['Boys'], color='blue', label='мальчики')
    plt.hist(df['Girls'], color='red', alpha=0.7, label='девочки')
    plt.xlabel('рост')
    plt.title('Распределение роста девочек и мальчиков')
    plt.legend(title='Подопытные:')
    return plt.gcf()
