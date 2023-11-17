from random import gauss

from peter.config import *

def generate_age(mean, std_dev):
  is_valid = False
  while is_valid == False:
    age = int(gauss(mean, std_dev))
    if age > MIN_AGE and age < MAX_AGE:
      is_valid = True
  return age

def generate_competence(mean, std_dev):
  is_valid = False
  while is_valid == False:
    competence = gauss(mean, std_dev)
    if competence > 0 and competence <= MAX_COMPETENCE:
      is_valid = True
  return competence

def reset_idx(dataset):
  indexes = list(range(1, dataset.shape[0] + 1))
  dataset.reset_index(drop=True, inplace=True)
  dataset.index = indexes
  return dataset


def age(dataset):
  dataset['age'] += 1
  return dataset
