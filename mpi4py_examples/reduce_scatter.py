# reduce_scatter
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

recv_size = range(1,size+1)
recvdata = numpy.zeros(recv_size[rank],dtype=numpy.int)
send_size = 0
for i in  range(0,size):
   send_size =send_size + recv_size[i]
senddata = (rank+1)*numpy.arange(send_size,dtype=numpy.int)
print 'on task',rank,'senddata  = ',senddata
comm.Reduce_scatter(senddata,recvdata,recv_size,op=MPI.SUM)
print 'on task',rank,'recvdata = ',recvdata

