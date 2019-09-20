# Algoritmo Genético - Quadrado Mágico

Genetic Algorithm - Magic Square (Quadrado Mágico)
Algoritmo Genético - Quadrado Mágico

@author Mathias Artur Schulz
@since 16/09/2019

O principal objetivo de um quadrado mágico é que a soma de cada linha, coluna e as duas diagonais sejam sempre iguais.

Um quadrado mágico pode ser de qualquer tamanho, no entanto deve ser constituído por uma tabela quadrada com valores aleatórios que não se repetem.

Para geração dos valores aleatórios, deve ser um random entre zero e o número de células da tabela. No entando essa configuração pode ser alterada para permitir valores randômicos em uma faixa maior, mas não menor, pois os valores não se repetem.

# Fitness
O fitness é calculado a partir da soma de cada linha, cada coluna e das duas diagonais, a partir das somas é realizado uma média entre as respectivas somas. Com isso, é realizado uma comparação de cada soma com a média e é calculado a diferença entre a respectiva soma e a média.

Caso o fitness seja igual a zero significa que a soma de cada linha, cada coluna e das duas diagonais são iguais, ou seja, é um quadrado mágico.

Quanto menor o fitness, melhor é o cromossomo.

# Exemplo de Resultado
-- Cromossomo:

[[ 2  9  7]

 [13  4  1]

 [ 6  5 10]]

-- Fitness:

9

-- Somas [Coluna1 Coluna2 Coluna3 Linha1 Linha2 Linha3 Diagonal1 Diagonal2]:

[21 18 18 18 18 21 16 17]

# Run
/usr/bin/python3 /home/matt/Workspace/AGQuadradoMagico/AGQuadradoMagico.py
