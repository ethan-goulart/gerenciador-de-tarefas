import json
import os


# Função para carregar as tarefas do arquivo JSON
def carregar_tarefa():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json','r') as arquivo:
            return json.load(arquivo)
    else:
        return []

# Função para salvar as tarefas em um arquivo JSON
def salvar_tarefa(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=2)

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descricao da tarefa: ")
    tarefa = {"descricao": descricao, "completa": False}
    tarefas.append(tarefa)
    salvar_tarefa(tarefas)
    print("Tarefa adicionada com sucesso!\n")

def visualizar_tarefa(tarefas):
    if tarefas:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            status = "✔" if tarefa["completa"] else "❌"
            print(f"{i + 1}. [{status}] {tarefa['descricao']}")
    else:
        print("Não há tarefas.\n")

def completar_tarefa(tarefas):
    visualizar_tarefa(tarefas)
    aux = int(input("Digite o numero da tarefa que deseja marcar como completa: "))
    tarefas[aux - 1]["completa"] = True
    salvar_tarefa(tarefas)
    print("Tarefa completada!\n")

def editar_tarefa(tarefas):
    visualizar_tarefa(tarefas)
    aux = int(input("Digite o numero da tarefa que deseja editar: "))
    new_descricao = input("Digite a nova descricao da tarefa: ")
    tarefas[aux - 1]["descricao"] = new_descricao
    salvar_tarefa(tarefas)
    print("Tarefa Editada!\n")

def excluir_tarefa(tarefas):
    visualizar_tarefa(tarefas)
    aux = int(input("Digite o numero da tarefa a ser Excluida: "))
    excluir_tarefa = tarefas.pop(aux - 1)
    salvar_tarefa(tarefas)
    print(f"Tarefa '{excluir_tarefa['descricao']}' excluída! \n")

def principal():

    tarefas = carregar_tarefa()

    while True:
        print("\n===== Gerenciador de Tarefas =====")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Completar Tarefas")
        print("4. Editar Tarefas")
        print("5. Excluir Tarefas")
        print("0. Sair")

        menu = input("Digite o número da opção desejada: ")

        if menu == "1":
            adicionar_tarefa(tarefas)
        elif menu == "2":
            visualizar_tarefa(tarefas)
        elif menu == "3":
            completar_tarefa(tarefas)
        elif menu == "4":
            editar_tarefa(tarefas)
        elif menu == "5":
            excluir_tarefa(tarefas)
        elif menu == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    principal()