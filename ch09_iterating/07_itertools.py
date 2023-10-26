from itertools import chain, islice, count
from pathlib import Path


# chain example
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = (7, 8, 9)
dict4 = {'key1': 10, 'key2': 11}
chained_list = chain(list1, list2, list3, dict4.values())       # chained list is an iterator, not a new list
print(tuple(chained_list))                       # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# islice example
with Path('../resources/cities15000_info.txt').open(encoding='utf-8') as f:
    for line in islice(f, 7, None):
        print(line.strip().split(':')[0].strip())


# count(start, step)    is an iterator with no upper bound
# unlike range which requires an upper bound
iterable = count(start=10, step=10)
while (val := next(iterable)) <= 100:
    print(val)
