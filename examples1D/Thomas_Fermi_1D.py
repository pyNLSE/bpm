# File: ./examples1D/Thomas_Fermi_1D.py
# Run as    python3 bpm.py Thomas_Fermi_1D 1D
# Initially, a nonlinear wave packet is confined within a harmonic well, and
# it is well approximated by a Thomas-Fermi profile (in which the Laplacian
# is neglected). At t=5, the strength of the nonlinearity is changed and an
# oscillation starts




import numpy as np

Nx = 1000						# Grid points
Ny = Nx
dt = 0.0005					# Evolution step
tmax = 15	                # End of propagation
xmax = 30					# x-window size
ymax = xmax					# y-window size
images = 300				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 2       # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 250               # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

# The initial |psi|^2 is an inverted parabola that solves the equation in the
# absence of the derivative term.

	x0=12
	f=0.j+np.zeros(len(x))
	for l in range(len(x)-1):
		if abs(x[l])<x0:
			f[l]=0.j+np.sqrt(x0**2-x[l]**2)
	
	return f;

def V(x,y,t,psi):		

# A harmonic trap and a cubic attractive (focusing) nonlinearity, whose strength
# changes at t=5

	if t<5:
		V = x**2 + (abs(psi))**2 
	else:
		V = x**2 +0.6* (abs(psi))**2 

	return V;