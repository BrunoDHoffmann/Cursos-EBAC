# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(nome):
    if nome in tarefas:
        return "Essa tarefa já existe."
    else:
        tarefas[nome] = False
        return f"Tarefa '{nome}' adicionada com sucesso!!"

def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    else:
        resultado = []
        for nome, valor in sorted(tarefas.items(), key=lambda item: item[0]):
            status = "✅ Concluída" if valor else "❌ Não concluída"
            resultado.append(f'{nome}: {status}')
        return print(resultado)

def remover_tarefa(nome):
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso!"
    else:
        return "Erro: Tarefa não encontrada."

def marcar_concluida(nome):
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada como concluída!"
    else:
        return "Erro: Tarefa não encontrada."

def exibir_menu():
    return (print(
        """Menu:  
        1 - Adicionar tarefa  
        2 - Listar tarefas  
        3 - Remover tarefa  
        4 - Marcar tarefa como concluída  
        5 - Sair  """
    ))

def main():
    while True:
        exibir_menu()
        opcao = int(input("Opção: ").strip())

        if opcao == 1:
            nome = input('Digite o nome da tarefa: ')
            adicionar_tarefa(nome)
        elif opcao == 2:
            listar_tarefas(tarefas)
        elif opcao == 3:
            nome = input('Digite o nome da tarefa: ')
            remover_tarefa(nome)
        elif opcao == 4:
            nome = input('Digite o nome da tarefa: ')
            marcar_concluida(nome)
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()