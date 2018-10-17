import random
randA = random.sample(range(1, 40), random.randint(10, 20))
randB = random.sample(range(1, 40), random.randint(10, 20))
print('randA = ', randA)
print('randB = ', randB)
res = [i for i in randA if i in randB]
print(set(res))
# or
print(set(randA) & set(randB))
