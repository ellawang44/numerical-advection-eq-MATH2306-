import pylab
import numpy
from optparse import OptionParser
import schemes
import init_cond
import l1norm

parser = OptionParser()

parser.add_option('-s', '--scheme', type = 'string', dest = 'scheme', help = 'Determines which scheme to run. Default is ftbs.')
parser.add_option('-i', '--init', type = 'string', dest = 'init', help = 'Determines which initial condition to use. Default is step function.')
parser.add_option('--cr', type = 'float', dest = 'cr', help = 'Changes the Cr value used, 1 by default.')
parser.add_option('--dx', type = 'float', dest = 'dx', help = 'Changes the dx used, 0.01 by default.')

(options, args) = parser.parse_args()

u = 1 #m/s
if options.cr:
    C_r = options.cr
else:
    C_r = 0.5
if options.dx:
    dx = options.dx
else:
    dx = 0.01
dt = C_r * dx / u
# add a bit onto t_max to make sure while loop terminates at the correct value
t_max = 1 + dt/10

# set up the initial grid
x = numpy.arange(0, 2, dx)
# get initial function
if options.init == 'gaussian':
    cond = 'gauss'
    h_0 = [init_cond.gaussian(i) for i in x]
    h = [init_cond.gaussian(i) for i in x]
    exact_soln = [init_cond.gaussian(i - t_max) for i in x]
else:
    cond = 'step'
    h_0 = [init_cond.step_profile(i) for i in x]
    h = [init_cond.step_profile(i) for i in x]
    exact_soln = [init_cond.step_profile(i - t_max) for i in x]
    
# initial time
t = 0

if options.scheme == 'ftcs':
    scheme = 'ftcs'
    while t < t_max:
        # incriment time step
        t += dt
        # propagate solution forwards
        h = [schemes.ftcs(j, j1, j2, C_r) for (j, j1, j2) in zip(h, h[1:], h[2:])]
        # add values back in for boundary
        if options.init == 'gaussian':
            h.insert(0, 0)
            h.append(0)
        else:
            h.insert(0, 1)
            h.append(0)
elif options.scheme == 'ftfs':
    scheme = 'ftfs'
    while t < t_max:
        # incriment time step
        t += dt
        # propagate solution forwards
        h = [schemes.ftfs(j, j1, C_r) for (j, j1) in zip(h, h[1:])]
        # add value back in for boundary
        h.append(0)
elif options.scheme == 'lax_wendroff':
    scheme = 'lax_wendroff'
    while t < t_max:
        # incriment time step
        t += dt
        # propagate solution forwards
        h = [schemes.lax_wendroff(j, j1, j2, C_r) for (j, j1, j2) in zip(h, h[1:], h[2:])]
        # add value back in for boundary
        if options.init == 'gaussian':
            h.insert(0, 0)
            h.append(0)
        else:
            h.insert(0, 1)
            h.append(0)
elif options.scheme == 'beam_warming':
    scheme = 'beam_warming'
    while t < t_max:
        # incriment time step
        t += dt
        # propagate solution forwards
        h = [schemes.beam_warming(j, j1, j2, C_r) for (j, j1, j2) in zip(h, h[1:], h[2:])]
        # add value back in for boundary
        if options.init == 'gaussian':
            h.insert(0, 0)
            h.insert(0, 0)
        else:
            h.insert(0, 1)
            h.insert(0, 1)
else:
    scheme = 'ftbs'
    while t < t_max:
        # incriment time step
        t += dt
        # propagate solution forwards
        h = [schemes.ftbs(j, j1, C_r) for (j, j1) in zip(h, h[1:])]
        # add value back in for boundary
        if options.init == 'gaussian':
            h.insert(0, 0)
        else:
            h.insert(0, 1)

print('L1 norm: ' + str(l1norm.L1(h, exact_soln)))
pylab.plot(x, h_0, 'r', label = 'initial condition')
pylab.plot(x, h, 'b', label = 'numerical solution')
pylab.plot(x, exact_soln, 'g', label = 'analytical solution')
pylab.xlabel('x')
pylab.ylabel('h')
pylab.legend()
# pylab.savefig('pics/' + scheme + '_' + cond)
# pylab.ylim(-0.1, 1.1)
pylab.show()
