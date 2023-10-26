"""

    Working with dictionaries

"""
import pprint

# Creating a dict
country = {'name': 'Brazil', 'population': 204000000}

print(f'Our initial dictionary: {country}')

print('\nUsing get() to accessing a dict (safely):')
print(country.get('name'))                  # returns Brazil
print(country.get('capital', 'N/A'))        # returns N/A


print('\nHandling dict access when using [] notation: ')
try:
    capital = country['capital']            # generates a KeyError
except KeyError:
    capital = '(unknown)'
print(capital)


print('\nAdding entries to a dict:')
country['capital'] = 'Brasilia'
print(country)


print('\nIterating a dict (gives keys back):')
for key in country:
    print(f'{key}: {country[key]}')


print('\nGetting just the values back from a dict:')
for value in country.values():
    print(value, end=' ')


print('\nGet both key and value back at the same time: ')
for key, val in country.items():
    print(f'Key: {key}, Value: {val}')
print()


countries = {
    'Brazil': {'population': 204000000, 'capital': 'Brasilia'},
    'Argentina': {'population': 43100000, 'capital': 'Buenos Aires'},
    'Venezuela': {'population': 30600000, 'capital': 'Caracas'}
}
print(f'Working with a dict of dicts:')
pprint.pprint(countries)

for key, val in countries.items():
    print(f'Country: {key}')
    for k, v in val.items():
        print(f'\t{k}: {v}')

print('\nExtract values from a dict of dicts using a comprehension:: ')
countries_sorted = [(country_name, country.get('capital', 'N/A')) for country_name, country in sorted(countries.items())]
print(countries_sorted)


# --------------------------------------------------------------
print('\nUsing a defaultdict:')
from collections import defaultdict
dict1 = defaultdict(float)
dict1['greet1'] = 'hello'
print(dict1['greet1'], dict1['greet2'])
print(dict1)
