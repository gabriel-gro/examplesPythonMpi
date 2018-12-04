# scatter
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

rootdata = None
if rank == 0:
    rootdata = (1,2,3,(4,5))
data = comm.scatter(rootdata,root=0)
print 'on task',rank,'after bcast:    data = ',data,type(rootdata)

