# File: ./examples1D/Solitons_in_phase_1D.py
# Run as    python3 bpm.py Solitons_in_phase_1D 1D
# Encounter of two solitons in phase, which traverse each other unaffected.
# During the collision, an interference pattern is generated.


import numpy as np

Nx = 500						# Grid points
Ny = Nx
dt = 0.001					# Evolution step
tmax = 5		            # End of propagation
xmax = 10 					# x-window size
ymax = xmax					# y-window size
images = 100				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 3        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 1.2               # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

# Two solitons heading each other in phase coincidence

	x01=-5
	x02=-x01
	v1=2
	v2=-v1
	fase1=0
	fase2=0
	f1 = (0.j+1/np.cosh(x-x01))*np.exp(v1*1.j*x+1.j*fase1)	# Soliton 1
	f2 = (0.j+1/np.cosh(x-x02))*np.exp(v2*1.j*x+1.j*fase2)	# Soliton 2
	f = f1+f2

	return f;

def V(x,y,t,psi):		# A cubic attractive (focusing) nonlinearity

	V = - (abs(psi))**2 
	return V;