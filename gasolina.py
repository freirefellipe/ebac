
import pandas

nome_grafico = str(input('Qual vai ser o nome e o formato do gráfico a ser criado? > '))

gasolina_pd = pandas.read_csv('gasolina.csv', sep=',')

print(gasolina_pd, '\n')

gasolina_media = gasolina_pd['venda'].describe().loc['mean'].T

print(f'A média de preço da gasolina é de R${gasolina_media}.', '\n')

import seaborn

gasolina_grafico_linha = seaborn.lineplot(x='dia', y='venda', data=gasolina_pd)

gasolina_grafico_linha.set_xlabel('Dia', fontsize='10', fontweight='bold')
gasolina_grafico_linha.set_ylabel('Preço', fontsize='10', fontweight='bold')

gasolina_grafico_linha.get_figure().savefig(nome_grafico)

print(f'O gráfico {nome_grafico} foi gerado com sucesso.')
