from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num = 10

vet = [i for i in range(num)]

# np.array cria vetor -> arg[0]: Obj | arg[1] type
value = np.array(vet, int)

print(' Rank: ',rank, ' value = ', value)

#para cada posicao do objete em cada processo é necessario ter uma posicao para passagem de valores
recv = np.empty(num, dtype=int)

# Iniciando os arrays que irao conter os valores dos resultados a seguir:
value_sum = np.array(recv, int)
value_max = np.array(recv, int)

# perform the reductions:
# Reduce -> Arg[0]: Obj com todo valore 
#           Arg[1]: obj a receber o fator de operacao
#           Arg[2]: Operação escolhida / example in end page
#           Arg[3]: De quem ira armazenar este resultado
comm.Reduce(value, value_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(str(rank) + "- value_sum = " + str(value_sum))


#   REDUCE OPERATIONS
# MPI.MIN        minimum
# MPI.MAX        maximum
# MPI.SUM        sum
# MPI.PROD       product
# MPI.LAND       logical and
# MPI.BAND       bitwise and
# MPI.LOR        logical or
# MPI.BOR        bitwise or
# MPI.LXOR       logical xor
# MPI.BXOR       bitwise xor
# MPI.MAXLOC     max value and location
# MPI.MINLOC     min value and location