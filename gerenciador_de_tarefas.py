import json
import os

def carregar_tarefa():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json','r') as arquivo:
            return json.load(arquivo)
    else:
        return []
    
def salvar_tarefa(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=2)

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descricao da tarefa: ")
    tarefa = {"descricao": descricao, "completa": False}
    tarefas.append(tarefa)
    salvar_tarefa(tarefas)
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefa(tarefas):
    print(tarefas)

def principal():

    tarefas = carregar_tarefa()

    while True:
        print("\n===== Gerenciador de Tarefas =====")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("0. Sair")

        menu = input("Digite o número da opção desejada: ")

        if menu == "1":
            adicionar_tarefa(tarefas)
        if menu == "2":
            visualizar_tarefa(tarefas)
        elif menu == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    principal()