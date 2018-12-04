# gather_array
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 4
recvdata = None
senddata = (rank+1)*numpy.arange(a_size,dtype=numpy.float64)
if rank == 0:
   recvdata = numpy.arange(size*a_size,dtype=numpy.float64)
comm.Gather(senddata,recvdata,root=0)
print 'on task',rank,'after Gather:    data = ',recvdata

counts=(2,3,4)
dspls=(0,3,8)
if rank == 0:
   recvdata = numpy.empty(12,dtype=numpy.float64)
sendbuf = [senddata,counts[rank]]
recvbuf = [recvdata,counts,dspls,MPI.DOUBLE]
comm.Gatherv(sendbuf,recvbuf,root=0)
print 'on task',rank,'after Gatherv:    data = ',recvdata


