num = int(input('Enter the number: '))
res = [i for i in range(2, num) if num % i == 0]
print(res)
