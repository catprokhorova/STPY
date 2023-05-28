import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from main import drawing

df = pd.read_csv('Visualization/USD_EUR.csv')
def expert(df):
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

def get_attr(gcf):
    res = {}
    res['line1'] = gcf.get_axes()[0].__dict__['_children'][0]
    res['line2'] = gcf.get_axes()[0].__dict__['_children'][1]
    res['title'] = gcf.get_axes()[0].title.__dict__['_text']
    res['xlabel'] = gcf.get_axes()[0].xaxis.__dict__['label'].__dict__['_text']
    res['ylabel'] = gcf.get_axes()[0].yaxis.__dict__['label'].__dict__['_text']
    res['xgrid'] = gcf.get_axes()[0].xaxis.__dict__['_major_tick_kw']['gridOn']
    res['ygrid'] = gcf.get_axes()[0].yaxis.__dict__['_major_tick_kw']['gridOn']
    try:
        res['line_col_1'] = gcf.get_axes()[0].__dict__['_children'][0].__dict__['_color']
        res['line_col_2'] = gcf.get_axes()[0].__dict__['_children'][1].__dict__['_color']
        res['line_lbl_1'] = gcf.get_axes()[0].__dict__['_children'][0].__dict__['_label']
        res['line_lbl_2'] = gcf.get_axes()[0].__dict__['_children'][1].__dict__['_label']
    except KeyError:
        pass
    res['legend'] = (gcf.get_axes()[0].__dict__['legend_'].__dict__['_legend_title_box']
                    .__dict__['_text'].__dict__['_text'])
    return res

st = get_attr(drawing(df))
ex = get_attr(expert(df))

def test_type():
    assert isinstance(st['line1'], Line2D), 'График должен быть линией'
    assert isinstance(st['line2'], Line2D), 'График должен быть линией'

def test_title():
    assert st['title'] == ex['title'], 'Задайте заголовок графика'

def test_x_label():
    assert st['xlabel'] == ex['xlabel'], 'Задайте заголовок оси Х'

def test_y_label():
    assert st['ylabel'] == ex['ylabel'], 'Задайте заголовок оси У'

def test_x_grid():
    assert st['xgrid'] == ex['xgrid'], 'Уберите направляющие с оси Х'

def test_y_grid():
    assert st['ygrid'] == ex['ygrid'], 'Оставьте направляющие у оси У'

def test_line_col():
    assert st['line_col_1'] == ex['line_col_1'], 'Задайте цвет USD "blue"'
    assert st['line_col_2'] == ex['line_col_2'], 'Задайте цвет EUR "red"'

def test_line_lbl():
    assert st['line_lbl_1'] == ex['line_lbl_1'], 'Задайте label для USD'
    assert st['line_lbl_2'] == ex['line_lbl_2'], 'Задайте label для EUR'

def test_legend():
    assert st['legend'] == ex['legend'], 'Добавьте заголовок легенды на график'

"""
Круто было бы, но meh:
import cv2
import numpy as np

st_img = cv2.imread('Visualization/student.png')
ex_img = cv2.imread('Visualization/expert.png')

st_img = cv2.cvtColor(st_img, cv2.COLOR_BGR2GRAY)
ex_img = cv2.cvtColor(ex_img, cv2.COLOR_BGR2GRAY)

def mean_sqrt_error(img_1, img_2):
    h, w = img_1.shape
    diff = cv2.subtract(img_1, img_2)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    return mse

def test():
    assert mean_sqrt_error(st_img, ex_img) == 0.0
"""
