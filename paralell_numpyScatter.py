from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size() # new: gives number of ranks in comm
rank = comm.Get_rank()

numDataPerRank = 10
data = None
if rank == 0:
    # np.linspace( Start, stop, Quant de numeros)
    data = np.linspace(1, size*numDataPerRank, numDataPerRank*size)

# inicia um vetor com elementos vazio do tamando arg[0] | do tipo arg[1]
recvbuf = np.empty(numDataPerRank, dtype='d') # allocate space for recvbuf
comm.Scatter(data, recvbuf, root=0)

print('Rank: ',rank, ', recvbuf received: ',recvbuf)