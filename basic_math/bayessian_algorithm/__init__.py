import numpy as np

from basic_math.bayessian_algorithm.formula import bayessian_formula

if __name__ == '__main__':
    prob_e_b = 0.6
    prob_b = 0.5
    prob_e = 0.35
    prob_b_e = bayessian_formula(prob_e_b, prob_b, prob_e)
    print(prob_b_e)