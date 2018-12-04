# gather
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

senddata = ['rank',rank]
rootdata = comm.gather(senddata,root=0)
print 'on task',rank,'after bcast:    data = ',rootdata

