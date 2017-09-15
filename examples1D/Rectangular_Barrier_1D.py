# File: ./examples1D/Rectangular_Barrier_1D.py
# Run as    python3 bpm.py Rectangular_Barrier_1D 1D
# A Gaussian wave packet impinges on a rectangular barrier. Part of the wave
# is reflected, part of the wave is transmitted.



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

# A Gaussian wave packet moving rightwards

	vx=10     # value of the initial velocity
	f=0.j+np.exp(-((x+15)/4)**2)  # Gaussian profile    
	f*=np.exp(1.j*vx*x)   # Multiply by an x-dependent phase to introduce velocity

	return f;

def V(x,y,t,psi):		# A barrier modeled by V=0 for |x|>5 and V=40 for |x|<5

	V = np.piecewise(x, [abs(x-5)<2.5, abs(x-5)>=2.5],[40,0])
	return V;