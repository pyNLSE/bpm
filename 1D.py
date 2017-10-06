import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import cm
import shutil
import platform


def grid(Nx,Ny,xmax,ymax):
	x = np.linspace(-xmax, xmax-2*xmax/Nx, Nx)     # x variable
	y = 0                 # not used, but a value must be given
	return x,y;

# Builds the Laplacian in Fourier space

def L(Nx,Ny,xmax,ymax):
	kx = np.linspace(-Nx/4/xmax, Nx/4/xmax-1/2/xmax, Nx)     # x variable
	return (2*np.pi*1.j*kx)**2 

# Introduces an absorbing shell at the border of the computational window

def absorb(x,y,xmax,ymax,dt,absorb_coeff):
	wx = xmax/20
	return np.exp(-absorb_coeff*(2-np.tanh((x+xmax)/wx)+np.tanh((x-xmax)/wx))*dt);

# Saves the data of abs(psi)**2 at different values of t

def savepsi(Ny,psi):
	
	return abs(psi)**2

# Defines graphic output: |psi|^2 is depicted

def output(x,y,psi,n,t,folder,output_choice,fixmaximum):
	# Number of figure
	if (output_choice==2) or (output_choice==3):
		num =str(int(n))
		if n < 100: 
			num ='0'+str(int(n))
		if n < 10:
			num ='00'+str(int(n))

	## The plot
	fig = plt.figure("1D plot")	# figure
	plt.clf()                       # clears the figure
	if platform.system() == 'Windows':
		fig.set_size_inches(8,6)
	plt.plot(x, abs(psi)**2)  # makes the plot
	plt.xlabel('$x$')           # format LaTeX if installed (choose axes labels, 
	plt.ylabel('$|\psi|^2$')    # title of the plot and axes range
	plt.title('$t=$ %f'%(t))    # title of the plot

	if fixmaximum>0:              # choose maximum |psi|^2 to be depicted in the vertical axis
		plt.axis([min(x),max(x),0,fixmaximum])
		
	# Saves figure 
	if (output_choice==2) or (output_choice==3):
		figname = folder+'/fig'+num+'.png'
		plt.savefig(figname)

	# Displays on screen
	if (output_choice==1) or (output_choice==3):
		plt.show(block=False)
		fig.canvas.flush_events()

	return;

# Some operations after the computation is finished: save the final value of psi, generate videos and builds
# the final plot: a contour map of the y=0 cut as a function of x and t

def final_output(folder,x,Deltat,psi,savepsi,output_choice,images,fixmaximum):


	np.save(folder,psi)		# saves final wavefunction

	if (output_choice==2) or (output_choice==3):
		movie(folder)	                        # creates video

	# Now we make a plot of the evolution depicting the 1D cut at y=0
	tvec=np.linspace(0,Deltat*images,images+1)
	tt,xx=np.meshgrid(tvec,x)
	figtx = plt.figure("Evolution of |psi(x)|^2")              # figure
	plt.clf()                # clears the figure
	figtx.set_size_inches(8,6)



    # Generates the plot
	toplot=savepsi
	if fixmaximum>0:
		toplot[toplot>fixmaximum]=fixmaximum 

	plt.contourf(xx, tt, toplot, 100, cmap=cm.jet, linewidth=0, antialiased=False)
	cbar=plt.colorbar()               # colorbar
	plt.xlabel('$x$')                 # axes labels, title, plot and axes range
	plt.ylabel('$t$')
	cbar.set_label('$|\psi|^2$',fontsize=14)

	figname = folder+'/sectx.png'
	plt.savefig(figname)    # Saves the figure
	plt.show()      # Displays figure on screen


# Generates video from the saved figures. This function is called by final_output
def movie(folder):
	folder.replace('.','')
	examplename=folder[13:]
	

	video_options='vbitrate=4320000:mbd=2:keyint=132:v4mv:vqmin=3:lumi_mask=0.07:dark_mask=0.2:mpeg_quant:scplx_mask=0.1:tcplx_mask=0.1:naq'		
	
	if platform.system() == 'Windows':
		try:
			shutil.copyfile('mencoder.exe', folder+'/mencoder.exe')
			os.chdir(folder)
			command ='mencoder "mf://fig*.png" -mf w=800:h=600:fps=25:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o movie_'+examplename+'.avi'
			os.system(command)
			try:
				os.remove('mencoder.exe')
			except:
				print("Could not delete mencoder.exe in examlpe directory")
			    
			os.chdir('../../')
		except:
			print("Error making movie with mencoder in windows")
		    
	else:
		try:
			command1 ='mencoder "mf://'+folder+'/fig*.png" -mf fps=25 -o /dev/null -ovc lavc -lavcopts vcodec=mpeg4:vpass=1:'+video_options
			command2 ='mencoder "mf://'+folder+'/fig*.png" -mf fps=25 -o ./'+folder+'/movie_'+examplename+'.avi -ovc lavc -lavcopts vcodec=mpeg4:vpass=2:'+video_options
			os.system(command1)
			os.system(command2)
		except:
			print("Error making movie with mencoder in Linux")
			    
			    
			    
			    
	## delete temporary files:
	try:
		os.remove('divx2pass.log')
	except:
		pass
			    
	try:
		shutil.rmtree('__pycache__')
	except:
		pass
		
	try:
		shutil.rmtree('examples1D/__pycache__/')
	except:
		pass

