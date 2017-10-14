import numpy

def step_profile(x):
    """The step profile for where the sudden change of value is at x = 0.5"""

    if x < 0.5:
        return 1
    else:
        return 0

def gaussian(x):
    """The Gaussian function"""

    return numpy.e**(-((x - 0.5)**2)/0.01)
