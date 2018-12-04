# alltoall
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data0 = ['rank',rank]
data1 = [1,'rank',rank]
senddata=(data0,data1)
print 'on task',rank,'    senddata = ',senddata
recvdata = comm.alltoall(senddata)
print 'on task',rank,'    recvdata = ',recvdata

