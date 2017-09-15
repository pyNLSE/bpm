# File: ./examples2D/Vortex_2D.py
# Run as    python3 bpm.py Vortex_2D 2D
# A vortex beam propagating in free space


import numpy as np

Nx = 300						# Grid points
Ny = Nx
dt = 0.001			         # Evolution step
tmax = 10		            # End of propagation
xmax = 20 					# x-window size
ymax = xmax			        # y-window size
images = 100				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 2/(4*np.pi*np.exp(1))             # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction: a vortex

	
	zR = 2            # Rayleigh range
	zini = -5           # initial position, with respect to focus
	qini = -zini+1.j*zR   # Complex parameter of the beam
	r=np.sqrt(x**2+y**2)
	phase=np.exp(1.j*np.arctan2(y,x))
	f = zR/np.sqrt(np.pi)/(qini**2)*r*np.exp(-1.j*r**2/(2*qini))*phase

	return f;

def V(x,y,t,psi):		# Free propagation

	V=0

	return V;