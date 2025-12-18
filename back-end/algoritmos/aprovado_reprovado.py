while True:
    try:
        nota = float(input('Nota: '))
        if nota > 6:
            print('Aprovado')
            break
        elif nota < 7 and nota > 4:
            print('Recuperação')
            break
        else:
            print('Reprovado')
            break
    except ValueError:
        print('Digite um valor valido.')