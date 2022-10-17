# MOO algorithms
# from pymoo.algorithms.moo.age import AGEMOEA
# from pymoo.algorithms.moo.age2 import AGEMOEA2
# Commented because of numba dependency
from pymoo.algorithms.moo.ctaea import CTAEA
from pymoo.algorithms.moo.dnsga2 import DNSGA2
from pymoo.algorithms.moo.gde3 import GDE3, GDE32NN, GDE3MNN, GDE3PCD
from pymoo.algorithms.moo.moead import MOEAD
from pymoo.algorithms.moo.nsde import NSDE
from pymoo.algorithms.moo.nsder import NSDER
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.algorithms.moo.rnsga2 import RNSGA2
from pymoo.algorithms.moo.rnsga3 import RNSGA3
from pymoo.algorithms.moo.rvea import RVEA
from pymoo.algorithms.moo.sms import SMSEMOA
from pymoo.algorithms.moo.spea2 import SPEA2
from pymoo.algorithms.moo.unsga3 import UNSGA3

# SOO nonconvex algorithms
from pymoo.algorithms.soo.nonconvex.brkga import BRKGA
from pymoo.algorithms.soo.nonconvex.cmaes import CMAES
from pymoo.algorithms.soo.nonconvex.de import DE
from pymoo.algorithms.soo.nonconvex.de_ep import EPDE
from pymoo.algorithms.soo.nonconvex.direct import DIRECT
from pymoo.algorithms.soo.nonconvex.es import ES
from pymoo.algorithms.soo.nonconvex.g3pcx import G3PCX
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.algorithms.soo.nonconvex.ga_niching import NicheGA
from pymoo.algorithms.soo.nonconvex.isres import ISRES
from pymoo.algorithms.soo.nonconvex.nelder import NelderMead
# from pymoo.algorithms.soo.nonconvex.optuna import Optuna
# Commented because of optuna dependency
from pymoo.algorithms.soo.nonconvex.pattern import PatternSearch
from pymoo.algorithms.soo.nonconvex.pso import PSO
from pymoo.algorithms.soo.nonconvex.pso_ep import EPPSO
from pymoo.algorithms.soo.nonconvex.random_search import RandomSearch
from pymoo.algorithms.soo.nonconvex.sres import SRES

# SOO convex algorithms
