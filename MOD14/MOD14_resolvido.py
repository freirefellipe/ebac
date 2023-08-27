import seaborn


diamonds_ds = seaborn.load_dataset('diamonds')

diamonds_cut_price_ds = diamonds_ds[['cut', 'price']].groupby('cut').agg('sum')

diamonds_graphic = seaborn.relplot(data=diamonds_cut_price_ds, x='cut', y='price', hue='price')

diamonds_graphic.savefig('dimaonds.png')

#

flights_ds = seaborn.load_dataset('flights')

flights_dec_ds = flights_ds.query('month == "Dec"')

with seaborn.axes_style('whitegrid'):
  
  flights_dec_graphic = seaborn.barplot(data=flights_dec_ds, x='year', y='passengers', color='steelblue')

  flights_dec_graphic.set(title='Passageiros em dezembro ao longo dos anos', xlabel='Ano', ylabel='Passageiros')

  flights_dec_graphic.get_legend()
  
flights_dec_graphic.get_figure().savefig('flights_dec.png')

#

flights_ds = seaborn.load_dataset('flights')

flights10years = flights_ds.query('1949 <= year <= 1959')

with seaborn.axes_style('whitegrid'):

  flights10years_graph = seaborn.lineplot(data=flights10years, x='year', y='passengers', hue='month')

flights10years_graph.get_figure.savefig('flights10years.png')

#

print('-Fim do Script-')
