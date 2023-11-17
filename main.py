import pandas as pd
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

from peter import *

for execution in range(MAX_EXECUTIONS):
  dataset = pd.DataFrame(columns = ['level', 'age', 'competence'])
  dataset = hire(dataset)
  
  output_file = open(DATA_DIR+'output/execution_'+str(execution)+'.csv','w')

  for iteration in tqdm(range(MAX_ITERATIONS), desc='Progress', unit='iterations'):
    global_efficiency = calculate_global_efficiency(dataset)
    output_file.write('{};{}\n'.format(iteration, global_efficiency))
    
    dataset = dismiss(dataset)
    dataset = promote(dataset, STRATEGY, HYPOTHESIS)
    dataset = age(dataset)
    dataset = hire(dataset)
  # end of iterations loop
  output_file.close()
# end of execution loop
