def a_generator(min_val, max_val):
    current_val = min_val
    while current_val <= max_val:
        yield current_val
        current_val += 1


gen = a_generator(3, 5)
print(type(gen))

# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
try:
    print(gen.__next__())
except StopIteration as err:
    pass

print(next(gen))
print(next(gen))
# print(next(gen))
# print(next(gen))

print('\nHere is the for loop:')
for val in gen:
    print(val)
