import numpy as np
import sys
import logging
import time
import matplotlib.image as mpimg


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


c2= 0.49 # meter**2/second
a=1  # meters 
dt=0.5# seconds

r=c2*dt/(a**2) #dimensionless and should be smaller than 1/2 for the algorithm to be stable

logging.basicConfig(filename='logfile', encoding='utf-8', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.debug('This message should go to the log file')
logging.info('This is the beginning of the log file.')
# logging.warning('And this, too')


#this is the FTCS (Forward Time, Centered Space) approximation to the heat equation in 2D
def update(u,rd):
    nx,ny=u.shape
    unew= np.zeros(u.shape)
    
    for ix in range(1,nx-1):
        for iy in range(1,ny-1):
            unew[ix,iy] = u[ix,iy] + rd*(u[ix+1,iy] + u[ix-1,iy] + u[ix,iy+1] + u[ix,iy-1] - 4*u[ix,iy])
   
    return unew
def init_fromfile(file):
    u = rgb2gray(mpimg.imread(file))
    u /= np.max(u)
    return u


def init_dat(N,M):
    #u = rgb2gray(mpimg.imread("/Users/vdrach/MATH2607/800px-Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg"))
    #u /= np.max(u)
    u= np.zeros([N,M])
    nx,ny=u.shape
    r=25
    for ix in range(1,nx-1):
        for iy in range(1,ny-1):
            #u[ix,iy]=np.exp(-((ix-nx/2)**2+(iy-ny/2)**2)/(2.*100**2))
            if((ix-nx/2)**2+(iy-ny/2)**2<r**2):
                u[ix,iy]=1.
    return u



Nargs = 6

if len(sys.argv) != Nargs:
    print("Number of arguments is incorrect!")
    exit("usage: python simulation_ex.py input_file N M Niter output_file")

start = time.time()

print("Starting a very time consuming simulations...")
fin=sys.argv[1]
N=int(sys.argv[2])
M=int(sys.argv[3])
Niter=int(sys.argv[4])
fout=sys.argv[5]

print("Parameters of the runs are:")
print(f"file = {fin}")
print(f"N = {N}")
print(f"M = {M}")
print(f"Niter = {Niter}")
print(f"output= {fout}")

input_para = {"file":fin,"N":N,"M":M,"Niter":Niter,"out":fout}
logging.info("Input parameters ---> {0}".format(input_para))
#fig = plt.figure()
ims = []

# initialise a log file
logging.info("Starting initialisation..")
# write time stamp  and list files in working directory

# generate a random images NxM (according to some distribution ?)
myu =init_fromfile(fin)

logging.info("Starting iterations..")
# perform a smoothing Niter
for i in range(Niter):
    print(f"counter iteration: {i}/{Niter}")
    newu= update(myu,r)
    myu= np.copy(newu)

    x = np.random.normal(3,2,10)
   
    logging.info('x_av  %.4f' ,np.mean(x))
    #im = plt.imshow(newu,vmin=0,vmax=1, animated=True)
    #ims.append([im])


logging.info("End iterations ...")

logging.info("Saving output ...")
mpimg.imsave(fout,myu)

end = time.time()
tsim = end - start

logging.info('Simulation time  %.4f' ,tsim)
logging.info('Simulation complete without errors')


