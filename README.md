# numerical-advection-eq-MATH2306-
Solves the advection equation using different schemes (forward time forward space, forward time centered space, forward time backwards space, Lax Wendroff, Beam Warming) with the initial profile being either the step function or the Gaussian function

## Argument Flags
--scheme
Determines which scheme to run. Options are "ftbs", "ftfs", "ftcs", "lax_wendroff", and "beam_warming". If this flag is not called, forward time backwards space is run by default. E.g: --scheme "lax_wendroff".

--init
Determines which initial condition to use. Options are "step", and "gaussian". If this flag is not called, the step-profile is used by default. E.g: --init "gaussian".

--cr
Changes the Cr value used. Input is any float value. By default, Cr = 0.5. E.g: --cr 3.

--dx
Changes the dx value used. Input it any float value. By default, dx = 0.01. E.g: --dx 0.5.

## Save Figure
There is a line of code which can save the figure automatically into the pics folder, this line is commented out currently. This can be changed to make saving figures easier. 
