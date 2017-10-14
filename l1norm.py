import numpy

def L1(num, analytical):

    '''
    Calculates the L1 norm of the numerical solution and analytical solution
    '''

    return sum(numpy.absolute(numpy.array(num) - numpy.array(analytical))) / sum(numpy.absolute(analytical))
