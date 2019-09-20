import random
import numpy as np


POPULATION_SIZE = 500
GENERATIONS = 1000
PARENTS_SIZE = 2
MUTATION_PROBABILITY = 0.5
TABLE_SIZE = 3
CHROMOSOME_SIZE = TABLE_SIZE * TABLE_SIZE
MAX_VALUE_TABLE = CHROMOSOME_SIZE + CHROMOSOME_SIZE


# Criação de um indivíduo da população a partir de uma matriz numpy
def chromosome():
    return np.random.choice(
        MAX_VALUE_TABLE, size=(TABLE_SIZE, TABLE_SIZE), replace=False
    )


# Criação da população
def population():
    return [chromosome() for i in range(POPULATION_SIZE)]


# Método que realiza a soma de cada linha, coluna e diagonal do cromossomo
# Retorna um array com as somas
def sumMatrix(chromosome):
    # Realiza a soma das colunas, cada posição do array representa uma coluna
    arraySumColumn = np.sum(chromosome, axis=0)
    # Realiza a soma das linhas, cada posição do array representa uma linha
    arraySumRow = np.sum(chromosome, axis=1)
    # Realiza a soma da diagonal principal
    sumPrimaryDiagonal = np.trace(chromosome)
    # Realiza a soma da diagonal secundária a partir da inversão das linhas
    sumSecondaryDiagonal = np.trace(chromosome[::-1])
    # Concatenação de todas somas em um único array
    chromosomeSum = np.concatenate([
        arraySumColumn, arraySumRow, [sumPrimaryDiagonal], [sumSecondaryDiagonal]
    ])
    return chromosomeSum


# Converte os cromossomos de uma população em uma matriz
def populationArrayToMatrix(population):
    return [i.reshape(-1) for i in population]


# Converte os cromossomos de uma população em um array
def populationMatrixToArray(population):
    return [i.reshape(TABLE_SIZE, TABLE_SIZE) for i in population]


# Método que calcula o fitness de um chromosome
# Fitness: Soma das distâncias de cada soma com a média
# OBS: Quanto menor o fitness melhor o cromossomo é
def fitness(chromosome):
    chromosomeSum = sumMatrix(chromosome)
    # Realiza a média de todas as somas
    average = int(sum(chromosomeSum) / len(chromosomeSum))

    fitness = 0
    for i in range(len(chromosomeSum)):
        diff = chromosomeSum[i] - average
        fitness = fitness + (diff if diff > 0 else -diff)
    return fitness


# Método de seleçao dos pais e cruzamento
def selectionAndCrossover(population):
    # Monta um array com cada cromossomo e seu respectivo fitness
    chromosomeAndFitness = [(fitness(i), i) for i in population]
    # Ordena a população por fitness - Do pior (maior) fitness para o melhor (menor)
    populationByFitness = [
        i[1] for i in sorted(chromosomeAndFitness, key=lambda chromosome: chromosome[0], reverse=True)
    ]
    populationByFitness = populationMatrixToArray(populationByFitness)
    
    # Seleciona os pais, cromossomos com melhor fitness (fitness mais baixo)
    parents = populationByFitness[(len(populationByFitness) - PARENTS_SIZE):]

    # Passa pelos outros cromossomos realizando o crossover com os pais
    for i in range(len(populationByFitness) - PARENTS_SIZE):
        # Caso possua mais de dois pais, é selecionado aleatóriamente apenas dois
        parents = random.sample(parents, 2)
        
        # print('cromossomo atual: ')
        # print(populationByFitness[i])
        # PEGA UM PONTO DE CORTE RANDÔMICO PARA REALIZAR O CROSSOVER
        cutPoint = random.randint(1, CHROMOSOME_SIZE - 1)
        # print('ponto de corte')
        # print(cutPoint)
        # REALIZA O CROSSOVER
        # PEGA A PARTE DO PARENT 1 ANTES DO PONTO DE CORTE
        populationByFitness[i][:cutPoint] = parents[0][:cutPoint]
        # print('crossover 1: ')
        # print(populationByFitness[i])
        # PEGA A PARTE DO PARENT 2 A PARTIR DO PONTO DE CORTE
        populationByFitness[i][cutPoint:] = parents[1][cutPoint:]
        # print('crossover 2: ')
        # print(populationByFitness[i])

        # TRANSFORMAÇÃO DO CROMOSSOMO ATUAL NOVAMENTE EM UMA MATRIZ
        populationByFitness[i] = populationByFitness[i].reshape(TABLE_SIZE, TABLE_SIZE)
        # print('matriz ')
        # print(populationByFitness[i])
    return populationByFitness


