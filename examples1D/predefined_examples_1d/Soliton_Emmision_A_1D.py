# File: ./examples/example_01.py
# Initial condition: a 2D Gaussian with tilting angle and curvature
# Material: A Kerr focusing nonlinear optical material

import numpy as np

Nx = 1200						# Grid points
Ny = Nx
dt = 0.0001			# Evolution step
tmax = 15		# Propagation end
xmax = 20					# x-window size
ymax = xmax					# y-window size
images = 300				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 3      # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 1.6             # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	
	f=0.j+np.exp(-((x+8)**2)/np.sqrt(2)/4)
	
	return f;

def V(x,y,t,psi):		# Nonlinear material 
	
	V= -np.exp(-((x+8)/4)**2) - 5*(np.tanh((x+6)/.5)+1)*abs(psi)**2
	return V;