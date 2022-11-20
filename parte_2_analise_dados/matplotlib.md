# Biblioteca Matplotlib

A biblioteca Matplotlib é uma biblioteca de visualização de dados em Python. Ela permite que você crie gráficos de linhas, gráficos de dispersão, histogramas, gráficos de barras, gráficos de pizza, etc. Com ela, você pode criar gráficos de alta qualidade com apenas algumas linhas de código.

## Instalação

Para instalar a biblioteca Matplotlib, basta executar o seguinte comando no terminal:

```bash
pip install matplotlib
```

## Importando a biblioteca

Para importar a biblioteca Matplotlib, basta executar o seguinte comando:

```python
import matplotlib.pyplot as plt
```

## Criando um gráfico de linha

Para criar um gráfico de linha, basta executar o seguinte código:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)

plt.show()
```

## Criando um gráfico de dispersão

Para criar um gráfico de dispersão, basta executar o seguinte código:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.scatter(x, y)

plt.show()
```

## %matplotlib inline

O comando `%matplotlib inline` é usado para mostrar os gráficos no Jupyter Notebook.

Exemplo:

```python   
%matplotlib inline

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
```
