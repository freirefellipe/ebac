## 

elenco_film = []

elenco_film.append('Um Sonho de Liberdade')
elenco_film.append('O Poderoso Chefão')
elenco_film.append('Batman: O Cavaleiro das Trevas')
elenco_film.append('O Poderoso Chefão II')
elenco_film.append('12 Homens e uma Sentença')
elenco_film.append('A Lista de Schindler')
elenco_film.append('O Senhor dos Anéis')
elenco_film.append('Pulp Fiction - Tempo de Violência')
elenco_film.append('O Senhor dos Anéis: A Sociedade do Anel')
elenco_film.append('Três Homens em Conflito')

ranking_10 = f'''
Top 10 Best Movies:

1. {elenco_film[0]}
2. {elenco_film[1]}
3. {elenco_film[2]}
4. {elenco_film[3]}
5. {elenco_film[4]}
6. {elenco_film[5]}
7. {elenco_film[6]}
8. {elenco_film[7]}
9. {elenco_film[8]}
10. {elenco_film[9]}
'''

print(ranking_10)

# Simulando remoção de elementos duplicados:

elenco_film.insert(0, 'Meu filme é massa')
elenco_film[1] = 'Meu filme é massa'

set_film = set(elenco_film)
elenco_film = list(set_film)

print(elenco_film)
print(type(elenco_film))

# Lista com dicionários como elementos:

elenco_film_detailed = [
		{'titulo':'Um Sonho de Liberdade', 'ano':'1994', 'idade':'16', 'nota': '9.3'}, 
		{'titulo':'O Poderoso Chefão', 'ano':'1972', 'idade':'14', 'nota':'9.2'},
		{'titulo':'Batman: O Cavaleiro das Trevas', 'ano':'2008', 'idade':'12', 'nota':'9.0'}, 
		{'titulo':'O Poderoso Chefão II', 'ano':'1974', 'idade':'14', 'nota':'9.0'},
		{'titulo':'12 Homens e uma Sentença', 'ano':'1957', 'idade':'livre', 'nota':'9.0'},
		{'titulo':'A Lista de Schindler', 'ano':'1993', 'idade':'14', 'nota':'9.0'},
		{'titulo':'O Senhor dos Anéis: O Retorno do Rei', 'ano':'2003', 'idade':'14', 'nota':'9.0'},
		{'titulo':'Pulp Fiction - Tempo de Violência', 'ano':'1994', 'idade':'18', 'nota':'8.9'},
		{'titulo':'O Senhor dos Anéis: A Sociedade do Anel', 'ano':'2001', 'idade':'12', 'nota':'8.8'},
		{'titulo':'Três Homens em Conflito', 'ano':'1966', 'idade':'14', 'nota':'8.8'},
	] # https://www.imdb.com/chart/top/



elenco_film_detailed.insert(0, {'titulo':'Meu Filme', 'ano':'1985', 'idade':'livre', 'nota':'10'}) # Alternativa 1, insere 'deslizando' os outros elementos;

elenco_film_detailed.pop() if len(elenco_film_detailed) > 9 else ''


elenco_film_detailed[9] = {'titulo':'Três Homens em Conflito', 'ano':'1966', 'idade':'14', 'nota':'8.8'} # Alternativa 2, substitui um dado por outro no elemento alvo

print(elenco_film_detailed)





