# send
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = None
if rank == 0:
    data = (1,'a','z',3.14) 
    comm.send(data,1)
elif rank == 1:
#    buf=[1,1]
    buf = bytearray(100)
    print 'on task',rank,'before recv:   data = ',data
    data = comm.recv(obj=buf)
    print 'on task',rank,'after recv:    data = ',data

