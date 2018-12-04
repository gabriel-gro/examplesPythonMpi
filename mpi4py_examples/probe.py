#probe.py
from mpi4py import MPI
import numpy 

comm = MPI.COMM_WORLD
nproc = comm.Get_size()
myid = comm.Get_rank()

if myid == 0:
   data = myid*numpy.ones(5,dtype = numpy.float64)
   comm.Send([data,3,MPI.DOUBLE],dest=1,tag=1)
if myid == 1:
   info = MPI.Status()
   comm.Probe(MPI.ANY_SOURCE,MPI.ANY_TAG,info)
   count = info.Get_elements(MPI.DOUBLE)
   data = numpy.empty(count,dtype = numpy.float64)
   comm.Recv(data,MPI.ANY_SOURCE,MPI.ANY_TAG,info)
   print 'on',myid, 'data: ',data


