def adicionar_tarefa(tarefas):
    descricao = input("Digite a descricao da tareda: ")
    tarefa = {"descricao": descricao, "completa": False}
    tarefas.append(tarefa)
    print(tarefas)

def principal():

    tarefas = []

    while True:
        print("\n===== Gerenciador de Tarefas =====")
        print("1. Adicionar Tarefa")
        print("0. Sair")

        menu = input("Digite o número da opção desejada: ")

        if menu == "1":
            adicionar_tarefa(tarefas)
        elif menu == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

principal()