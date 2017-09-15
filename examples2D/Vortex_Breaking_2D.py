# File: ./examples2D/Vortex_Breaking_2D.py
# Run as    python3 bpm.py Vortex_Breaking_2D 2D
# Azimuthal instability of a vortex because of an attractive nonlinearity


import numpy as np

Nx = 300						# Grid points
Ny = Nx
dt = 0.001		    	# Evolution step
tmax = 500		        # End of propagation 
xmax = 120 					# x-window size
ymax = xmax		       	# y-window size
images = 200				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0.02         # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction: a vortex

	
	zR = 200            # Rayleigh range
	zini = 0           # initial position, with respect to focus
	qini = -zini+1.j*zR  # Complex parameter of the beam
	r=np.sqrt(x**2+y**2)
	phase=np.exp(1.j*2*np.arctan2(y,x))
	f = 0.0009*r**2*np.exp(-1.j*r**2/(2*qini))*phase
	
	return f;

def V(x,y,t,psi):		# Focusing Kerr (cubic) nonlinearity

	V=-abs(psi)**2

	return V;