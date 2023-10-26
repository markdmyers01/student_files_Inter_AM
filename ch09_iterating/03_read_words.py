import sys

def read_words(filename='data.txt'):
    total_words = []
    try:
        with open(filename, encoding='utf8') as f:
            for line in f:
                line_words = line.strip().split()
                total_words.extend(line_words)
    except IOError as err:
        print(err, file=sys.stderr)

    return total_words

print(read_words())
for word in read_words():
    print(word)

print('Generator version....')
# ---------------------------------------------------------------
# Generator version of the above code


def read_words_generator(filename='data.txt'):
    try:
        with open(filename, encoding='utf8') as f:
            for line in f:
                line_words = line.strip().split()
                for one_word in line_words:
                    yield one_word
    except IOError as err:
        print(err, file=sys.stderr)

for word in read_words_generator():
    print(word)

item1 = [1, 2, 3]
item2 = [4, 5, 6]
item3 = item1 + item2
print(item3)
item4 = (7, 8, 9)
# item3.append(item4)
item3.extend(item4)
print(item3)
