## Variáveis 

Em Python, não é necessário declarar o tipo de uma variável, mas o interpretador irá verificar o tipo da variável em tempo de execução.

Além disso, o interpretador não faz correções automáticas entre tipos incompatíveis. Para realizar a operação entre tipos não compatíveis, é necessário converter explicitamente o tipo da variável ou variáveis antes da operação.

### Declaração de variáveis

Em Python, a declaração de variáveis é feita da seguinte forma:

```python
nome_da_variavel = valor_da_variavel
```

### Tipos de variáveis

Em Python, existem os seguintes tipos de variáveis:

* Inteiro (int)
* Real (float)
* String (str)
* Booleano (bool)
* Complexo (complex)
* Lista (list)
* Tupla (tuple)
* Dicionário (dict)
* Conjunto (set)

#### Inteiro (int)

O tipo inteiro é utilizado para representar números inteiros, ou seja, números sem casas decimais. Em Python, não existe limite para o tamanho de um número inteiro.

```python
inteiro = 10
```

#### Real (float)

O tipo real é utilizado para representar números reais, ou seja, números com casas decimais. Em Python, não existe limite para o tamanho de um número real.

```python

real = 10.5
```

#### String (str)

O tipo string é utilizado para representar textos. Em Python, não existe limite para o tamanho de uma string.

```python
string = "Olá, mundo!"
```

#### Booleano (bool)

O tipo booleano é utilizado para representar valores lógicos, ou seja, verdadeiro ou falso. Em Python, o valor verdadeiro é representado por True e o valor falso é representado por False.

```python
booleano = True
```

#### Complexo (complex)

O tipo complexo é utilizado para representar números complexos, ou seja, números que possuem parte real e parte imaginária. Em Python, não existe limite para o tamanho de um número complexo.

```python
complexo = 10 + 5j
```

#### Lista (list)

O tipo lista é utilizado para representar uma coleção de valores. Em Python, uma lista pode conter valores de tipos diferentes.

```python
lista = [1, 2, 3, 4, 5]
```

Para remover um elemento de uma lista, basta utilizar o método remove().

```python
lista.remove(3)
```

Para adicionar um elemento em uma lista, basta utilizar o método append().

```python
lista.append(6)
```

#### Tupla (tuple)

Assim como as listas, o tipo tupla é utilizado para representar uma coleção de valores. Porém, as tuplas são imutáveis, ou seja, não é possível adicionar, remover ou alterar valores de uma tupla.

```python
tupla = (1, 2, 3, 4, 5)
```

Após a criação de uma tupla, não é possível alterar valores.



#### Dicionário (dict)

O tipo dicionário é utilizado para representar uma coleção de valores. Em Python, um dicionário é composto por pares de chave e valor.

```python
dicionario = {"nome": "João", "idade": 20}
```

#### Conjunto (set)

O tipo conjunto é utilizado para representar uma coleção de valores. Em Python, um conjunto não permite valores duplicados.

```python
conjunto = {1, 2, 3, 4, 5}
```

## Operadores

Em Python, existem os seguintes operadores:

* Aritméticos
* Relacionais
* Lógicos
* Atribuição
* Identidade
* Membro
* Bitwise

### Aritméticos

Os operadores aritméticos são utilizados para realizar operações aritméticas.

| Operador | Descrição | Exemplo |
| --- | --- | --- |
| + | Adição | 10 + 5 |
| - | Subtração | 10 - 5 |
| * | Multiplicação | 10 * 5 |
| / | Divisão | 10 / 5 |
| % | Módulo | 10 % 5 |
| // | Divisão inteira | 10 // 5 |
| ** | Exponenciação | 10 ** 5 |

### Relacionais

Os operadores relacionais são utilizados para realizar comparações entre valores.

| Operador | Descrição | Exemplo |
| --- | --- | --- |
| == | Igual | 10 == 5 |
| != | Diferente | 10 != 5 |

### Lógicos

Os operadores lógicos são utilizados para realizar operações lógicas.

| Operador | Descrição | Exemplo |
| --- | --- | --- |
| and | E | 10 and 5 |
| or | Ou | 10 or 5 |
| not | Não | not 10 |

### Atribuição

Os operadores de atribuição são utilizados para atribuir valores a variáveis.

| Operador | Descrição | Exemplo |
| --- | --- | --- |
| = | Atribuição | x = 10 |
| += | Atribuição de adição | x += 10 |
| -= | Atribuição de subtração | x -= 10 |
| *= | Atribuição de multiplicação | x *= 10 |

### Identidade

Os operadores de identidade são utilizados para verificar se duas variáveis são iguais ou diferentes.

| Operador | Descrição | Exemplo |
| --- | --- | --- |
| is | Igual | x is y |
| is not | Diferente | x is not y |

### Membro

Os operadores de membro são utilizados para verificar se um valor pertence a uma coleção.

| Operador | Descrição | Exemplo |
| --- | --- | --- |
| in | Pertence | x in y |
| not in | Não pertence | x not in y |

### Bitwise

Os operadores bitwise são utilizados para realizar operações bitwise.

| Operador | Descrição | Exemplo |
| --- | --- | --- |
| & | AND | 10 & 5 |
| \| | OR | 10 \| 5 |
| ^ | XOR | 10 ^ 5 |
| ~ | NOT | ~10 |
| << | Deslocamento à esquerda | 10 << 5 |
| >> | Deslocamento à direita | 10 >> 5 |

