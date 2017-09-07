# File: ./examples1D/Lin_1D_A.py
# Focusing by a plano-convex lens


import numpy as np

Nx = 1500			# 600			# Grid points
Ny = 450    # 250
dt = 0.0005		# 0.001# Evolution step
tmax = 800		# Propagation end
xmax = 1000 					# x-window size
ymax = 300			# y-window size
images = 800				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 2        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0            # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	zR = 10000            # Rayleigh range
	zini = 0           # initial position, with respect to focus
	qini = 2*1.j*zini+zR  # Complex parameter of the beam
	f = np.sqrt(2*zR/np.pi)/qini*np.exp(-(x**2+y**2)/qini)

	return f;

def V(x,y,t,psi):		# Thick lens

	tini=1
	tfin=1.1
	k=.5
	m=1
	mask=2*(1+np.cos(k*x-m*np.arctan2(y,x)))
	if (t>=tini) and (t<tfin):
		V=-20*1.j*mask
	else:
		V=0

	return V;