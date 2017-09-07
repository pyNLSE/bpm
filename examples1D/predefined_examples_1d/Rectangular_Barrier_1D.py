# File: ./examples1D/Lin_1D_C.py
# Scattering of a wave packet by a barrier

import numpy as np

Nx = 1600						# Grid points
Ny = Nx
dt = 0.0001					# Evolution step
tmax = 6		# Propagation end
xmax = 50 					# x-window size
ymax = xmax					# y-window size
images = 100				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3         # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 1.05             # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	vx=10
	f=0.j+np.exp(-((x+15)/4)**2)    # A Gaussian wave packet moving rightwards
	f*=np.exp(1.j*vx*x)

	return f;

def V(x,y,t,psi):		# A barrier modeled by V=0 for |x|>5 and V=40 for |x|<5

	V = np.piecewise(x, [abs(x-5)<2.5, abs(x-5)>=2.5],[40,0])
	return V;