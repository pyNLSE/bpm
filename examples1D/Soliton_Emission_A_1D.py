# File: ./examples1D/Soliton_Emission_A_1D.py
# Run as    python3 bpm.py Soliton_Emission_A_1D 1D
# Initially, there is a Gaussian wavefunction within a shallow trap.
# Due to a space-dependent attractive nonlineary, the energy moves rightwards
# and it turns out that a train of solitons is emitted.



import numpy as np

Nx = 1200						# Grid points
Ny = Nx
dt = 0.0001		        	# Evolution step
tmax = 15		            # End of propagation
xmax = 20					# x-window size
ymax = xmax					# y-window size
images = 300				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 3      # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 1.6             # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction: a Gaussian

	
	f=0.j+np.exp(-((x+8)**2)/np.sqrt(2)/4)
	
	return f;

def V(x,y,t,psi):		

# The linear part of the potential is a shallow trap modeled by an inverted
# Gaussian. The nonlinear part is an attractive cubic term whose coefficient
# depends on x in a step-like form
	
	V= -np.exp(-((x+8)/4)**2) - 5*(np.tanh((x+6)/.5)+1)*abs(psi)**2
	return V;