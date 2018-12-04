# scatter_array
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 4
recvdata = numpy.empty(a_size+rank,dtype=numpy.float64)
senddata = None 
if rank == 0:
   senddata = numpy.arange(size*a_size,dtype=numpy.float64)
comm.Scatter(senddata,recvdata,root=0)
print 'on task',rank,'after Scatter:    data = ',recvdata

recvdata = numpy.empty(a_size,dtype=numpy.float64)
counts = None
dspls = None
if rank == 0:
   senddata = numpy.arange(100,dtype=numpy.float64)
   counts=(1,2,3)
   dspls=(4,3,10)
comm.Scatterv([senddata,counts,dspls,MPI.DOUBLE],recvdata,root=0)
print 'on task',rank,'after Scatterv:    data = ',recvdata


