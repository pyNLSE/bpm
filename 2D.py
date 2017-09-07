# Python functions for bpm2d.py

import numpy as np
import pyfftw
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams["text.usetex"] = False
import os
from matplotlib import cm


# Builds the fft

def fft(Nx,Ny):
	a = pyfftw.n_byte_align_empty((Nx, Ny), 16, dtype='complex64')
	a[:] = np.random.randn(*a.shape) + 1j*np.random.randn(*a.shape)
	fft = pyfftw.builders.fft2(a, overwrite_input=True, planner_effort='FFTW_EXHAUSTIVE')
	pyfftw.forget_wisdom()
	return fft;

# Builds the ifft

def ifft(Nx,Ny):
	a = pyfftw.n_byte_align_empty((Nx, Ny), 16, dtype='complex64')
	a[:] = np.random.randn(*a.shape) + 1j*np.random.randn(*a.shape)
	ifft = pyfftw.builders.ifft2(a, overwrite_input=True, planner_effort='FFTW_EXHAUSTIVE')
	pyfftw.forget_wisdom()
	return ifft;

# Builds the (x,y) grid

def grid(Nx,Ny,xmax,ymax):
	x = np.linspace(-xmax, xmax-2*xmax/Nx, Nx)     # x variable
	y = np.linspace(-ymax, ymax-2*ymax/Ny, Ny)     # y variable
	y,x=np.meshgrid(y, x)
	return x,y;

# Builds the Laplacian in Fourier space

def L(Nx,Ny,xmax,ymax):
	kx = np.linspace(-Nx/4/xmax, Nx/4/xmax-1/2/xmax, Nx)     # x variable
	ky = np.linspace(-Ny/4/ymax, Ny/4/ymax-1/2/ymax, Ny)     # y variable
	ky, kx = np.meshgrid(ky, kx)
	return (2*np.pi*1.j*kx)**2 + (2*np.pi*1.j*ky)**2 ;

# Introduces an absorbing shell at the border of the computational window

def absorb(x,y,xmax,ymax,dt,absorb_coeff):
	wx = xmax/40
	wy = ymax/40
	return np.exp(-absorb_coeff*(4-np.tanh((x+xmax)/wx)+np.tanh((x-xmax)/wx)-np.tanh((y+ymax)/wy)+np.tanh((y-ymax)/wy))*dt);

# Saves the 1D cut at y=0 at different values of t

