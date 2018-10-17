import random
a = random.sample(range(1, 40), random.randint(12, 16))
b = random.sample(range(1, 40), random.randint(12, 16))
print('a: ', a)
print('b: ', b)
# random.sample gets unique elment so no need to worry about duplicates
print([i for i in a if i in b])
# still
print(list(set(a) & set(b)))

