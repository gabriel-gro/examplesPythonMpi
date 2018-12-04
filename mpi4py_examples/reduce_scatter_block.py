# reduce_scatter_block
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 3
recvdata = numpy.zeros(a_size,dtype=numpy.int)
senddata = (rank+1)*numpy.arange(size*a_size,dtype=numpy.int)
print 'on task',rank,'senddata  = ',senddata
comm.Reduce_scatter_block(senddata,recvdata,op=MPI.SUM)
print 'on task',rank,'recvdata = ',recvdata

