from peter.misc import reset_idx
from peter.config import *

def layoff(dataset):
  not_layoffed = dataset.query('competence >= 4.0')
  not_layoffed = not_layoffed.query('age <= 65')
  not_layoffed = reset_idx(not_layoffed)
  return not_layoffed
