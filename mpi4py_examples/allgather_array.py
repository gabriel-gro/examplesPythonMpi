# gather_array
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 4
senddata = (rank+1)*numpy.arange(a_size,dtype=numpy.float64)
recvdata = numpy.arange(size*a_size,dtype=numpy.float64)
comm.Allgather(senddata,recvdata)
print 'on task',rank,'after Gather:    data = ',recvdata

counts=(2,3,4)
dspls=(0,3,8)
recvdata = numpy.empty(12,dtype=numpy.float64)
comm.Allgatherv([senddata,counts[rank]],[recvdata,counts,dspls,MPI.DOUBLE])
print 'on task',rank,'after Gatherv:    data = ',recvdata


