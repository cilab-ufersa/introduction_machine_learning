# Análise e visualização de dados machine learning 

No processo de aprendizado de máquina, a análise e visualização de dados é uma das etapas mais importantes. É nessa etapa que você vai entender melhor os dados que você está trabalhando, e vai conseguir identificar possíveis problemas que podem atrapalhar o seu modelo de aprendizado de máquina.

## Análise exploratória de dados com Python 

Para realizar a análise exploratória de dados, você pode utilizar a biblioteca Pandas. Essa biblioteca é uma das mais utilizadas para análise de dados em Python.

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




