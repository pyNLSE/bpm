# Integrating a 1+1D or 1+2D NLSE with different initial conditions and for different potentials. 
# To run this code type the command: 
# python3 bpm.py example 1D    for a 1D example   (1D.py file needed)
# python3 bpm.py example 2D    for a 2D example   (2D.py file needed)
# where example.py contains the details for the particular example and should be placed in 
# the directory ./examples1D   or   ./examples2D

import numpy as np
import sys
import os
import importlib
import glob

# Preliminaries (handling directories and files)
sys.path.insert(0, './examples'+sys.argv[2])		  # adds to path the directory with examples
output_folder = './examples'+sys.argv[2]+'/'+sys.argv[1]  # directory for images and video output
if not os.path.exists(output_folder):                     # creates folder if it does not exist
    os.makedirs(output_folder)

try:              # Erase all image files (if exist) before starting computation and generating new output
    for filename in glob.glob(output_folder+'/*.png') :   
        os.remove( filename )
except: 
    pass

my = importlib.__import__(sys.argv[1])		     # imports the file with the details for the computation
build = importlib.__import__(sys.argv[2])	     # selects 1D or 2D


# Initialization of the computation

x, y = build.grid(my.Nx,my.Ny,my.xmax,my.ymax)		# builds spatial grid
psi = my.psi_0(x,y) 					# loads initial condition


L = build.L(my.Nx,my.Ny,my.xmax,my.ymax)		# Laplacian in Fourier space
linear_phase = np.fft.fftshift(np.exp(1.j*L*my.dt/2))            	# linear phase in Fourier space (including point swap)
border = build.absorb(x,y,my.xmax,my.ymax,my.dt,my.absorb_coeff)    # Absorbing shell at the border of the computational window

savepsi=np.zeros((my.Nx,my.images+1))     # Creates a vector to save the data of |psi|^2 for the final plot
steps_image=int(my.tmax/my.dt/my.images)  # Number of computational steps between consecutive graphic outputs


# Main computational loop
print("calculating", end="", flush=True)
for j in range(steps_image*my.images+1):		# propagation loop
	if j%steps_image == 0:  # Generates image output 
		build.output(x,y,psi,int(j/steps_image),j*my.dt,output_folder,my.output_choice,my.fixmaximum)
		savepsi[:,int(j/steps_image)]=build.savepsi(my.Ny,psi)
		print(".", end="", flush=True)

	V = my.V(x,y,j*my.dt,psi)			# potential operator
	psi *= np.exp(-1.j*my.dt*V)			# potential phase
	if sys.argv[2] == "1D":
		psi = np.fft.fft(psi)			# 1D Fourier transform
		psi *=linear_phase		        # linear phase from the Laplacian term
		psi = border*np.fft.ifft(psi)	# inverse Fourier transform and damping by the absorbing shell
	elif sys.argv[2] == "2D":
		psi = np.fft.fft2(psi)			# 2D Fourier transform
		psi *=linear_phase		        # linear phase from the Laplacian term
		psi = border*np.fft.ifft2(psi)	# inverse Fourier transform and damping by the absorbing shell
	else: 
		print("Not implemented")

# Final operations
# Generates some extra output after the computation is finished and save the final value of psi:

build.final_output(output_folder,x,steps_image*my.dt,psi,savepsi,my.output_choice,my.images,my.fixmaximum)
print()

