
# from .bayesian_optimizor import BayesianOptimization,UtilityFunction
from .new_bayesian_optimizor import BayesianOptimization,UtilityFunction

from .experience_buffer import ExpBuffer


my_buffer = ExpBuffer()

Parameters={
    'pro01memory': (0,1000000),         # pro01的内存           [0-1000000]
    'pro01cpu': (0,10),                 # pro01的cpu           [0-10]
    'pro01reso': (0,6),                 # pro01的分辨率         [0,1,2,3,4,5]代表128,160,320,480,640,1280六个档位
    'pro01threshold': (1000,15000),     # pro01的关键帧阈值      [1000,15000]
    'pro01place': (0,2),                # pro01的位置           [0,1]代表边缘端与云端

    # face detection module
    'pro02memory': (0,1000000),          # pro02的内存        [0-1000000]
    'pro02cpu':(0,10),                   # pro02的cpu        [0-10]
    'pro02reso': (0, 6),                 # pro02的分辨率         [0,1,2,3,4,5]代表128,160,320,480,640,1280六个档位
    'pro02threshold': (0.1,1),           # pro02的nms阈值     [0.1,1]
    'pro02place': (1,2),                 # pro02的位置        [1]

    # pose estimation module
    'pro03memory': (0,1000000),          # pro03的内存         [0-1000000]
    'pro03cpu': (0,10),                  # pro03的cpu         [0-10]
    'pro03place': (1,2),                     # pro03的位置         [1]

    # docker dispatch module
    'pro04memory': (0,1000000),          # pro04的内存        [0-1000000]
    'pro04cpu': (0,10),                  # pro04的cpu        [0-10]
    'pro04place': (0,2),                 # pro04的位置        [0,1]

    'pro05bandwidth': (0,2000),          # 带宽限制            [0-2000]
}

my_optimizer = BayesianOptimization(
    f=None,
    pbounds=Parameters,
    verbose=2,
    random_state=1,
    exp_buffer=my_buffer,
    allow_duplicate_points=True
)

my_utility = UtilityFunction(kind="ucb", kappa=2.5, xi=0.0)





