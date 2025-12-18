x = int(input('Numero: '))
x = str(x)
if x == x[::-1]:
    print('palindromo')
else:
    print('nao')