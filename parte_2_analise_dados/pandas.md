## Análise exploratória de dados com Python 

Para realizar a análise exploratória de dados, você pode utilizar a biblioteca Pandas. 

A biblioteca Pandas é uma biblioteca de código aberto, que fornece estruturas de dados e ferramentas de análise de dados para a linguagem de programação Python.  Essa biblioteca é uma das mais utilizadas para análise de dados em Python.

Na biblioteca Pandas, você pode manipular dados de forma muito simples. Você pode ler arquivos CSV, JSON, TXT, HTML, entre outros, e transformá-los em DataFrames, que são estruturas de dados muito utilizadas para análise de dados.

### import 

Os módulos Python podem obter acesso ao código de outro módulo importando o arquivo/função usando `import`.  Dessa forma, para realizar a importação de qualquer biblioteca no python utilizamos o comando ` import`. 

Exemplo: 

```python
import  nome_do_modulo
```
ou ainda 

```python
import  nome_do_modulo as ndm
```
Nesse último exemplo parâmetro "as" serve para renomearmos o nome da biblioteca e esse parâmetro é opcional. Ele é muito útil caso o nome da biblioteca esteja dando conflito com o nome de alguma variável.

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
