from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    data = None

    numDataForRank = 10
    data = [(rank + 1) * i for i in range(numDataForRank)]


    # Processo busca atualizar dados da variavel em outro processo (deve existir a variavel em todos)
    data = comm.gather(data, root=0)
    if rank == 0:
        print('Rank: ',rank,', data: ' ,data)

main()