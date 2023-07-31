# SCRAPING

import json

with open('deliveries.json', mode='r', encoding='utf8') as deliveries_json:
    
    deliveries = json.load(deliveries_json)

a = len(deliveries)

b = deliveries[0]

c = b.keys()

d = b['origin']['lat']

# WRANGLING

import pandas

deliveries_df = pandas.DataFrame(deliveries)

origin_deliveries_df = pandas.json_normalize(deliveries_df['origin']) # transforma os dados de origin em 2 colunas, operação chamada Flatten.

# agora inclui essas duas novas colunas no dataframe

deliveries_df = pandas.merge(left=deliveries_df, right=origin_deliveries_df, how='inner', left_index=True, right_index=True)

deliveries_df = deliveries_df.drop('origin', axis=1) # drop vai excluir a coluna antiga e desorganizada.

deliveries_df = deliveries_df[['name', 'region', 'lng', 'lat', 'vehicle_capacity', 'deliveries']]

deliveries_df.rename(columns={'lng':'hub_lng', 'lat':'hub_lat'}, inplace=True) # faz a mudança em forma de dicionário

deliveries_deliveries = deliveries_df[['deliveries']].explode('deliveries') 

# em uma célula só havia N valores com chave 'id' em formato de dicionários dentro de uma lista. Com o método 'explode' esses N viraram uma só coluna, e com muito mais linhas que o dataframe anterior. A ideia agora é inverter, e fazer com que esse novo dataframe resultado da explosão se torne o principal, tendo o dataframe anterior que se adequar em tamanho ao novo.

deliveries_normalized_df = pandas.concat([
				
    pandas.DataFrame(deliveries_deliveries['deliveries'].apply(lambda i : i['size'])).rename(columns={'deliveries':'delivery_size'}),
    pandas.DataFrame(deliveries_deliveries['deliveries'].apply(lambda i : i['point']['lng'])).rename(columns={'deliveries':'delivery_lng'}),
    pandas.DataFrame(deliveries_deliveries['deliveries'].apply(lambda i : i['point']['lat'])).rename(columns={'deliveries':'delivery_lat'}),
], axis=1)


deliveries_df = deliveries_df.drop('deliveries', axis=1)

deliveries_df = pandas.merge(left=deliveries_df, right=deliveries_normalized_df, how='right', left_index=True, right_index=True) # "how='right'" vai incluir a tabela menor (da esquerda) na maior (direita)


# tudo que foi feito anteriormente foi para criar um Dataframe adequado análise de dados de cada entrega.

# ESTRUTURA

e = deliveries_df.shape

f = deliveries_df.columns

g = deliveries_df.index

# SCHEMA (descrição da coluna com tipo e outras coisas)

h = deliveries_df.info() # não esquecer esse método, que é muito importante (string em Pandas se chama Object)

 # categóricos

i = deliveries_df.select_dtypes('object').describe().transpose()

 # numéricos

j = deliveries_df.drop(['name', 'region'], axis=1).select_dtypes('int64').describe().transpose()

# DADOS FALTANTES

k = deliveries_df.isna().any() # any é para resumir a informação da coluna (série) inteira



# print()


