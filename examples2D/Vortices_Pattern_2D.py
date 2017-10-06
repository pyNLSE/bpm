# File: ./examples2D/Vortices_Pattern_2D.py
# Run as    python3 bpm.py Vortices_Pattern_2D 2D
# A Gaussian beam impinges on a mask that generates a diffaction pattern with
# vortices of different topological charges.


# NOTICE: This example uses a fine computational grid, it uses a lot of memory 
# and takes some time to run. It is possible to reduce Nx, Ny and take a larger dt
# in order to obtain approximate results with less computational resources.

import numpy as np

Nx = 1500		       # Grid points
Ny = 450    
dt = 0.0005	         	# Evolution step
tmax = 800		        # End of propagation 
xmax = 1000 					# x-window size
ymax = 300		     	# y-window size
images = 800				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 2        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0            # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction: a Gaussian

	zR = 5000            # Rayleigh range
	zini = 0           # initial position, with respect to focus
	qini = -zini+1.j*zR  # Complex parameter of the beam
	f = np.sqrt(zR/np.pi)/qini*np.exp(-1.j*(x**2+y**2)/(2*qini))

	return f;

def V(x,y,t,psi):		

	# Between tini and tfin, there is an imaginary potential that absorbs part of
	# the energy. It acts as a spatial filter. After tfin, there is free propagation

	tini=1
	tfin=1.1
	k=.5
	m=1
	mask=2*(1+np.cos(k*x-m*np.arctan2(y,x)))
	if (t>=tini) and (t<tfin):
		V=-20*1.j*mask
	else:
		V=0

	return V;
