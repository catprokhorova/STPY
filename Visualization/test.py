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