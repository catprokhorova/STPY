"""
Текст задания:
напишем

Код для студента:
напишем
"""

#решение эксперта:
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Visualization/USD_EUR.csv')

plt.figure().set_figwidth(15)
plt.plot(df['DATE'], df['USD'], color='blue', label='USD')
plt.plot(df['DATE'], df['EUR'], color='red', label='EUR')
plt.xlabel('пятнички')
plt.xticks([])
plt.grid(axis = 'y')
plt.ylabel('курс валюты в рублях')
plt.title('Динамика курса доллара и евро по пятничкам')
plt.legend(title='валюты:')
plt.savefig('Visualization/student.png')
# plt.show()