# Laços de repetição em Python 

Laços de repetição são estruturas de controle que permitem executar um bloco de código várias vezes. Existe dois tipos de laços de repetição em Python: **for** e **while**. 

## while

O while é uma estrutura de controle que permite executar um bloco de código enquanto uma condição for verdadeira. Sua sintaxe é:


```python
while condicao:
    # bloco de código
```

O bloco de código é executado enquanto a condição for verdadeira. Caso contrário, o bloco de código não é executado.

Exemplo:

```python
contador = 0
while contador < 10:
    print(contador)
    contador += 1
```

No exemplo acima, o bloco de código é executado enquanto o contador for menor que 10. A cada iteração, o contador é incrementado em 1. 

## for

O for é uma estrutura de controle que permite executar um bloco de código varias vezes. No exemplo a seguir, o laço for é executado  para cada elemento de uma sequência.

```python
for elemento in sequencia:
    # bloco de código
```

O bloco de código é executado para cada elemento da sequência. Caso contrário, o bloco de código não é executado.

Exemplo:

```python
for numero in range(10):
    print(numero)
```

No exemplo acima, o bloco de código é executado para cada elemento da sequência. A sequência é gerada pelo método range(). O método range() gera uma sequência de números inteiros. O método range() recebe como parâmetro a quantidade de numeros sequência. Portanto, range(10) gera os números de 0 a 9. Assim, o bloco de código é executado 10 vezes, em que cada iteração a variavel numero recebe um valor diferente, iniciando em 0 e terminando em 9.

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
