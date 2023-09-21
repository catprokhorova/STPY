import pytest
import numpy as np
from scipy import stats
from Visualization.main2 import interval


def seed():
  n = np.random.choice(range(30,50))
  mean = np.random.choice(range(50,71))
  sig = np.random.choice(range(5,16))
  conf = np.random.choice([0.90, 0.95, 0.98, 0.99, 0.999])
  return n, mean, sig, conf


params = seed()


def expert(n, mean, sig, conf):
  h = sig * stats.norm.ppf((1 + conf)/2)/np.sqrt(n)
  return (mean+h)-(mean-h)


def test_1():
  assert interval(*params) == expert(*params)


def test_2():
  assert interval(*params) == expert(*params)


def test_3():
  assert interval(*params) == expert(*params)