# bcast_array
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = numpy.empty(5,dtype=numpy.float64)
if rank == 0:
    data = numpy.arange(5,dtype=numpy.float64)
comm.Bcast([data,3,MPI.DOUBLE],root=0)
print 'on task',rank,'after recv:    data = ',data

