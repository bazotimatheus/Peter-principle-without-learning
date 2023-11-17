from peter.misc import reset_idx
from peter.config import *

def dismiss(dataset):
  not_dismissed = dataset.query('competence >= 4.0')
  not_dismissed = not_dismissed.query('age <= 65')
  not_dismissed = reset_idx(not_dismissed)
  return not_dismissed
