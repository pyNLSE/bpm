# File: ./examples1D/Lin_1D_A.py
# Focusing by a plano-convex lens


import numpy as np

Nx = 500						# Grid points
Ny = Nx
dt = 0.001			# Evolution step
tmax = 60		# Propagation end
xmax = 100 					# x-window size
ymax = xmax			# y-window size
images = 6			# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3       # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0.04            # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	rhole=10
	r=np.sqrt(x**2+y**2)
	f=0.j+(np.tanh((rhole-r)/.01)+1)/2

	return f;

def V(x,y,t,psi):		# Thick lens

	
	V=0

	return V;