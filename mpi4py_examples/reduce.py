# reduce
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

senddata = rank+1,rank
recvdata = comm.reduce(senddata,root=0,op=MPI.PROD)
print rank,type(senddata),type(recvdata)
print 'on task',rank,'after reduce:    data = ',recvdata

