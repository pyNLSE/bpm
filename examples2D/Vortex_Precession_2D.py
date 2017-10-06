# File: ./examples2D/Vortex_Precession_2D.py
# Run as    python3 bpm.py Vortex_Precession_2D 2D
# Vortex precession within a harmonic potential



import numpy as np

Nx = 300						# Grid points
Ny = Nx
dt = 0.001					# Evolution step
tmax = 80		            # End of propagation 
xmax = 8 					# x-window size
ymax = xmax					# y-window size
images = 800				# number of .png images  
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 3     # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 2             # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				

      # Initial wavefunction: a vortex configuration

	z=x+1.j*y
	absz2=x**2+y**2
	f = (1-1.2*z)*np.exp(z)*np.exp(-absz2/2)  

	return f;

def V(x,y,t,psi):		# A harmonic trap and a repulsive cubic potential

	V = (x**2+y**2)/2 + abs(psi)**2
	return V;
