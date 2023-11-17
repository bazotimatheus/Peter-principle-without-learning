from random import randint
import pandas as pd

from peter.misc import reset_idx, generate_competence
from peter.config import *

def promote(dataset, strategy, hypothesis):
  for current_level in range(2, 7):
    upper_level = current_level - 1
    current_level_df = dataset.loc[dataset['level'] == current_level]
    upper_level_df = dataset.loc[dataset['level'] == upper_level]

    while (upper_level_df.shape[0] < MAX_NUMBER_AGENTS[upper_level - 1]) and (not current_level_df.empty):
      if strategy == 'best':
        selected_row = current_level_df.loc[current_level_df['competence'] == current_level_df['competence'].max()].head(1)
      elif strategy == 'worst':
        selected_row = current_level_df.loc[current_level_df['competence'] == current_level_df['competence'].min()].head(1)
      elif strategy == 'random':
        selected_row = current_level_df.sample(n=1)

      if isinstance(selected_row, pd.Series):
        if hypothesis == 'peter':
          dataset.at[selected_row.name, 'competence'] = generate_competence(7, 2)
        elif hypothesis == 'common':
          new_competence = selected_row['competence'] * randint(9, 11) / 10
          dataset['competence'] = min(new_competence, 10)

      if not selected_row.empty:
        selected_idx = selected_row.index[0]
        dataset.at[selected_idx, 'level'] += 1

      current_level_df = dataset.loc[dataset['level'] == current_level]
      upper_level_df = dataset.loc[dataset['level'] == upper_level]
    
      dataset.sort_values(['level'], inplace=True)
      dataset = reset_idx(dataset)
    # end while
  # end for
  return dataset
