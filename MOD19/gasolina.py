import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df.columns = ['Dia', 'Preço']

gasolina_grafico_linha = sns.lineplot(x='Dia', y='Preço', data=gasolina_df)

gasolina_grafico_linha.get_figure().savefig('gasolina.png')

print('Gráfico gerado com sucesso')
