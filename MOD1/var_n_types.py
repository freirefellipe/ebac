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

print(f'A = {a}')
print(f'B = {b}')
print(f'C = {c}')

###

notizia = 'Selic vai a 2.75% e supera expectativas; é a primeira alta em 6 anos.'

selic_trova = notizia.find('%')

selic = float(notizia[selic_trova - 4 : selic_trova])

anni_trova = notizia.find('anos')

anni = notizia[anni_trova - 3 : anni_trova]

print(f'Selic al momento è {selic}%.')
print(f'Il periodo è di {anni} anni.')


