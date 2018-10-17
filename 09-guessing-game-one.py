import random
cont = 'y'

while cont == 'y':
    num = random.randint(1, 9)
    count = 0
    while True:
        inp = int(input('your guess: '))
        count = count + 1
        if(inp == num):
            print('right guess! you tried ', count, ' times.')
            cont = input('Continue (press y)? ')
            break
        elif inp < num:
            print('too low')
        else:
            print('too high')
