# Análise e visualização de dados machine learning 

1. [NumPy](https://github.com/cilab-ufersa/introduction_machine_learning/blob/develop/parte_2_analise_dados/numpy.md)
2. [Pandas](https://github.com/cilab-ufersa/introduction_machine_learning/tree/develop/parte_2_analise_dados)
3. [Matplotlib](https://github.com/cilab-ufersa/introduction_machine_learning/blob/develop/parte_2_analise_dados/matplotlib.md) 

- [Projeto 02](https://github.com/cilab-ufersa/introduction_machine_learning/tree/develop/parte_2_analise_dados/projeto_02)

- [Projeto 03](https://github.com/cilab-ufersa/introduction_machine_learning/tree/develop/parte_2_analise_dados/projeto_3)

No processo de aprendizado de máquina, a análise e visualização de dados é uma das etapas mais importantes. É nessa etapa que você vai entender melhor os dados que você está trabalhando, e vai conseguir identificar possíveis problemas que podem atrapalhar o seu modelo de aprendizado de máquina.


Existem algumas bibliotecas que podem te ajudar nessa etapa, como o Pandas, Matplotlib, Numpy e Seaborn. Nesse curso, vamos usar o Pandas, Numpy e Matplotlib para fazer a análise e visualização dos dados.

Você pode consultar a documentação do Pandas [aqui](https://pandas.pydata.org/pandas-docs/stable/), do Numpy [aqui](https://numpy.org/doc/stable/) e do Matplotlib [aqui](https://matplotlib.org/contents.html). 

--- 

## Análise exploratória de dados com Python 

Para realizar a análise exploratória de dados, você pode utilizar a biblioteca Pandas. Essa biblioteca é uma das mais utilizadas para análise de dados em Python.

## import
Para realizar a importação de qualquer biblioteca no python utilizamos o comando "import", o parâmetro "as" serve para renomearmos o nome da biblioteca e esse parâmetro é opcional. Ele é muito útil caso o nome da biblioteca esteja dando conflito com o nome de alguma variável.

### Importando a biblioteca Pandas

Para importar a biblioteca Pandas, você pode utilizar o comando abaixo:

```python
import pandas as pd
```

### Carregando os dados

Para carregar os dados, você pode utilizar o comando abaixo:

```python
df = pd.read_csv('caminho_do_arquivo')
```

### Visualizando os dados

Para visualizar os dados, você pode utilizar o comando abaixo:

```python
df.head()
```

Exemplo: 

```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv')

df.head()
```


### Visualizando as informações dos dados

Para visualizar as informações dos dados, você pode utilizar o comando abaixo:

```python
df.info()
```

### Visualizando as estatísticas dos dados

Para visualizar as estatísticas dos dados, você pode utilizar o comando abaixo:

```python
df.describe()
```

### Visualizando a correlação dos dados

Para visualizar a correlação dos dados, você pode utilizar o comando abaixo:

```python
df.corr()
```

### Visualizando a quantidade de valores únicos

Para visualizar a quantidade de valores únicos, você pode utilizar o comando abaixo:

```python
df['nome_da_coluna'].value_counts()
```

## Criando dataframes

Para criar dataframes, você pode utilizar o comando abaixo:

```python
df = pd.DataFrame(dicionario)
```

Exemplo:

```python
import pandas as pd

dicionario = {
    'nome': ['João', 'Maria', 'José'],
    'idade': [20, 25, 30]
}

df = pd.DataFrame(dicionario)

df.head()
```



