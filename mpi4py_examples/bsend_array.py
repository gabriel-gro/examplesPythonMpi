# bsend_array
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_sz = 1000
data = rank*numpy.arange(a_sz,dtype=numpy.int)
if rank == 0:
    buf = numpy.empty(a_sz+3,dtype = numpy.int)
    MPI.Attach_buffer(buf)
    comm.Bsend(data,dest=1,tag=11)
elif rank == 1:
    print 'on task',rank,'before recv:   data = ',data[a_sz-1]
    comm.Recv(data,source=0,tag=11)
    print 'on task',rank,'after recv:    data = ',data[a_sz-1]

