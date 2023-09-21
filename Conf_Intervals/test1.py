import pytest
import numpy as np
from scipy import stats
from main1 import sample


def seed():
  delta = np.random.choice([1,2,5,7,9])
  sigsqr = np.random.choice([144, 169, 196, 225, 256, 289, 324])
  conf = np.random.choice([0.90, 0.95, 0.99])
  return delta, sigsqr, conf


params = seed()


def expert(delta, sigsqr, conf):
    return np.ceil(sigsqr*(stats.norm.ppf((1 + conf)/2)**2)/(delta**2))


def test_1():
  assert sample(*params) == expert(*params)


def test_2():
  assert sample(*params) == expert(*params)


def test_3():
  assert sample(*params) == expert(*params)