import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from main2 import drawing

df = pd.read_csv('Visualization/height_rus.csv')
def expert(df):
    plt.figure()
    plt.hist(df['Boys'], color='blue', label='мальчики')
    plt.hist(df['Girls'], color='red', alpha=0.7, label='девочки')
    plt.xlabel('рост')
    plt.title('Распределение роста девочек и мальчиков')
    plt.legend(title='Пол:')
    return plt.gcf()

def get_attr(gcf):
    res = {}
    res['hist1'] = gcf.get_axes()[0].__dict__['_children'][0]
    res['hist2'] = gcf.get_axes()[0].__dict__['_children'][-1]
    res['title'] = gcf.get_axes()[0].title.__dict__['_text']
    res['xlabel'] = gcf.get_axes()[0].xaxis.__dict__['label'].__dict__['_text']
    res['xgrid'] = gcf.get_axes()[0].xaxis.__dict__['_major_tick_kw']['gridOn']
    res['ygrid'] = gcf.get_axes()[0].yaxis.__dict__['_major_tick_kw']['gridOn']
    try:
        res['hist_lbl_1'] = gcf.get_axes()[0].__dict__['_children'][0].__dict__['_label']
        res['hist_lbl_2'] = gcf.get_axes()[0].__dict__['_children'][10].__dict__['_label']
        res['alpha1'] = gcf.get_axes()[0].__dict__['_children'][0].__dict__['_alpha']
        res['alpha2'] = gcf.get_axes()[0].__dict__['_children'][-1].__dict__['_alpha']
    except KeyError:
        pass
    res['legend'] = (gcf.get_axes()[0].__dict__['legend_'].__dict__['_legend_title_box']
                    .__dict__['_text'].__dict__['_text']) #works
    return res

st = get_attr(drawing(df))
ex = get_attr(expert(df))

def test_type():
    assert isinstance(st['hist1'], Rectangle), 'Изобразите гистограмму'
    assert isinstance(st['hist2'], Rectangle), 'Изобразите гистограмму'

def test_title():
    assert st['title'] == ex['title'], 'Задайте заголовок графика'

def test_x_label():
    assert st['xlabel'] == ex['xlabel'], 'Задайте заголовок оси Х'

def test_alpha():
    assert st['alpha1'] == ex['alpha1'], 'Оставьте эту гистограмму непрозрачной'
    assert st['alpha2'] == ex['alpha2'], 'Задайте непрозрчность гистограммы 0.7'

def test_hist_lbl():
    assert st['hist_lbl_1'] == ex['hist_lbl_1'], 'Задайте label для мальчиков'
    assert st['hist_lbl_2'] == ex['hist_lbl_2'], 'Задайте label для девочек'

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
