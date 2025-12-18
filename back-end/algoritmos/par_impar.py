#Numero par ou impar
while True:
    try:
        num = int(input('Digite um numero (0 para sair): '))
        if num == 0:
            print('Operação encerrada.')
            break
        elif num % 2 == 0:
            print('par')
        else:
            print('impar')
    except ValueError:
        print('Digite um numero valido por favor.')