'PREÇO OUTLIER DOS DIAMANTES'

import seaborn

diamonds_ds = seaborn.load_dataset('diamonds')

with seaborn.axes_style('whitegrid'):

  diamonds_graph = seaborn.boxplot(x=diamonds_ds['price']) # o boxplot só precisa de uma coluna. Porém, é possível gerar o gráfico a partir de uma tabela completa.

  diamonds_graph.set(title='Preços dos diamantes', xlabel='Preço (USD)')



'CORRELAÇÃO PREÇO POR PESO DE CADA TIPO DE TRANSPARÊNCIA'

import seaborn

diamonds_ds = seaborn.load_dataset('diamonds')[['price', 'carat', 'clarity']].groupby('clarity').agg('mean')

with seaborn.axes_style('whitegrid'):

  diamonds_grapho = seaborn.scatterplot(data=diamonds_ds, x='price', y='carat', hue='clarity')

  diamonds_grapho.set(title='Correlação preço por peso dos tipos de transparência.', xlabel='Preço', ylabel='Peso')

  diamonds_grapho.get_legend().set_title('Transparência')



'DISTRIBUIÇÃO CONTÍNUA APROXIMADA DO PESO DOS CARROS'

# por tipos de carro

import seaborn

mpg_ds = seaborn.load_dataset('mpg')

with seaborn.axes_style('whitegrid'):

  mpg_grapho = seaborn.histplot(data=mpg_ds, x='weight', hue=len(mpg_ds['name']), palette='dark', kde=True)

  mpg_grapho.set(title='Distribuição contínua de peso dos carros em seus diversos tipos', xlabel='Peso', ylabel='Carros')

# por anos 

import seaborn

mpg_ds = seaborn.load_dataset('mpg')

with seaborn.axes_style('whitegrid'):

  mpg_grapho = seaborn.histplot(data=mpg_ds, x='weight', hue=mpg_ds['model_year'])

  mpg_grapho.set(title='Distribuição contínua de peso dos carros ao longo dos anos', xlabel='Peso', ylabel='Anos')


