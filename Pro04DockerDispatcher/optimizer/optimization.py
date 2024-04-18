
from bayesian_optimizor import BayesianOptimization
from bayesian_optimizor import UtilityFunction
from experience_buffer import ExpBuffer


my_buffer = ExpBuffer()
my_optimizer = BayesianOptimization(
    f=None,
    pbounds={'x': (-2, 6), 'y': (-3, 8)},
    verbose=2,
    random_state=1,
    exp_buffer=my_buffer,
    allow_duplicate_points=True
)
my_utility = UtilityFunction(kind="ucb", kappa=2.5, xi=0.0)





