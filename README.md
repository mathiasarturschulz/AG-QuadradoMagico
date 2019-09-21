# Genetic Algorithm - Magic Square (Quadrado Mágico) - Python

**@author** Mathias Artur Schulz

**@since** 16/09/2019


## Quadrados Mágicos

Um quadrado mágico é uma tabela de lado n, no qual a soma dos números das linhas, das colunas e das duas diagonais são sempre iguais. A respectiva tabela pode ser de qualquer tamanho, no entanto deve ser quadrada e possui valores que não se repetem.

Os quadrados mágicos podem ser classificados em três tipos, que são: Imperfeitos ou defeituosos, não obedecem a todas as regras, como um quadrado mágico em que a soma de todas as linhas e todas as colunas são iguais, mas as diagonais possuem somas diferentes; Hipermágicos, possuem propriedades adicionais, ou seja, obedecem às regras básicas, entretanto a troca de duas colunas de lugar formam outro quadrado mágico; Diabólicos, são quadrados hipermágicos com muitas propriedades ou com propriedades muito complexas, possuem esse nome devido a dificuldade de os formar.

Acredita-se que a origem do quadrado mágico tenha sido na China e na Índia, há cerca de 3000 anos, sendo que os quadrados mágicos ganharam esse nome devido ao fato da crença de que possuíam poderes especiais. Os chineses acreditavam que quem possuísse um quadrado mágico também possuiria sorte e felicidade para toda a vida. Além disso, acreditavam que os quadrados mágicos possuíam símbolos que reuniam os princípios básicos que formavam o universo, no qual os números pares simbolizavam o princípio feminino (Yin), os números ímpares simbolizavam o princípio masculino (Yang), o número 5 representava a Terra, os números 1 e 6 a água, 2 e 7 o fogo, 3 e 8 madeira e 4 e 9 os metais.

No século XV, os quadrados mágicos se tornaram conhecidos na Europa, sendo relacionados com a alquimia e a astrologia. Um quadrado mágico gravado numa placa de prata era usado como amuleto contra a peste, além disso, cada quadrado mágico de ordem 3 até a ordem 9 representava um planeta, que são: Ordem 3 representava Saturno; Ordem 4 representava Júpiter, Ordem 5 representava Marte; Ordem 6 representava Solenoide; Ordem 7 representava Vénus; Ordem 8 representava Mercúrio e ordem 9 representava Luna.

O presente relatório técnico possui como objetivo apresentar a construção de um algoritmo genético desenvolvido na linguagem de programação Python com o propósito de resolver o problema do quadrado mágico. Será abordado e explicado a forma de representação do cromossomo, o fitness e os operadores genéticos, por fim será apresentado o código e os testes realizados.

##### Link de Referência:
http://www.mat.uc.pt/~mat0717/public_html/Cadeiras/1Semestre/O%20que%20%C3%A9%20um%20quadrado%20m%C3%A1gico.pdf



## Representação Cromossomial

Para a representação de um cromossomo foi utilizado uma matriz construída a partir da função *random.choice* da biblioteca NumPy, disponível para a linguagem de programação Python.

A matriz quadrada possui ordem n e valores aleatórios que não se repetem. Para geração dos valores aleatórios, sempre será um valor inteiro maior que zero, sendo que o valor máximo permitido será o número de células da matriz ao quadrado, no entanto esse valor pode ser facilmente configurado nas variáveis iniciais do algoritmo. No entanto, o valor máximo a ser gerado não deve ser menor que o número de células da matriz, devido ao fato de não ser permitido valores repetidos.


## Fitness (Função de Avaliação)

Para geração do fitness de um cromossomo, primeiramente é realizado a soma de cada linha, coluna e das duas diagonais, sendo que cada soma é armazenada em uma posição do array de somas. Com isso, a partir das somas encontradas, é realizado uma média das somas.

Após o cálculo das somas e a média das somas, é realizado uma comparação de cada soma do array de somas com a média e é calculado a diferença entre a respectiva soma e a média. Com isso, o fitness será a soma das diferenças encontradas.

Neste algoritmo, quanto menor o fitness, melhor é o cromossomo. Caso o fitness seja igual a zero, significa que a soma de cada linha, cada coluna e das duas diagonais são iguais, ou seja, é um quadrado mágico.


## Operadores Genéticos (Mutação e Crossover)

Para a realização do crossover, primeiramente são selecionados os pais da população, os pais são os melhores cromossomos, a quantidade de pais que serão selecionados podem ser determinados a partir de uma variável inicial do algoritmo.

No processo de crossover é passado por todos os outros cromossomos que não são pais, para cada cromossomo é selecionado aleatoriamente dois pais e é realizado o crossover. Sendo que para cada cromossomo a ser realizado o crossover existe um ponto de corte randômico, o ponto de corte divide o cromossomo atual em duas partes, a primeira parte receberá a parte correspondente do pai 1 e a segunda parte receberá a parte correspondente do pai 2.

Para realização da mutação, primeiramente é determinado uma probabilidade de mutação a partir de uma variável inicial, por padrão determinada com 0.5 de probabilidade de mutação. Com isso, é percorrido todos os cromossomos que não são pais, para cada cromossomo é gerado um número float randômico entre zero e um, caso o número gerado seja menor ou igual a probabilidade de mutação, então ocorrerá a mutação.

Na mutação é gerado um ponto do cromossomo onde ocorrerá a mutação e para essa posição do cromossomo será gerado um novo valor, ocorrendo a mutação no cromossomo. No entanto, o novo valor deve ser diferente de todos os outros presentes no cromossomo.


##### Formato de resultado

Inicialmente será apresentando todos os cromossomos da população e então será realizando a evolução das gerações (crossover e mutações). Por fim será apresentado a última geração obtida, apresentando do pior cromossomo até o melhor cromossomo da geração.

Para cada cromossomo é apresentado o cromossomo obtido, o fitness e o array de somas de cada coluna, linha e as duas diagonais, exemplo com tabela de ordem 3:

-- Cromossomo:

[[ valor11  valor12  valor13]

 [ valor21  valor22  valor23]

 [ valor31  valor32  valor33]]

-- Fitness:

valor_fitness

-- Array de somas

[coluna01 coluna02 coluna03 linha01 linha02 linha03 diagonal01 diagonal02]:


##### Exemplo de Resultado

[[ 2  9  7]

 [13  4  1]

 [ 6  5 10]]


9


[21 18 18 18 18 21 16 17]


## Exemplo de como rodar
/usr/bin/python3 /home/matt/Workspace/AGQuadradoMagico/AGQuadradoMagico.py
