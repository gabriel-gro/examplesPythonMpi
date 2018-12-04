# bcast
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

rootdata = None
if rank == 0:
    rootdata = (1,'a','z',3.14) 
data = comm.bcast(rootdata,root=0)
print 'on task',rank,'after bcast:    data = ',data

