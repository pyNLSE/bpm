# File: ./examples1D/Soliton_Emission_B_1D.py
# Run as    python3 bpm.py Soliton_Emission_B_1D 1D
# Initially, a Gaussian wave packet is confined within a shallow trap. At a given
# time, a repulsive interaction is turned on and the wave starts expanding. Then,
# the sign of the nonlinear term is changed and the interaction becomes attractive.
# This results in the formation of a bunch of solitons that escape from the trap.



import numpy as np

Nx = 1200						# Grid points
Ny = Nx
dt = 0.0002				# Evolution step
tmax = 10		        # End of propagation
xmax = 60					# x-window size
ymax = xmax					# y-window size
images = 400				# number of .png images
absorb_coeff = 20		# 0 = periodic boundary
output_choice = 3      # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0.8            # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction: a Gaussian

	
	f=0.j+np.exp(-((x)**2)/np.sqrt(2)/4)
	
	return f;

def V(x,y,t,psi):		

	# The linear part of the potential is a shallow trap modeled by an inverted Gaussian
	# The nonlinear part is a cubic term whose sign and strength change abruptly in time.
	
	a0=0;  # initial (vanishing) nonlinear coefficient    
	a1=25;   # repulsive nonlinear coefficient for 3<t<8
	a2=-35;   # attractive nonlinear coefficient for t>8

	if t<1:
		V= -np.exp(-((x)/4)**2) + a0*abs(psi)**2
	elif t<3:
		V= -np.exp(-((x)/4)**2) + a1*abs(psi)**2
	else:
		V= -np.exp(-((x)/4)**2) + a2*abs(psi)**2

	return V;