MAX_EXECUTIONS = 5
MAX_ITERATIONS = 100
MIN_COMPETENCE = 4.0
MAX_COMPETENCE = 10.0
MIN_AGE = 18
MAX_AGE = 65

NUM_LEVELS = 6

MAX_NUMBER_AGENTS = [1, 5, 11, 21, 41, 81]

LEVEL_RESPONSIBILITY = [1.0, 0.9, 0.8, 0.6, 0.4, 0.2]

# valid hypotheses: 'peter', 'common'
HYPOTHESIS = 'common'

# valid strategies: 'best', 'worst', 'random'
STRATEGY = 'random'

DATA_DIR = './data/'+HYPOTHESIS+'/'+STRATEGY+'/'
