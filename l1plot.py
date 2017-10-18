import pylab
import scipy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# data
dx = [0.05, 0.03, 0.01, 0.001, 0.0001]
ftbs = [0.812, 0.648, 0.335, 0.0463, 0.00484]
lw = [0.592, 0.360, 0.0388, 0.00480, 0.000505]

def f(x, A, n):
    return A*x**n

ftbs_fit = [f(i, 10.6, 0.8) for i in dx]

pylab.plot(dx, ftbs, label = r'$L_1$')
pylab.plot(dx, ftbs_fit, label = 'fitted curve')
pylab.xscale('log')
pylab.xlabel('Log $\Delta x$')
pylab.yscale('log')
pylab.ylabel(r'Log $\rm{L}_1$')
pylab.legend()
pylab.savefig('pics/l1norm_ftbs')
pylab.show()

lw_fit = [f(i, 19.034, 1.2) for i in dx]

pylab.plot(dx, lw, label = r'$L_1$')
pylab.plot(dx, lw_fit, label = 'fitted curve')
pylab.xscale('log')
pylab.xlabel('Log $\Delta x$')
pylab.yscale('log')
pylab.ylabel(r'Log $\rm{L}_1$')
pylab.legend()
pylab.savefig('pics/l1norm_lw')
pylab.show()
