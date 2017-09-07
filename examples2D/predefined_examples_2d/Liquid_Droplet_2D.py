# File: ./examples1D/Lin_1D_A.py
# Interference of two Gaussian wave packets


import numpy as np

Nx = 400						# Grid points
Ny = 240
dt = 0.001					# Evolution step
tmax = 140		# Propagation end
xmax = 160					# x-window size
ymax = 100					# y-window size
images = 300				# number of .png images
absorb_coeff = 10		# 0 = periodic boundary
output_choice = 2      # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0.8           # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.

def psi_0(x,y):				# Initial wavefunction


	rsoliton=60
	Nx=len(x[:,1])
	Ny=len(y[1,:])
	psi0=np.zeros((Nx,Ny))+0.j
	x0=0
	y0=10
	vx=0
	vy=-1

	for ix in range(Nx):
		for iy in range(Ny):
			rhere=np.sqrt((x[ix,1]-x0)**2+(y[1,iy]-y0)**2)
			psi0[ix,iy]=np.sqrt(3/4/(np.exp(rhere-rsoliton)+1))

	psi0*=np.exp(1.j*(vx*x+vy*y))
				
       


	return psi0;

def V(x,y,t,psi):		# Free propagation

	V = - abs(psi)**2 +  abs(psi)**4 + 20*(np.tanh(y+80)-1)
	return V;