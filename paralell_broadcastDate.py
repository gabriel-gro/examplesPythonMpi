from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        data = [1, 2, 3]
    if rank == 1:
        data = [3, 0, 0]
    else:
        data = None

    # Processo busca atualizar dados da variavel em outro processo (deve existir a variavel em todos)
    data = comm.bcast(data, root=0)
    print('Rank: ',rank,', data: ' ,data)

main()