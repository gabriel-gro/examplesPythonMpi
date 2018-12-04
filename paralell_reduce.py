from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

value = list(int(rank))
print('Rank: ', rank, ' value = ', value)
value = None

comm.reduce(value, op = MPI.SUM, root=0)

if rank == 0:
    print(' Rank 0: value_sum = ',value)