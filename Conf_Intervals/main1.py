"""
Определение размера выборки

Определите размер необходимой выборки для исследования среднего чека за кофе в городе N, 
если известны следующие параметры:
- погрешность (Δ);
- дисперсия (σ2);
- уровень доверия (1-α).
Ответ округлите до целого.

ВНИМАНИЕ! НЕ УДАЛЯЙТЕ КОД НИЖЕ, А ДОПОЛНИТЕ ЕГО. ФУНКЦИЯ НУЖНА ДЛЯ ПРОВЕРКИ ВАШЕГО РЕШЕНИЯ.

Код для студента:

import numpy as np
from scipy import stats


def sample(delta, sigsqr, conf):
    return ...
"""

#кот, который смог:

import numpy as np
from scipy import stats

def sample(delta, sigsqr, conf):
    return round(np.ceil(sigsqr*(stats.norm.ppf((1 + conf)/2)**2)/(delta**2)))

if __name__ == '__main__':
  print(sample(2, 144, 0.95))
  print(sample(7, 196, 0.95))
  print(sample(9, 289, 0.99))