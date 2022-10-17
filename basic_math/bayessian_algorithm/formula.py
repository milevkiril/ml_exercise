import pandas as pd
import numpy as np


def bayessian_formula(prob_e_b, prob_b, prob_e):
    """
    This function calculates the probability for a certain belief considering an evidence.

    :param prob_e_b: Probability of the evidence when the belief is true.
    :param prob_b: Probability of the belief being true.
    :param prob_e: Probability of the evidence being true.
    :return:
    """
    return prob_e_b * prob_b / prob_e

