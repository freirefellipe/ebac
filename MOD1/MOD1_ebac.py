# -*- coding: utf-8 -*-
"""MOD1-ebac.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15MyH7jN0_bbDFoEupn4_d1mZfAHkNnDd

# Operações simples:

| Dia   | Valor Total Vendas | Qtd Total Vendas | Ticket Medio |
|-------|--------------------|------------------|--------------|
| 19/01 | (A)                | 3                | 320.52       |
| 20/01 | 834.47             | (B)              | 119.21       |
| 23/01 | 15378.12           | 5                | (C)          |
"""

a = round(float(320.52)*3)

print(f'320.52*3 = {a}')

b = round(float(834.47)/119.21)

print(f'834.47/119.21 = {b}')

"""# Uso do método .find() pra encontrar no texto:"""

texto = 'Selic vai a 2.75% e supera expectativas; é a primeira alta em 6 anos.'

selic_percentage = texto.find('%')

selic = texto[selic_percentage - 4 : selic_percentage]

anos = texto[texto.find('anos') - 3 : texto.find('anos')]

print(f'A taxa Selic no momento é de {selic}% no período de {anos} anos.')

"""# Uso dos métodos .upper(), .lower() - etc - em Strings para entre maiúsculas e minúsculas as palavras':"""

nome = str(input('Insira seu nome: ')).upper()

nome = str(input('Insira seu nome: ')).lower()

nome_completo_split = str(input('Insira seu nome: ')).split(' ')

primeiro_nome = list(map(lambda i:i.capitalize(), nome_completo_split))

print(primeiro_nome)

display(f'Seja bem-vindo, {primeiro_nome[0]}.')