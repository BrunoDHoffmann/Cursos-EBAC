continuar = 1

while continuar == 1:
    try:
        print("""
        MENU:
        1 - SOMA
        2 - SUBTRAÇÃO
        3 - MULTIPLICAÇÃO
        4 - DIVISÃO
        Digite um numero entre 1 e 4
        """)
        opt = int(input('Digite o numero da opção escolhida: '))
        if opt < 1 or opt > 4:
            print('Opção inválida! Tente digitar um numero entre 1 e 4.')
        else:
            num1 = float(input('Digite o primeiro numero: '))
            num2 = float(input('Digite o segundo numero: '))
            match opt:
                case 1:
                    print(f'Resultado: {num1 + num2}')
                case 2:
                    print(f'Resultado: {num1 - num2}')
                case 3:
                    print(f'Resultado: {num1 * num2}')
                case 4:
                    if not num2:
                        print('Zero')
                    else: 
                        print(f'Resultado: {num1 / num2}')
            continuar = int(input("""
            1 - Continuar
            2 - Sair
            """))
            if continuar == 2:
                print('Até a proxima!')
                break
    except:
        print('Por favor, digite valores validos.')