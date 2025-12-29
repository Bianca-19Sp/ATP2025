#TPC6 APLICAÇÃO PARA GESTÃO DE ALUNOS

# Definição da estrutura de dados
# aluno = (nome, id, [notaTPC, notaProj, notaTeste]) - tuplo
# turma = lista de alunos

# Funções para as operações
def criar_turma():
    print("Nova turma criada.")
    return []

def inserir_aluno(turma):
    nome = input("Digite o nome do aluno: ")
    id = int(input("Digite o ID do aluno: "))
    
    # Verificar se o ID já existe
    while any(a[1] == id for a in turma):
        print("Este ID já está associado a outro aluno.")
        id = int(input("Digite um novo ID para o aluno: "))

    # Inserir notas com validação
    notaTPC = float(input("Digite a nota do TPC (0-20): "))
    while notaTPC < 0 or notaTPC > 20:
        notaTPC = float(input("Nota inválida. Digite a nota do TPC (0-20): "))

    notaProj = float(input("Digite a nota do Projeto (0-20): "))
    while notaProj < 0 or notaProj > 20:
        notaProj = float(input("Nota inválida. Digite a nota do Projeto (0-20): "))

    notaTeste = float(input("Digite a nota do Teste (0-20): "))
    while notaTeste < 0 or notaTeste > 20:
        notaTeste = float(input("Nota inválida. Digite a nota do Teste (0-20): "))

    aluno = (nome, id, [notaTPC, notaProj, notaTeste])
    turma.append(aluno)
    print("Aluno adicionado com sucesso.")

def listar_turma(turma):
    if not turma:
        print("A turma está vazia.")
    else:
        print("Listagem de alunos:")
        for aluno in turma:
            print(aluno)

def consultar_aluno(turma):
    id = int(input("Digite o ID do aluno que deseja consultar: "))
    aluno_encontrado = next((a for a in turma if a[1] == id), None)
    
    if aluno_encontrado:
        print("Aluno encontrado:", aluno_encontrado)
    else:
        print(f"Não foi encontrado nenhum aluno com o ID {id}.")

def guardar_turma(turma, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for aluno in turma:
            arquivo.write(f"{aluno[0]},{aluno[1]},{aluno[2][0]},{aluno[2][1]},{aluno[2][2]}\n")
    print(f"Turma salva no arquivo {nome_arquivo}.")

def carregar_turma(nome_arquivo):
    turma = []
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                if len(dados) == 5:
                    nome, id, notaTPC, notaProj, notaTeste = dados
                    turma.append((nome, int(id), [float(notaTPC), float(notaProj), float(notaTeste)]))
        print(f"Turma carregada do arquivo {nome_arquivo}.")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except ValueError:
        print("Erro ao processar o conteúdo do arquivo.")
    return turma

# Menu da aplicação
def mostrar_menu():
    print("""
    Menu de Opções:
    1 - Criar Turma
    2 - Inserir Aluno
    3 - Listar Turma
    4 - Consultar Aluno por ID
    5 - Guardar Turma em Arquivo
    6 - Carregar Turma de Arquivo
    0 - Sair
    """)

# Aplicação
def main():
    turma = []
    while True:
        mostrar_menu()
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            turma = criar_turma()
        elif opcao == 2:
            inserir_aluno(turma)
        elif opcao == 3:
            listar_turma(turma)
        elif opcao == 4:
            consultar_aluno(turma)
        elif opcao == 5:
            guardar_turma(turma, "turma.txt")
        elif opcao == 6:
            turma = carregar_turma("turma.txt")
        elif opcao == 0:
            print("Obrigada! Volte sempre.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar a aplicação
main()
