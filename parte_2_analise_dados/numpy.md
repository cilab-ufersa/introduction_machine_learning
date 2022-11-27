# Biblioteca Numpy

Numpy é uma biblioteca para computação científica em Python. Ela é utilizada para trabalhar com arrays multidimensionais, que são mais eficientes que as listas do Python.


## Importando a biblioteca Numpy

Para importar a biblioteca Numpy, você pode utilizar o comando abaixo:

```python
import numpy as np
```

## Criando um array

Para criar um array, você pode utilizar o comando abaixo:

```python
array = np.array([1, 2, 3, 4, 5])
```

## Visualizando o array

Para visualizar o array, você pode utilizar o comando abaixo:

```python
array
```

Exemplo:

```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])

array
```

## Visualizando o tipo do array

Para visualizar o tipo do array, você pode utilizar o comando abaixo:

```python
array.dtype
```

Exemplo:

```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])

array.dtype
```

## Visualizando o formato do array

Para visualizar o formato/tamanho do array, você pode utilizar o comando abaixo:

```python
array.shape
```

Exemplo:

```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])

array.shape
```

## Criando um array multidimensional

Para criar um array multidimensional, você pode utilizar o comando abaixo:

```python
array = np.array([[1, 2, 3], [4, 5, 6]])
```

## Funções para criar arrays

Para criar arrays, você pode utilizar as funções abaixo:

```python
np.zeros((2, 3)) # Cria um array de zeros
np.ones((2, 3)) # Cria um array de uns
np.full((2, 3), 7) # Cria um array com o valor 7
np.eye(3) # Cria uma matriz identidade
np.random.random((2, 3)) # Cria um array com valores aleatórios
```

## Criando um array com valores sequenciais

Para criar um array com valores sequenciais, você pode utilizar o comando abaixo:

```python
np.arange(0, 10, 2) # Cria um array com valores de 0 a 10, pulando de 2 em 2
```

## Criando um array com valores espaçados uniformemente

Para criar um array com valores espaçados uniformemente, você pode utilizar o comando abaixo:

```python
np.linspace(0, 1, 5) # Cria um array com 5 valores de 0 a 1
```

## Visualizando o tamanho do array

Para visualizar o tamanho do array, você pode utilizar o comando abaixo:

```python
array.size
```

## Utilidade de arrays

Arrays são muito utilizados para trabalhar com dados numéricos. Por exemplo, você pode utilizar arrays para representar uma imagem, onde cada pixel é um número que representa a intensidade de cor. Ou você pode utilizar arrays para representar um sinal de áudio, onde cada amostra é um número que representa a intensidade sonora.

## Visualizando o número de dimensões do array

Para visualizar o número de dimensões do array, você pode utilizar o comando abaixo:

```python
array.ndim
```


## Ndarray 

Um ndarray é um array multidimensional, onde todos os elementos são do mesmo tipo. Os elementos de um ndarray são acessados por um índice, que é uma tupla de números inteiros não negativos. O número de índices é o número de dimensões do array. O ndarray possui os seguintes atributos:

* ndim: número de dimensões do array
* shape: tupla com o tamanho do array em cada dimensão
* size: número total de elementos do array
* dtype: tipo dos elementos do array

## Indexação de arrays

Para acessar um elemento de um array, você pode utilizar o comando abaixo:

```python
array[0, 0]
```

Exemplo:

```python
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

array[0, 0]
```

## Fatiamento de arrays

Para acessar uma fatia de um array, você pode utilizar o comando abaixo:

```python
array[0:2, 1]
```

Exemplo:

```python
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

array[0:2, 1]
```

## Indexação booleana

Para acessar elementos de um array utilizando uma condição, você pode utilizar o comando abaixo:

```python
array[array > 2]
```