def savepsi(Ny,psi):

	return abs(psi[:,Ny//2+1])**2

# Defines graphic output: a contour plot two-dimensional figure and the y=0 1d cut. 
# For both figures, |psi|^2 is depicted

def output(x,y,psi,n,t,folder,output_choice,fixmaximum):

    # Number of figure

	if (output_choice==2) or (output_choice==3):

		num =str(int(n))
		if n < 100: 
			num ='0'+str(int(n))
		if n < 10:
			num ='00'+str(int(n))

    ## Two-dimensional countour map

	fig = plt.figure("Contour map")				# figure
	plt.clf()                       # clears the figure
	plt.rc('text', usetex=True)		# Use LaTeX 
	plt.rc('font', family='serif')	# LaTeX font
	plt.axes().set_aspect('equal')  # Axes aspect ratio
	
	plt.xlabel('$x$')                 # choose axes labels
	plt.ylabel('$y$')

    # Makes the contour plot:

	toplot=abs(psi)**2
	if fixmaximum>0:
		toplot[toplot>fixmaximum]=fixmaximum    	
    

	surf = plt.contourf(x, y, toplot, 100, cmap=cm.jet, linewidth=0, antialiased=False)


	if fixmaximum>0:            # chooses the maximum for the color scale
		plt.clim(0,fixmaximum)
  
	cbar=plt.colorbar()          # colorbar
	cbar.set_label('$|\psi|^2$',fontsize=14)

	plt.title('$t=$ %f'%(t))    # Title of the plot 

	# Saves figure
	
	if (output_choice==2) or (output_choice==3):

		figname = folder+'/fig'+num+'.png'
		plt.savefig(figname)

	# Displays on screen

	if (output_choice==1) or (output_choice==3):

		plt.show(block=False)
		plt.pause(0.05)



	## One dimensional cut y=0

	fig = plt.figure("1D-cut for y=0")		# figure
	plt.clf()                       # clears the figure
	plt.rc('text', usetex=True)		# Use LaTeX 
	plt.rc('font', family='serif')	# LaTeX font

	Ny=len(y[1,:])
	plot = plt.plot(x[:,1], toplot[:,Ny//2+1])  # makes the plot

	plt.xlabel('$x$')                 # choose axes labels, title of the plot and axes range
	plt.ylabel('$|\psi|^2$')
 
	plt.title('$t=$ %f'%(t))     # title of the plot

	if fixmaximum>0:              # choose maximum |psi|^2 to be depicted in the vertical axis
		plt.axis([min(x[:,1]),max(x[:,1]),0,fixmaximum])

   # Saves figure 
	
	if (output_choice==2) or (output_choice==3):

		figname = folder+'/cut'+num+'.png'
		plt.savefig(figname)

	# Displays on screen

	if (output_choice==1) or (output_choice==3):

		plt.show(block=False)
		plt.pause(0.05)


	return;

# Some operations after the computation is finished: save the final value of psi, generate videos and builds
# the final plot: a contour map of the y=0 cut as a function of x and t

def final_output(folder,x,Deltat,psi,savepsi,output_choice,images,fixmaximum):


	np.save(folder,psi)		# saves final wavefunction

	if (output_choice==2) or (output_choice==3):
		movie(folder)	                        # creates video

	# Now we make a plot of the evolution depicting the 1D cut at y=0

	x=x[:,1]
	tvec=np.linspace(0,Deltat*images,images+1)
	tt,xx=np.meshgrid(tvec,x)
	figtx = plt.figure("Evolution of 1D cut at y=0")              # figure
	plt.clf()                       # clears the figure
	plt.rc('text', usetex=True)     # Use LaTeX 
	plt.rc('font', family='serif')  # LaTeX font
    
    # Generates the plot

	toplot=savepsi
	if fixmaximum>0:
		toplot[toplot>fixmaximum]=fixmaximum 

	surf = plt.contourf(xx, tt, toplot, 100, cmap=cm.jet, linewidth=0, antialiased=False)
	plt.xlabel('$x$')                 # choose axes labels, title of the plot and axes range
	plt.ylabel('$t$')

	if fixmaximum>0:            # chooses the maximum for the color scale
		plt.clim(0,fixmaximum)

	cbar=plt.colorbar()               # colorbar
	cbar.set_label('$|\psi|^2$',fontsize=14)
	figname = folder+'/sectx.png'
	plt.savefig(figname)    # Saves the figure
	plt.show()      # Displays figure on screen


# Generates two videos from the saved figures. This function is called by final_output

def movie(folder):
	folder.replace('.','')

	examplename=folder[13:]

	str1 ='opt="vbitrate=4320000:mbd=2:keyint=132:v4mv:vqmin=3:lumi_mask=0.07:dark_mask=0.2:mpeg_quant:scplx_mask=0.1:tcplx_mask=0.1:naq" '
	str2 ='mencoder "mf://'+folder+'/fig*.png" -mf fps=25 -o /dev/null -ovc lavc -lavcopts vcodec=mpeg4:vpass=1:$opt'
	str3 ='mencoder "mf://'+folder+'/fig*.png" -mf fps=25 -o ./'+folder+'/movie_'+examplename+'.avi -ovc lavc -lavcopts vcodec=mpeg4:vpass=2:$opt'
	str4 ='mencoder "mf://'+folder+'/cut*.png" -mf fps=25 -o /dev/null -ovc lavc -lavcopts vcodec=mpeg4:vpass=1:$opt'
	str5 ='mencoder "mf://'+folder+'/cut*.png" -mf fps=25 -o ./'+folder+'/moviecut_'+examplename+'.avi -ovc lavc -lavcopts vcodec=mpeg4:vpass=2:$opt'



	os.system(str1)
	os.system(str2)
	os.system(str3)
	os.system(str4)
	os.system(str5)
	os.system('rm divx2pass.log')
	os.system('rm -r __pycache__/')
	os.system('rm -r examples2D/__pycache__/')