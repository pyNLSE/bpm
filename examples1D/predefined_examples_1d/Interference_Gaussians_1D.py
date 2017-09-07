# File: ./examples1D/Lin_1D_A.py
# Interference of two Gaussian wave packets


import numpy as np

Nx = 1000						# Grid points
Ny = Nx
dt = 0.001					# Evolution step
tmax = 4		# Propagation end
xmax = 25 					# x-window size
ymax = xmax					# y-window size
images = 100				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3         # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0               # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	f = (0.j+np.exp(-((x-3)/.5)**2))+(0.j+np.exp(-((x+3)/.5)**2))   # Two Gaussian that will interfere

	return f;

def V(x,y,t,psi):		# Free propagation

	V = 0
	return V;