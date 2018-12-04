# isend_array
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
print comm, type(comm)
size = comm.Get_size()
print size, type(size) 
rank = comm.Get_rank()

a_size = 10
data = (1+rank)*numpy.arange(a_size,dtype=numpy.float64)
if rank == 0:
    req=comm.Isend([data,a_size,MPI.DOUBLE],1,11)
elif rank == 1:
    print 'on task',rank,'before recv:   data = ',data[1], data[a_size-1]
    req=comm.Irecv(data,source=0,tag=11)
    print req, type(req)
    re = False
    while re == False :
       re=MPI.Request.Test(req)
    print 'test result',re,type(re)
    re=MPI.Request.Wait(req)
    print 'wait result',re
    print 'on task',rank,'after recv:    data = ',data[1], data[a_size-1]

