
import pandas
import seaborn

gasolina_pd = pandas.read_csv('gasolina.csv', sep=',')

print(gasolina_pd, '\n')

gasolina_media = gasolina_pd['venda'].describe().loc['mean'].T

print(f'A média de preço da gasolina é de R${gasolina_media}.', '\n')

gasolina_grafico_linha = seaborn.lineplot(x='dia', y='venda', data=gasolina_pd)
gasolina_grafico_linha.set_xlabel('Dia', fontsize='10', fontweight='bold')
gasolina_grafico_linha.set_ylabel('Preço', fontsize='10', fontweight='bold')

gasolina_grafico_linha.get_figure().savefig('gasolina.png')

print(f'O gráfico foi gerado com sucesso.')

## Os códigos abaixo são comandos para o terminal do Linux:

# $ git add gasolina.png gasolina.py
# $ git commit -m 'Here goes...'
# $ git push origin main

# Link para o GitHub é: https://github.com/freirefellipe/analytics.git

