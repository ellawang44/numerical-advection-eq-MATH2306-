import pylab
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# data
dx = [0.1, 0.05, 0.03, 0.01, 0.001]
ftbs = [0.993, 0.812, 0.648, 0.335, 0.0463]
lw = [0.988, 0.592, 0.360, 0.0388, 0.00480]

pylab.plot(dx, ftbs)
pylab.xscale('log')
pylab.xlabel('Log $\Delta x$')
pylab.yscale('log')
pylab.ylabel(r'Log $\rm{L}_1$')
pylab.savefig('pics/l1norm_ftbs')
pylab.show()

pylab.plot(dx, lw)
pylab.xscale('log')
pylab.xlabel('Log $\Delta x$')
pylab.yscale('log')
pylab.ylabel(r'Log $\rm{L}_1$')
pylab.savefig('pics/l1norm_lw')
pylab.show()
