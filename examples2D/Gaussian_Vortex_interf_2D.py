# File: ./examples2D/Gaussian_Vortex_interf_2D.py
# Run as    python3 bpm.py Gaussian_Vortex_interf_2D 2D
# A Gaussian beam and a vortex cross each other generating the typical fork-like
# pattern


import numpy as np

Nx = 600						# Grid points
Ny = 300 
dt = 0.001		      	# Evolution step
tmax = 7		        # End of propagation
xmax = 30 					# x-window size
ymax = 20		      	# y-window size
images = 140				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 3        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0.07            # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction

	# gaussian beam moving rightwarks

	x1=-10
	y1=0
	r1=np.sqrt((x-x1)**2+(y-y1)**2)
	zR1=7
	zini1=-5
	qini1 = -zini1+1.j*zR1  # Complex parameter of the beam
	vx1=2.5
	vy1=0
	vel_phase1=np.exp(1.j*(vx1*x+vy1*y))
	f1 = np.sqrt(zR1/np.pi)/qini1*np.exp(-1.j*r1**2/(2*qini1))*vel_phase1

	# vortex moving leftwards

	x2=8
	y2=0
	zR2 = 5            # Rayleigh range
	zini2 = -5           # initial position, with respect to focus
	qini2 = -zini2+1.j*zR2    # Complex parameter of the beam
	r2=np.sqrt((x-x2)**2+(y-y2)**2)
	phase=np.exp(1.j*np.arctan2(y-y2,x-x2))
	vx2=-2.5
	vy2=0
	vel_phase2=np.exp(1.j*(vx2*x+vy2*y))
	f2 = zR2/np.sqrt(np.pi)/(qini2**2)*r2*np.exp(-1.j*r2**2/(2*qini2))*phase*vel_phase2

	return f1+f2;

def V(x,y,t,psi):		# Free propagation

	V=0

	return V;