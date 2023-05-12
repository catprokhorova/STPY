import pytest
import numpy as np
from main2 import monte_carlo

def seed(num):
    np.random.seed(num)
    return np.random.randint(0, 1000, 10000000)

def expert(trials):

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

def test_1():
    assert monte_carlo([999]) == 100, 'Условие для 999 реализовано некорректно'
    assert monte_carlo([777]) == 200, 'Условие  для 777 реализовано некорректно'
    assert monte_carlo([555]) == 50, 'Условие для 555 реализовано некорректно'
    assert monte_carlo([333]) == 15, 'Условие для 333 реализовано некорректно'
    assert monte_carlo([111]) == 10, 'Условие для 111 реализовано некорректно'
    assert monte_carlo([677]) == 5, 'Условие для *77 реализовано некорректно'
    assert monte_carlo([667]) == 3, 'Условие для **7 реализовано некорректно'
    assert monte_carlo([100]) == 2, 'Условие для *00 реализовано некорректно'
    assert monte_carlo([10]) == 1, 'Условие для **0 реализовано некорректно'

def test_2():
    assert monte_carlo(seed(42)) == expert(seed(42))

def test_3():
    assert monte_carlo(seed(13)) == expert(seed(13))

def test_4():
    assert monte_carlo(seed(7)) == expert(seed(7))