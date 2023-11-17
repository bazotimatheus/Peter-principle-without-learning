from peter.config import *

def calculate_max_efficiency(dataset):
  max_efficiency = 0
  total_agents = dataset.shape[0]
  levels = [1, 2, 3, 4, 5, 6]

  counts = [dataset.query(f'level == {level}').shape[0] for level in levels]

  NiRi = sum(count * rate for count, rate in zip(counts, LEVEL_RESPONSIBILITY))

  max_efficiency = 10 * NiRi / total_agents
  return max_efficiency

def calculate_global_efficiency(dataset):
  global_efficiency = 0

  total_agents = dataset.shape[0]

  levels = [1, 2, 3, 4, 5, 6]

  competency_sums = [dataset.query(f'level == {level}')['competence'].sum() for level in levels]

  max_efficiency = calculate_max_efficiency(dataset)

  CiRi = sum(competency_sum * rate for competency_sum, rate in zip(competency_sums, LEVEL_RESPONSIBILITY))

  global_efficiency = (CiRi * 100) / (max_efficiency * total_agents)
  return global_efficiency
