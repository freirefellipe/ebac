from bs4 import BeautifulSoup


fortune_html = BeautifulSoup(open('fortune.html', mode='r'), 'html.parser')

ranking_tagged = fortune_html.find_all('div', class_='rt-tr-group')

ranking = []

for line in ranking_tagged:
    data = line.find_all('span')
    data_clean = list(map(lambda datum : datum.get_text(), data))
    ranking.append(data_clean)


import csv

header = [
  'rank', 
  'name', 
  'revenues', 
  'revenues-percent-change', 
  'profits', 
  'profits-percent-change', 
  'assets', 
  'market-value',
  'employees'
]

### Caso queira fazer um dicionário com os dados em vez de escrever documento csv.
ranking_list = []

#count = 0
#for num in range(0, 9, 1):
#    dicio_ranking[header[num]] = [ranking[0][num], ranking[1][num], ranking[2][num], ranking[3][num]]

for i in range(0, len(ranking), 1):
    dicio_ranking = {}
    dicio_ranking[header[0]] = ranking[i][0]
    dicio_ranking[header[1]] = ranking[i][1]
    dicio_ranking[header[2]] = ranking[i][2]    
    dicio_ranking[header[3]] = ranking[i][3]
    dicio_ranking[header[4]] = ranking[i][4]
    dicio_ranking[header[5]] = ranking[i][5]
    dicio_ranking[header[6]] = ranking[i][6]
    dicio_ranking[header[7]] = ranking[i][7]
    dicio_ranking[header[8]] = ranking[i][8]
    ranking_list.append(dicio_ranking)


print(ranking_list)


import pandas

ranking_list_df = pandas.DataFrame.from_dict(ranking_list, orient='columns', dtype=None)
print(ranking_list_df)

###


with open(file='fortune_ranking.csv', mode='w', encoding='utf8') as fortune_ranking:
    fortune_ranking_csv = csv.writer(fortune_ranking, delimiter=';')
    fortune_ranking_csv.writerows([[header[0], header[1], header[2], header[3], header[4], header[5], header[6], header[7], header[8]]])
    fortune_ranking_csv.writerows(map(lambda datum : [
        datum[0],
        datum[1],
        datum[2],
        datum[3],
        datum[4],
        datum[5],
        datum[6],
        datum[7],
        datum[8]
        ], ranking)
        )

print('Documento csv criado.')


import pandas as pd

fortune_ranking_df = pd.read_csv('fortune_ranking.csv', sep=';')

print(fortune_ranking_df)

    # escolher somente as colunas (séries) que têm caracteres a serem removidos.

for series in ['revenues', 'revenues-percent-change', 'profits','assets', 'profits-percent-change', 'market-value', 'employees']:

    fortune_ranking_df[series] = fortune_ranking_df[series].apply(lambda value : value.replace('$', ''))
    fortune_ranking_df[series] = fortune_ranking_df[series].apply(lambda value : value.replace('%', ''))

# fortune_ranking_df[series] = fortune_ranking_df[series].apply(lambda value : ''.join(list(filter(str.isnumeric, value)))) # pegaria somente os números da célula.

print(fortune_ranking_df)


fortune_ranking_df.to_csv('fortune-limpo.csv', sep=';', encoding='utf8', index=False) # lembrar do encoding para não ter problema com caracteres especiais

