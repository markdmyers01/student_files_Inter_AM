"""
    Several examples of different ways to invoke functions
"""
from pathlib import Path


def check_files(path='..', filename=''):
    p = Path(path)
    results = p / filename
    return results.exists()


def check_all_files(path='..', *files):
    p = Path(path)
    results = all([(p / x).exists() for x in files if isinstance(x, str)])
    return results


def check_all_files_extra(path='..', *args, **kwargs):
    print(args)
    print(kwargs)
    p = Path(path)
    results = [(p / x).exists() for x in args]
    if kwargs.get('individual'):
        return results
    return all(results)


def check_files_positional(path='..', /, filename=''):
    p = Path(path)
    results = p / filename
    return results.exists()


print(check_files('../ch02_basics', '01_strings.py'))
print(check_files())
print(check_files(filename='01_strings.py', path='../ch02_basics'))

print(check_all_files('../ch02_basics', '01_strings.py', '03_lists.py'))
print(check_all_files('../ch02_basics', '01_strings.py', '03_lists.py', '04_not_there.py', 10, [1, 2, 3]))

print(check_all_files_extra('../ch02_basics', '01_strings.py', '03_lists.py'))
print(check_all_files_extra('../ch02_basics', '01_strings.py', '03_lists.py', '04_not_there.py', individual=True))
print(check_all_files_extra('../ch02_basics', '01_strings.py', '03_lists.py', '04_not_there.py', samp1='test1', samp2=100, individual=False))

print(check_files_positional('../ch02_basics', '01_strings.py'))
# print(check_files_positional(path='../ch02_basics', filename='01_strings.py'))
