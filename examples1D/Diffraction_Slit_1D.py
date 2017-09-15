# File: ./examples1D/Diffraction_Slit_1D.py
# Run as    python3 bpm.py Diffraction_Slit_1D 1D
# Diffraction by a slit
# The initial condition is a flat function within a finite domain, modeling
# the passage of a wide wave through a slit. The evolution generates the typical
# diffraction pattern

import numpy as np

Nx = 1000						# Grid points
Ny = Nx
dt = 0.0001					# Evolution step
tmax = .4		            # End of propagation
xmax = 30 					# x-window size
ymax = xmax					# y-window size
images = 100				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3         # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0               # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

# A step function, modelling the passage of a plane wave through a slit

	f = 0.j+np.piecewise(x, [abs(x)<.5, abs(x)>=.5],[1,0])  

	return f;

def V(x,y,t,psi):		# Free propagation

	V = 0
	return V;