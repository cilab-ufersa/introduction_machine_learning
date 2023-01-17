# Dicionários em Python 

Dicionários são estruturas de dados que permitem armazenar pares de chave e valor.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
}
```

O dicionário acima possui três pares de chave e valor. A chave é uma string e o valor pode ser qualquer tipo de dado.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}
```

## Acessando valores

Para acessar um valor de um dicionário, basta informar a chave do valor desejado.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

print(dicionario['chave1'])
print(dicionario['chave2'])
print(dicionario['chave3'])
```

## Adicionando valores

Para adicionar um valor a um dicionário, basta informar a chave e o valor desejado.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

dicionario['chave4'] = 'valor4'
dicionario['chave5'] = 5
dicionario['chave6'] = 6.0

print(dicionario)
```

## Removendo valores

Para remover um valor de um dicionário, basta utilizar a função `pop()`.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

dicionario.pop('chave1')

print(dicionario)
```

## Métodos

### keys()

O método `keys()` retorna uma lista com as chaves de um dicionário.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

print(dicionario.keys())
```

### values()

O método `values()` retorna uma lista com os valores de um dicionário.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

print(dicionario.values())
```

### items()

O método `items()` retorna uma lista com os pares de chave e valor de um dicionário.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

print(dicionario.items())
```

### clear()

O método `clear()` remove todos os pares de chave e valor de um dicionário.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

dicionario.clear()

print(dicionario)
```

### copy()

O método `copy()` retorna uma cópia de um dicionário.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

dicionario_copia = dicionario.copy()

print(dicionario_copia)
```

### fromkeys()

O método `fromkeys()` cria um dicionário com as chaves informadas e o valor informado.

```python
chaves = ['chave1', 'chave2', 'chave3']

dicionario = dict.fromkeys(chaves, 'valor')

print(dicionario)
```

### get()

O método `get()` retorna o valor de uma chave informada.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

print(dicionario.get('chave1'))
```

### popitem()

O método `popitem()` remove o último par de chave e valor de um dicionário.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

dicionario.popitem()

print(dicionario)
```

### setdefault()

O método `setdefault()` retorna o valor de uma chave informada. Caso a chave não exista, o valor informado é adicionado ao dicionário.

```python
dicionario = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

print(dicionario.setdefault('chave1', 'valor'))
print(dicionario.setdefault('chave4', 'valor'))
```

### update()

O método `update()` atualiza um dicionário com os pares de chave e valor de outro dicionário.

```python

dicionario1 = {
    'chave1': 'valor1',
    'chave2': 2,
    'chave3': 3.0,
}

dicionario2 = {
    'chave4': 'valor4',
    'chave5': 5,
    'chave6': 6.0,
}

dicionario1.update(dicionario2)

print(dicionario1)
```

## Exercícios

1. Crie um dicionário com 5 pares de chave e valor. Utilize o método `keys()` para exibir as chaves do dicionário. Utilize o método `values()` para exibir os valores do dicionário. Utilize o método `items()` para exibir os pares de chave e valor do dicionário. Utilize o método `clear()` para remover todos os pares de chave e valor do dicionário. Utilize o método `copy()` para criar uma cópia do dicionário. Utilize o método `fromkeys()` para criar um dicionário com as chaves informadas e o valor informado. Utilize o método `get()` para exibir o valor de uma chave informada. Utilize o método `popitem()` para remover o último par de chave e valor do dicionário. Utilize o método `setdefault()` para exibir o valor de uma chave informada. Caso a chave não exista, o valor informado é adicionado ao dicionário. Utilize o método `update()` para atualizar o dicionário com os pares de chave e valor de outro dicionário.

2. Crie um dicionário com 5 pares de chave e valor. Utilize o método `popitem()` para remover um par de chave e valor do dicionário. 