# Função de mutação
# Utilizar valores pequenos de taxa de mutação para o algoritmo não ficar aleatório
def mutation(population):
    # PERCORRO OS CROMOSSOMOS SEM CONTAR OS PARENTS
    for i in range(len(population) - PARENTS_SIZE):
        # GERAÇÃO DE UM VALOR RANDÔMICO
        # CASO O RANDOM SEJA MENOR OU IGUAL A PROBABILIDADE DE MUTAÇÃO
        # OCORRERÁ A MUTAÇÃO
        if (random.random() <= MUTATION_PROBABILITY):
            # print(population[i])
            # TRANSFORMAÇÃO DO CROMOSSOMO ATUAL EM UM ARRAY PARA APLICAR A MUTAÇÃO
            population[i] = population[i].reshape(-1)
            # print(population[i])
            # GERAÇÃO DA POSIÇÃO DO ARRAY QUE TERÁ O VALOR ALTERADO (MUTAÇÃO)
            mutationPoint = random.randint(0, CHROMOSOME_SIZE - 1)
            # print('mutationPoint')
            # print(mutationPoint)
            # GERAÇÃO DO NOVO VALOR PARA MUTAÇÃO
            newValue = random.randint(1, MAX_VALUE_TABLE)
            # print('newValue')
            # print(newValue)
            while(newValue in population[i]):
                newValue = random.randint(1, MAX_VALUE_TABLE)
            population[i][mutationPoint] = newValue
            # print('population with mutation')
            # print(population[i])
            # TRANSFORMAÇÃO DO CROMOSSOMO ATUAL NOVAMENTE EM UMA MATRIZ
            population[i] = population[i].reshape(TABLE_SIZE, TABLE_SIZE)
            # print (population[i])
    return population

# Método para realizar a validação se um chromosome alcançou o objetivo
# esperado, que é o quadrado mágico
def validation(population):
    print('\n Validation: ')
    for chromosome in population:
        # Realiza a soma das colunas, cada posição do array representa uma coluna
        arraySumColumn = np.sum(chromosome, axis=0)
        # Realiza a soma das linhas, cada posição do array representa uma linha
        arraySumRow = np.sum(chromosome, axis=1)

        # Realiza a soma da diagonal principal
        sumPrimaryDiagonal = np.trace(chromosome)
        # Realiza a soma da diagonal secundária
        # Para pegar a diagonal secundária foi 
        # invertido as linhas do cromossomo
        # Tornando a diagonal secundária como primária
        sumSecondaryDiagonal = np.trace(chromosome[::-1])

        # Concatenação de todas somas em um único array
        arraySum = np.concatenate([
            arraySumColumn, arraySumRow, [sumPrimaryDiagonal], [sumSecondaryDiagonal]
        ])
        print(arraySum)

population = population()
print('População inicial: ')
[print(chromosome) for chromosome in population]
print('\n')
for i in range(GENERATIONS):
    population = selectionAndCrossover(population)
    population = mutation(population)
print('População Final: ')
[print(chromosome) for chromosome in population]

chromosomeAndFitness = [(fitness(i), i) for i in population]

# Ordena a população por fitness
# Do pior (maior) fitness para o melhor (menor)
population = [
    i[1] for i in sorted(chromosomeAndFitness, key=lambda chromosome: chromosome[0], reverse=True)
]
validation(population)

# Fitness | C1 | C2 | Cn | R1 | R2 | Rn | D1 | D2
