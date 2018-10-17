cont = 'y'
while cont == 'y':
    print('Rock: r Scissors: s Paper: p')
    right_inputs = ['r', 's', 'p']
    a = b = ''
    while a not in right_inputs:
        a = input('Player A: ')

    while b not in right_inputs:
        b = input('Player B: ')

    if a == b:
        print('Draw')
    elif right_inputs.index(b) == (right_inputs.index(a)+1) % 3:
        print('A wins')
    else:
        print('B wins')
    cont = input('Continue? (y to continue)')
