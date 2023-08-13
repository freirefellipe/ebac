# acessar os documentos com bs4 e limpá-los:

 # estados: acesso
 
from bs4 import BeautifulSoup

estados_bruto = BeautifulSoup(open('estados-bruto.xml', mode='r'), 'xml')

 # estados: seleção e limpeza

header = ['ID', 'NOME', 'IDCAPITAL', 'SIGLA', 'REGIAO']

id_tag = estados_bruto.find_all(header[0])
id_ = list(map(lambda i : i.get_text(), id_tag))

nome_tag= estados_bruto.find_all(header[1])
nome = list(map(lambda i: i.get_text(), nome_tag))

idcapital_tag = estados_bruto.find_all(header[2])
idcapital = list(map(lambda i : i.get_text(), idcapital_tag))

sigla_tag = estados_bruto.find_all(header[3])
sigla = list(map(lambda i : i.get_text(), sigla_tag))

regiao_tag = estados_bruto.find_all(header[4])
regiao = list(map(lambda i : i.get_text(), regiao_tag))          

 # estado: documentos .csv com divisórias em ; com os dados desejados

import csv

with open (file='estados-limpo.csv', mode='w', encoding='utf8') as estados:
    estados_csv = csv.writer(estados, delimiter=';')
    estados_csv.writerows([[header[1], header[3], header[4]]])
    for x in range (0, len(id_)):
            estados_csv.writerows([[nome[x], sigla[x], regiao[x]]])


 # criar uma visualização dos dados com o pacote Pandas


import pandas as pd
import unidecode

estados_df = pd.read_csv('estados-limpo.csv', sep=';')
estados_df.columns = ['estado', 'sigla', 'regiao']  # renomeia os cabeçalhos

cidades_bruto_df = pd.read_csv('cidades-bruto.csv', sep=',')
cidades_2010_df = cidades_bruto_df.query('Censo == 2010')
cidades_df = cidades_2010_df[['UF', 'nome', 'Pop_est_2009', 'PIB', 'PIB_percapita']]
cidades_df.columns = ['estado', 'cidade', 'populacao', 'pib', 'pib_percapita']  # renomeia os cabeçalhos

for ogni in ['estado', 'cidade']:
    cidades_df[ogni] = list(map(lambda i : unidecode.unidecode(i), cidades_df[ogni]))

cidades_df.to_csv('cidades-limpo.csv', sep=';', encoding='utf8')

 # unir os dois Dataframes com .merge(..., how='inner')

brasil_df = pd.merge(left=estados_df, right=cidades_df, on='estado', how='inner')

brasil_df.to_csv('brasil.csv', sep=';', encoding='utf8')


# ANALISE DE DADOS

Dicio_Brasil = dict(
	# 10 cidades mais populosas
	dez_cid_pop = brasil_df[['cidade', 'populacao']].sort_values(by=['populacao'], ascending=False).head(n=10), 

	# 5 cidades com menor PIB per capita no NE  
	cid_pibpc_ne = brasil_df[['regiao', 'estado', 'cidade', 'pib_percapita']].query('regiao == "NORDESTE"').sort_values(by='pib_percapita', ascending=False).head(n=5),

	# 15 cidades com maior PIB em SP
	cid_pib_sp = brasil_df[['estado', 'cidade', 'pib']].query('estado == "SAO PAULO"').sort_values(by='pib', ascending=False).head(n=15),

	# PIB de SC
	sc_pib = brasil_df.query('estado == "SANTA CATARINA"').agg('sum').loc['pib'],

	# População da região sul
	sul_pop = brasil_df.query('regiao == "SUL"').agg('sum').loc['populacao'],

	# PIB per capita médio das cidades de MS
	ms_percapita_medio = brasil_df.query('estado == "MATO GROSSO DO SUL"').describe().T.loc['pib_percapita'].loc['mean'],

	# População do Brasil
	br_pop = brasil_df.agg('sum').loc['populacao']
)

# VISUALISAÇÃO

import matplotlib.pyplot as plt

# 10 cidades menos populosas so Brasil
dez_cid_menos_pop = brasil_df[['cidade','populacao']].sort_values(by='populacao', ascending=True).head(n=10).plot.bar(x='cidade', y='populacao')
dez_cid_menos_pop.get_figure().savefig('dez_cid_menos_pop.png')

# proporção da população do Brasil por região
brasil_pop_regiao = pd.DataFrame({
					'populacao':[ # crio um DF que vai conter somente a coluna populacao e seu index
							brasil_df.query('regiao == "NORTE"').agg('sum').loc['populacao'], 
							brasil_df.query('regiao == "NORDESTE"').agg('sum').loc['populacao'], 
							brasil_df.query('regiao == "CENTRO-OESTE"').agg('sum').loc['populacao'], 
							brasil_df.query('regiao == "SUDESTE"').agg('sum').loc['populacao'], 
							brasil_df.query('regiao == "SUL"').agg('sum').loc['populacao']
				]
			}, 
			index= ['NORTE', 'NORDESTE', 'CENTRO-OESTE', 'SUDESTE', 'SUL'] # altera os números que ordenam as linhas, nesse caso para nomes escolhidos, para que cada fatia do gráfico possa ter um nome
			)

brasil_pop_regiao_pie = brasil_pop_regiao.plot.pie(y='populacao', figsize=(14, 9))
brasil_pop_regiao_pie.get_figure().savefig('pop.png')

print(brasil_pop_regiao)

