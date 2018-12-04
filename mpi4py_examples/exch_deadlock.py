# exch_deadlock
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 10
send_data=rank*numpy.arange(a_size,dtype=numpy.float64)
recv_data=-numpy.empty(a_size,dtype=numpy.float64)
ipr = (rank +1)%size
ipl = (rank -1)%size
#comm.Ssend(send_data,dest=ipl)
#comm.Srecv(recv_data,source=ipr)
comm.Sendrecv(send_data,dest=ipl,recvbuf=recv_data,source=ipr)
print 'on task',rank,'after exchange ',send_data[1],recv_data[1]
