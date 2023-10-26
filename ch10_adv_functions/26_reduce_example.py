"""
    26_reduce_example.py
    Using reduce()
"""
import functools


def sentence_maker(word1, word2):
    return ' '.join([word1, word2])

results = functools.reduce(sentence_maker, ['Four', 'score', 'and', 'seven', 'years', 'ago'])
print(results)

def num_func(total, amt):
    return total + amt

results = functools.reduce(num_func, [1, 2, 3, 4, 5, 6])
print(results)