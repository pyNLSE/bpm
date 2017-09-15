# File: ./examples2D/Filamentation.py
# Run as    python3 bpm.py Filamentation 2D
# Filamentation: an initially constant energy distribution results in the
# formation of filaments. The nonlinearities drive the evolution.


import numpy as np

Nx = 400			# Grid points
Ny = Nx    
dt = 0.001		   # Evolution step
tmax = 20		    # End of propagation 
xmax = 50 					# x-window size
ymax = xmax			# y-window size
images = 100				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 3       # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 5           # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				

# Initial wavefunction: a flat distribution, perturbed by a small quantity of random noise
	
	f = np.ones((len(x[:,1]),len(y[1,:])))+0.j
	f = f + 0.001*np.random.randn(len(x[:,1]),len(y[1,:]))+1.j*0.001*np.random.randn(len(x[:,1]),len(y[1,:]))

	return f;

def V(x,y,t,psi):		

# An attractive cubic nonlinearity that induces modulation instability. 
# A repulsive quintic term is included in order to avoid collapse (singularity formation).

	V=  -abs(psi)**2 + 0.1* abs(psi)**4
	

	return V;