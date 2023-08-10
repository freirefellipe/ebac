print('''
| Dia   | Valor Total Vendas | Qtd Total Vendas | Ticket Medio |
|-------|--------------------|------------------|--------------|
| 19/01 | (A)                | 3                | 320.52       |
| 20/01 | 834.47             | (B)              | 119.21       |
| 23/01 | 15378.12           | 5                | (C)          |
''')


a = round(float(3*320.52), 2)
b = round(float(834.47/119.21), 2)
c = round(float(15378.12/5), 2)

print(f'A = 3*320.52 = {a}')
print(f'B = 834.47/119.21 = {b}')
print(f'C = 15378.12/5 = {c}')

###

notizia = 'Selic vai a 2.75% e supera expectativas; é a primeira alta em 6 anos.'

selic_trova = notizia.find('%')

selic = float(notizia[selic_trova - 4 : selic_trova])

anni_trova = notizia.find('anos')

anni = notizia[anni_trova - 3 : anni_trova]

print(f'Selic al momento è di {selic}%.')
print(f'Il periodo è di {anni} anni.')

###

print('Corrigindo inserção de palavras em banco de dados.')

nome_inserito = str(input('Insira seu nome completo. >')).upper()

nome_separato = nome_inserito.split()
nome_separato = list(map(lambda i : i.capitalize(), nome_separato))

dicio_user = {}
		
dicio_user['primo_nome'] = nome_separato[0].strip()
dicio_user['secondo_nome'] = nome_separato[1].strip()
dicio_user['terzo_nome'] = nome_separato[2].strip()

print(nome_inserito)
print(nome_separato)
print(dicio_user)
print('Seja bem vindo,', dicio_user['primo_nome'], '.')

