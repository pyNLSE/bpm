# File: ./examples1D/Lin_1D_A.py
# Interference of two Gaussian wave packets


import numpy as np

Nx = 300						# Grid points
Ny = Nx
dt = 0.001					# Evolution step
tmax = 80		# Propagation end
xmax = 8 					# x-window size
ymax = xmax					# y-window size
images = 800				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 2       # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 2             # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	z=x+1.j*y
	absz2=x**2+y**2
	f = (1-1.2*z)*np.exp(z)*np.exp(-absz2/2)  # Two Gaussian that will interfere

	return f;

def V(x,y,t,psi):		# Free propagation

	V = (x**2+y**2)/2 + abs(psi)**2
	return V;