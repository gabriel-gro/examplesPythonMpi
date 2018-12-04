#status.py
from mpi4py import MPI
import numpy 

comm = MPI.COMM_WORLD
nproc = comm.Get_size()
myid = comm.Get_rank()

data = myid*numpy.ones(5,dtype = numpy.float64)

if myid == 0:
   comm.Send([data,3,MPI.DOUBLE],dest=1,tag=1)
if myid == 1:
   info = MPI.Status()
   comm.Recv(data,MPI.ANY_SOURCE,MPI.ANY_TAG,info)
   source = info.Get_source()
   tag = info.Get_tag()
   count = info.Get_elements(MPI.DOUBLE)
   size = info.Get_count()
   print 'on',myid, 'source, tag, count, size is',source, tag, count, size 


