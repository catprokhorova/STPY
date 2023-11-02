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

@pytest.mark.parametrize(
        'trials, result', 
        [[[999], 100], [[777], 200], [[555], 50], [[333], 15], 
         [[111], 10], [[677], 5], [[667], 3], [[100], 2], [[10], 1]]
)
def test_conditions(trials, result):
    assert monte_carlo(trials) == result,  f'Условие для {trials} реализовано некорректно'

@pytest.mark.parametrize(
        'num', [42, 13, 7]
)
def test_result(num):
    assert monte_carlo(seed(num)) == expert(seed(num))
