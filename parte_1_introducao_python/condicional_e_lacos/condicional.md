# Condicional em Python 

Condicional é uma estrutura de controle que permite executar um bloco de código caso uma condição seja verdadeira.

## if

O if é uma estrutura de controle que permite executar um bloco de código caso uma condição seja verdadeira.

```python
if condicao:
    # bloco de código
```

O bloco de código é executado caso a condição seja verdadeira. Caso contrário, o bloco de código não é executado.

```python
if 2 > 1:
    print('2 é maior que 1')
```

## else

O else é uma estrutura de controle que permite executar um bloco de código caso uma condição seja falsa.

```python
if condicao:
    # bloco de código
else:
    # bloco de código
```

O bloco de código do else é executado caso a condição seja falsa. Caso contrário, o bloco de código do else não é executado.

```python

if 2 < 1:
    print('2 é menor que 1')
else:
    print('2 é maior que 1')
```

## elif

O elif é uma estrutura de controle que permite executar um bloco de código caso uma condição seja verdadeira. O elif é uma abreviação de else if.

```python

if condicao:
    # bloco de código
elif condicao:
    # bloco de código
else:
    # bloco de código
```

O bloco de código do elif é executado caso a condição seja verdadeira. Caso contrário, o bloco de código do elif não é executado.

```python
if 2 < 1:
    print('2 é menor que 1')
elif 2 > 1:
    print('2 é maior que 1')
else:
    print('2 é igual a 1')
```

## Operadores de comparação

Os operadores de comparação são utilizados para comparar valores. Os operadores de comparação são:

| Operador | Descrição |
|----------|-----------|
| ==       | Igual a   |
| !=       | Diferente de |
| >        | Maior que |
| <        | Menor que |
| >=       | Maior ou igual a |
| <=       | Menor ou igual a |

```python
print(2 == 2) # True
print(2 != 2) # False
print(2 > 2) # False
print(2 < 2) # False
print(2 >= 2) # True
print(2 <= 2) # True
```

## Operadores lógicos

Os operadores lógicos são utilizados para combinar condições. Os operadores lógicos são:

| Operador | Descrição |
|----------|-----------|
| and      | E         |
| or       | Ou        |
| not      | Não       |

```python
print(2 == 2 and 2 > 1) # True
print(2 == 2 or 2 > 1) # True
print(not 2 == 2) # False
```

## Operadores de identidade

Os operadores de identidade são utilizados para comparar objetos. Os operadores de identidade são:

| Operador | Descrição |
|----------|-----------|
| is       | É         |
| is not   | Não é     |

```python   
print(2 is 2) # True
print(2 is not 2) # False
```

## Operadores de associação

Os operadores de associação são utilizados para verificar se um valor faz parte de um objeto. Os operadores de associação são:

| Operador | Descrição |
|----------|-----------|
| in       | Está em   |
| not in   | Não está em |

```python
lista = [1, 2, 3]
print(1 in lista) # True
print(1 not in lista) # False
```

## Exercícios

1. Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

2. Escreva um programa que leia um número inteiro e mostre na tela se ele é positivo ou negativo.

3. Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar e se é positivo ou negativo.
