'''
«Теория вероятностей – 1»

Сотрудники отдела маркетинга полагают, что в ближайшее время
ожидается рост спроса на продукцию фирмы. Вероятность этого они оценивают в 80% (P(B1)).
Консультационная фирма, занимающаяся прогнозом рыночной ситуации, подтвердила
предположение о росте спроса. Положительные прогнозы консультационной фирмы
сбываются с вероятностью 95% (P(A|B1)), а отрицательные – с вероятностью 99% (P(A|B2)). 
Какова вероятность того, что рост спроса действительно произойдет?

Код для студента:

def full_probability():
    # вероятность положительного прогноза о росте (P(B1)):
    p_b1 = ...
    # вероятность отрицательного прогноза о росте (P(B2)):
    p_b2 = ...
    # условные вероятности (P(A|B1) и P(A|B2)):
    p_a_b1 = ...
    p_a_b2 = ...
    # вероятность события A (P(A)):
    p_a = ...
    return p_a
'''

# Код эксперта:

def full_probability():
    # вероятность положительного прогноз о росте (P(B1)):
    p_b1 = 0.8
    # вероятность отрицательного прогноз о росте (P(B2)):
    p_b2 = 1 - p_b1
    # условные вероятности (P(A|B1) и P(A|B2)):
    p_a_b1 = 0.95
    p_a_b2 = 0.99
    # вероятность события A (P(A)):
    p_a = p_a_b1 * p_b1 + p_a_b2 * p_b2
    return p_a

if __name__ == '__main__':
    print(full_probability())

'''
Правильный ответ:
0.958
'''