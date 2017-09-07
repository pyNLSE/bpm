# File: ./examples/example_01.py
# Initial condition: a 2D Gaussian with tilting angle and curvature
# Material: A Kerr focusing nonlinear optical material

import numpy as np

Nx = 1200						# Grid points
Ny = Nx
dt = 0.0002				# Evolution step
tmax = 10		# Propagation end
xmax = 60					# x-window size
ymax = xmax					# y-window size
images = 400				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3      # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0             # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	
	f=0.j+np.exp(-((x)**2)/np.sqrt(2)/4)
	
	return f;

def V(x,y,t,psi):		# Nonlinear material 
	
	a0=0;  # initial (vanishing) nonlinear coefficient    
	a1=25;   # repulsive nonlinear coefficient for 3<t<8
	a2=-35;   # attractive nonlinear coefficient for t>8

	if t<1:
		V= -np.exp(-((x)/4)**2) + a0*abs(psi)**2
	elif t<3:
		V= -np.exp(-((x)/4)**2) + a1*abs(psi)**2
	else:
		V= -np.exp(-((x)/4)**2) + a2*abs(psi)**2

	return V;