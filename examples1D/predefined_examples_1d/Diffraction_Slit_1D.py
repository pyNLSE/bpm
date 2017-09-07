# File: ./examples/example_01.py
# Initial condition: a 2D Gaussian with tilting angle and curvature
# Material: A Kerr focusing nonlinear optical material

import numpy as np

Nx = 1000						# Grid points
Ny = Nx
dt = 0.0001					# Evolution step
tmax = .4		# Propagation end
xmax = 30 					# x-window size
ymax = xmax					# y-window size
images = 100				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3         # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0               # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	f = 0.j+np.piecewise(x, [abs(x)<.5, abs(x)>=.5],[1,0])  # A step function, modelling the passage of a plane wave through a slit

	return f;

def V(x,y,t,psi):		# Free propagation

	V = 0
	return V;