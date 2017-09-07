# File: ./examples/example_01.py
# Initial condition: a 2D Gaussian with tilting angle and curvature
# Material: A Kerr focusing nonlinear optical material

import numpy as np

Nx = 1000						# Grid points
Ny = Nx
dt = 0.0005					# Evolution step
tmax = 15		# Propagation end
xmax = 30					# x-window size
ymax = xmax					# y-window size
images = 300				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 2       # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0               # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	x0=12
	f=0.j+np.zeros(len(x))
	for l in range(len(x)-1):
		if abs(x[l])<x0:
			f[l]=0.j+np.sqrt(x0**2-x[l]**2)
	
	return f;

def V(x,y,t,psi):		# Nonlinear material 

	if t<5:
		V = x**2 + (abs(psi))**2 
	else:
		V = x**2 +0.6* (abs(psi))**2 

	return V;