# Laços de repetição em Python 

Laços de repetição são estruturas de controle que permitem executar um bloco de código várias vezes.

## while

O while é uma estrutura de controle que permite executar um bloco de código enquanto uma condição for verdadeira.

```python
while condicao:
    # bloco de código
```

O bloco de código é executado enquanto a condição for verdadeira. Caso contrário, o bloco de código não é executado.

```python
contador = 0
while contador < 10:
    print(contador)
    contador += 1
```

## for

O for é uma estrutura de controle que permite executar um bloco de código para cada elemento de uma sequência.

```python
for elemento in sequencia:
    # bloco de código
```

O bloco de código é executado para cada elemento da sequência. Caso contrário, o bloco de código não é executado.

```python
for numero in range(10):
    print(numero)
```

## break

O break é uma palavra-chave que permite interromper um laço de repetição.

```python
while True:
    # bloco de código
    break
```

O bloco de código é executado até que o break seja executado.

```python
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 10:
        break
```

## continue

O continue é uma palavra-chave que permite interromper a execução do laço de repetição atual e continuar a execução do próximo laço de repetição.

```python
while True:
    # bloco de código
    continue
```

O bloco de código é executado até que o continue seja executado.

```python
contador = 0
while True:
    contador += 1
    if contador == 10:
        continue
    print(contador)
    if contador == 20:
        break
```

## else

O else é uma estrutura de controle que permite executar um bloco de código caso um laço de repetição seja executado até o fim.

```python
while condicao:
    # bloco de código
else:
    # bloco de código
```

O bloco de código do else é executado caso o laço de repetição seja executado até o fim. Caso contrário, o bloco de código do else não é executado.

```python
contador = 0
while contador < 10:
    print(contador)
    contador += 1
else:
    print('Fim do laço de repetição')
```

## Exercícios

1. Escreva um programa que imprima os números de 1 a 10.

2. Escreva um programa que imprima os números de 10 a 1.

3. Escreva um programa que imprima os números pares de 1 a 10.

4. Escreva um programa que imprima os números ímpares de 1 a 10.