import numpy as np
import random
import matplotlib.pyplot as plt

iteration_constant = 50000


def calculate_the_permissible_voltage(tension_of_material):
    tensions_admissible = []
    for security_factor in np.arange(1.0, 1.6, 0.1):
        admissible_tension = tension_of_material / security_factor
        tensions_admissible.append(admissible_tension)

    return tensions_admissible


def bending_moment(weight, force, length):
    return 4 * (force + weight) / length


def moment_of_inertia(high, base):
    return pow(high, 3) * base / 12


def acting_tension(thickness, inertia, moment):
    return - moment * thickness / (2 * inertia)


def performance_function(admissible, acting):
    performance_functions = []
    for admissible_value in admissible:
        performance = admissible_value - acting
        performance_functions.append(performance)

    return performance_functions


def failure_probability(performance_values):
    values_failure_probability = []
    security_factor = 1.0
    for performance_value in performance_values:
        probability = function_gaussian(performance_value)
        f_p = 1 - abs(probability)/iteration_constant
        values_failure_probability.append((round(security_factor, 1), round(f_p, 2)))
        security_factor += 0.1

    return values_failure_probability


def function_gaussian(performance):
    values = []
    sigma = 50
    beta = 0.0
    for i in range(iteration_constant):
        value = random.gauss(performance, sigma)
        values.append(value)
        if value < 0.0:
            beta += value
    plt.hist(values, bins=200)
    return beta
