# author Mathias Artur Schulz
# since 16/09/2019

# Genetic Algorithm - Magic Square (Quadrado Mágico)

# Um Quadrado Mágico (QM) de ordem 3 é construído distribuindo-se os números de 1 a 9 
# nas casas de uma tabela 3×3, um em cada casa, de maneira que a soma dos números de cada 
# coluna, linha ou diagonal seja sempre a mesma.

# Constituído por uma tabela quadrada com valores aleatório que não se repetem.
# No qual a soma dos números de cada linha, coluna e das duas diagonais será sempre a mesma.

# Indivíduos com fitness melhor reproduzem mais

# RUN:
# /usr/bin/python3 /home/matt/Workspace/AGQuadradoMagico/AGQuadradoMagico.py

import random
import numpy as np

POPULATION_SIZE = 10
PARENTS_SIZE = 2
MUTATION_PROBABILITY = 0.5
TABLE_SIZE = 3
CHROMOSOME_SIZE = TABLE_SIZE * TABLE_SIZE
MAX_VALUE_TABLE = CHROMOSOME_SIZE + CHROMOSOME_SIZE

# Criação de um indivíduo da população
# Utilizando uma matriz numpy
def chromosome():
    return np.random.choice(
        MAX_VALUE_TABLE, size=(TABLE_SIZE, TABLE_SIZE), replace=False
    )

# Criação da população
def population():
    return [chromosome() for i in range(POPULATION_SIZE)]

# Função que avalia o fitness de um indivíduo
# Verifica se é um bom gene para reprodução
# Classifica o chromosome
def fitness(chromosome):
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
    # Realiza a média de todas as somas
    average = int(sum(arraySum) / len(arraySum))

    # Cálculo do fitness (Quanto menor o fitness melhor o cromossomo é)
    # É realizado uma soma das distâncias de cada soma com a média
    # Quando maior a soma final, pior é o cromossomo
    fitness = 0
    for i in range(len(arraySum)):
        diff = arraySum[i] - average
        fitness = fitness + (diff if diff > 0 else -diff)
    return fitness

# Método de seleçao dos pais e cruzamento
def selectionAndCrossover(population):
    # Monta um array com cada cromossomo e seu respectivo fitness
    chromosomeAndFitness = [(fitness(i), i) for i in population]

    # Ordena a população por fitness
    # Do pior (maior) fitness para o melhor (menor)
    populationByFitness = [
        i[1] for i in sorted(chromosomeAndFitness, key=lambda chromosome: chromosome[0], reverse=True)
    ]
    # print('\n Chromosomes: ')
    # [print(chromosome) for chromosome in populationByFitness]
    
    # SELECIONA OS CROMOSSOMOS COM O MELHOR FITNESS DE ACORDO COM A VARIAVEL PARENTS
    parents = populationByFitness[(len(populationByFitness) - PARENTS_SIZE):]
    # print('\n Melhores:')
    # [print(chromosome) for chromosome in parents]

    # print('\n Resto')
    # É PASSADO PELOS OUTROS CROMOSSOMOS E REALIZADO O CROSSOVER
    for i in range(len(populationByFitness) - PARENTS_SIZE):
        # CASO HAJA MAIS DE DOIS PARENTS É SELECIONADO DE FORMA ALEATÓRIA APENAS DOIS
        parents = random.sample(parents, 2)
        parents = [i.reshape(-1) for i in parents]
        # print('\n parents')
        # print(parents)
        # TRANSFORMAÇÃO DO CROMOSSOMO ATUAL EM UM ARRAY PARA APLICAR O CROSSOVER
        populationByFitness[i] = populationByFitness[i].reshape(-1)
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
            while(newValue == population[i][mutationPoint]):
                newValue = random.randint(1,9)
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
for i in range(100):
    population = selectionAndCrossover(population)
    population = mutation(population)
print('População Final: ')
[print(chromosome) for chromosome in population]

validation(population)

