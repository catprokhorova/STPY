'''
«Теория вероятностей – 2»

Требуется смоделировать игру против лотерейного автомата типа "777". 
Игрок платит 1 руб, после чего выпадает случайное целое число, 
равномерно распределённое от 0 до 999 (np.random.randint). 
При некоторых значениях числа игрок получает выигрыш:
777: 200 руб.
999: 100 руб.
555: 50 руб.
333: 15 руб.
111: 10 руб.
*77: 5 руб.
**7: 3 руб.
*00: 2 руб.
**0: 1 руб.
где * – любая цифра.
Задание: рассчитайте математическое ожидание суммы выигрыша.

Код для студента:

import numpy as np

# trials - список из 1 млн. целых чисел от 0 до 999
# генерируется отдельно в тестовом файле
def monte_carlo(trials):
    # словарь, содержащий выигрышные комбинации и сумму выигрыша
    # случаи с * следует обработать в цикле с помощью
    # операции взятия остатка от деления (%)
    score = {
        999: 100,
        777: 200,
        555: 50,
        333: 15,
        111: 10
    }
    # сумма выигрыша      
    balance = 0

    for i in ...:
        ...

    res = ...
    return res

if __name__ == '__main__':
    np.random.seed(42)
    trials = np.random.randint(0, 1000, 10000000)
    print(monte_carlo(trials))
'''

# Код эксперта:

import numpy as np

# trials - список из 1 млн. целых чисел от 0 до 999
# генерируется отдельно в тестовом файле
def monte_carlo(trials):

    score = {
        999: 100,
        777: 200,
        555: 50,
        333: 15,
        111: 10
    }
    balance = 0
    
    for i in trials:
        value = score.get(i)
        if value:
            balance += value
        elif i % 100 == 77:
            balance += 5
        elif i % 10 == 7:
            balance += 3
        elif i % 100 == 0:
            balance += 2
        elif i % 10 == 0:
            balance += 1

    res = round(balance / len(trials), 5)
    return res