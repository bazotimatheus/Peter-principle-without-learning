import pandas as pd

from peter.config import *
from peter.misc import *

def hire(dataset):
  for current_level in range(1, NUM_LEVELS + 1):
    number_agents_current_level = dataset.query('level == @current_level').shape[0]
    
    while number_agents_current_level < MAX_NUMBER_AGENTS[current_level - 1]:
      level = current_level
      age = generate_age(25, 5)
      competence = generate_competence(7, 2)
      
      data = {'level' : [level], 'age' : [age], 'competence' : [competence]}
      new_agent = pd.DataFrame(data)
      dataset = pd.concat([dataset, new_agent])
      number_agents_current_level = dataset.query('level == @current_level').shape[0]
  dataset = reset_idx(dataset)
  return dataset
