# File: ./examples1D/Lin_1D_A.py
# Propagation of vortex


import numpy as np

Nx = 300						# Grid points
Ny = Nx
dt = 0.001			# Evolution step
tmax = 500		# Propagation end
xmax = 120 					# x-window size
ymax = xmax			# y-window size
images = 200				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 1        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0 #0.02         # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	
	zR = 400            # Rayleigh range
	zini = 0           # initial position, with respect to focus
	qini = 2*1.j*zini+zR  # Complex parameter of the beam
	r=np.sqrt(x**2+y**2)
	phase=np.exp(1.j*2*np.arctan2(y,x))
	f = 0.0009*r**3*np.exp(-r**2/qini)*phase
	
	return f;

def V(x,y,t,psi):		# Thick lens

	V=-abs(psi)**2

	return V;