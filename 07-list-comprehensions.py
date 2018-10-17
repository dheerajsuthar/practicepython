import random
ll = random.sample(range(1, 100), 20)
print('input: ', ll)
op = [i for i in ll if i % 2 == 0]
print('result: ', op)
