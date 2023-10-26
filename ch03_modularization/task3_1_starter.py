"""
      task3_1_starter.py   -   Modularization

      This file represents the driver for our city_search.py module.

      It reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

"""
from pathlib import Path

import ch03_modularization.city_search as cs

working_dir = '../resources'
data_file = 'cities15000.txt'
fullname = Path(working_dir) / data_file

cs.read_data(fullname)

print(cs.largest().name)
print(cs.highest().name, '\n')

results = cs.search('colorado')

if not results:
    print('No cities found.')
else:
    col_header = [h[0].capitalize() for h in cs.header]
    print('{0:<35}{1:>15}{2:>15}{3:>10}'.format(*col_header))
    print('{0:-<75}'.format(''))
    for city in results:
        # print('{0:<35}{1:>15,}{2:>15,}{3:>10}'.format(*city))
        # print(f'{city.name:<35}{city.population:>15,}{city.elevation:>15,}{city.country:>10}')

        name, population, elevation, country = city
        print(f'{name:<35}{population:>15,}{elevation:>15,}{country:>10}')

    print('{0:-<75}'.format(''))

    tot_pop = sum([r.population for r in results])
    print('{0:>35}{1:>15,}'.format('Total:', tot_pop))
