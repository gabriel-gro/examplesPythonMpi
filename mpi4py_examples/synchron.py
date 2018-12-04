#synchron.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def synchron():
   buf = None
   if rank == 0:
      for ip in range(1,size):
         comm.send(buf,dest=ip)
         buf=comm.recv(source=ip)
      for ip in range(1,size):
         comm.send(buf,dest=ip)
   else:
     buf=comm.recv(source=0)
     comm.send(buf,dest=0)
     buf = comm.recv(source=0)

for ip in  range(0,size):
   if rank == ip:
      print 'rank',rank,'ready'
   synchron()
