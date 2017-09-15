# File: ./examples2D/Gaussian_Beam_2D.py
# Run as    python3 bpm.py Gaussian_Beam_2D 2D
# A Gaussian beam propagating in free space


import numpy as np

Nx = 300						# Grid points
Ny = Nx
dt = 0.001		      # Evolution step
tmax = 10		      # End of propagation
xmax = 20 					# x-window size
ymax = xmax		     	# y-window size
images = 100				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 2/(4*np.pi)             # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction: a Gaussian beam

	zR = 2              # Rayleigh range
	zini = -5           # initial position, with respect to focus
	qini = -zini+1.j*zR  # Complex parameter of the beam
	f = np.sqrt(zR/np.pi)/qini*np.exp(-1.j*(x**2+y**2)/(2*qini))

	return f;

def V(x,y,t,psi):		# Free propagation

	V=0

	return V;