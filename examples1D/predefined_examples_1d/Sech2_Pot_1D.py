# File: ./examples1D/Lin_1D_D.py
# Initial condition: a 2D Gaussian with tilting angle and curvature
# Potential: A particular reflectionless potential

import numpy as np

Nx = 2000						# Grid points
Ny = Nx
dt = 0.001					# Evolution step
tmax = 200		# Propagation end
xmax = 100 					# x-window size
ymax = xmax					# y-window size
images = 100				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3         # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0               # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	vx=.4               # velocity
	cx=-.005             # initial curvature of the beam
	f=0.j+np.exp(-((x+30)/15)**2)      # A Gaussian
	f*=np.exp(1.j*(vx*x+cx*(x+30)**2))    # Include velocity and curvature
	
	return f;

def V(x,y,t,psi):		# Free propagation

	s=10     # The potential is reflectionless if s is a positive integer
	V=-1/2*s*(s+1)/(np.cosh(x))**2     # The reflectionless potential
	return V;