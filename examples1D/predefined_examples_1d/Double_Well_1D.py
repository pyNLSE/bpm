# File: ./examples1D/Lin_1D_E.py
# Beating in a double well potential


import numpy as np

Nx = 600						# Grid points
Ny = Nx
dt = 0.001					# Evolution step
tmax = 30		# Propagation end
xmax = 5					# x-window size
ymax = xmax					# y-window size
images = 300				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3         # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 1.25              # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	f = 0.j+np.exp(-((x-1)**2)/2)   # A Gaussian centered at one of the wells

	return f;

def V(x,y,t,psi):		# A double well potential

	V = (x**2-1)**2/8
	return V;