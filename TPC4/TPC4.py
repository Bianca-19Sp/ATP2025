#Sala de cinema

import random 

def crescente(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
    return lista



numerosalas = ["1", "2", "3", "4", "5", "6"]
Disponiveis = False



def sala():
    rand = random.randint(1, 12)
    nome = ""
    if rand < 4:
        nome = "The Grand Budapest Hotel"
    elif rand < 7:
        nome = "Pulp Fiction"
    elif rand < 10:
        nome = "Little Women"
    else:
        nome = "Pride and Prejudice"

    numerolugar = random.randint(80, 150)
    while numerolugar % 10 != 0:
        numerolugar = random.randint(80, 150)

    vendas = random.randint(1, numerolugar)
    lugares_vendidos = random.sample(range(1, numerolugar + 1), vendas)

    return [nome, numerolugar, vendas, crescente(lugares_vendidos)]

cinema = [sala() for _ in range(6)] 


def menu():
    return ("""Seja bem vindo! Escolha a opção que quer:
    (1) Visualizar salas:
    (2) Filmes em exibição:
    (3) Lugares disponíveis:
    (4) Comprar bilhete:
    (5) Criar nova sala:
    (0) Sair do programa:
    """)
    


opção = 1

while opção != 0:
    print(menu())
    try:
        opção = int(input("Escolhe uma das opções: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue


    if opção == 1:
        for i in range(len(numerosalas)):
            print(f"""A sala número {numerosalas[i]} contém as seguintes informações:
                Filme: {cinema[i][0]}
                Lugares: {cinema[i][1]}
                Disponíveis: {cinema[i][1] - cinema[i][2]}
                """)
        input("Carrega para voltares ao menu:")


    elif opção == 2:
        filmes = ["The Grand Budapest Hotel", "Pulp Fiction", "Little Women", "Pride and Prejudice"]
        for procuro in filmes:
            existe = False
            print(f"{procuro}:")
            for i in range(len(numerosalas)):
                if cinema[i][0] == procuro:
                    print(f"Sala {numerosalas[i]}")
                    existe = True
            if not existe:
                print(f"O filme {procuro} não está disponível no cinema.")
        input("Carrega para voltares ao menu:")


    elif opção == 3:
        for i in range(len(numerosalas)):
            print(f"Sala {numerosalas[i]}: {cinema[i][0], cinema[i][1], cinema[i][2]}")
        
        escolher1 = str(input("Escolhe uma sala: "))
        
        if escolher1 not in numerosalas:
            print("Escolha inválida! Tente novamente.")
        else:
            for i in range(len(numerosalas)):
                if numerosalas[i] == escolher1:
                    print(f"Lugares vendidos da Sala {escolher1}: {cinema[i][3]}")
                    Disponiveis = True
                    escolher2 = int(input(f"Escolhe um lugar de 1 a {cinema[i][1]}: "))
                    
                    if escolher2 < 1 or escolher2 > cinema[i][1]:
                        print("Lugar inválido! Tente novamente:")
                    elif escolher2 in cinema[i][3]:
                        Disponiveis = False
                        print(Disponiveis)
                    else:
                        print(Disponiveis)
                        salai = i
        input("Carrega para voltares ao menu:")


    elif opção == 4:
        if not Disponiveis:
            print("Salecione um lugar disponível na opção 3 do menu.")
        else:
            resposta = input(f"Deseja comprar o bilhete para o filme {cinema[salai][0]}, na sala {numerosalas[salai]}, no lugar {escolher2}? (s/n)")
            if resposta == 's':
                cinema[salai][3].append(escolher2)
                cinema[salai][2] += 1

                crescente(cinema[salai][3])

                print("Bilhete comprado com sucesso!")
            else:
                print("Compra cancelada.")

        input("Carrega para voltares ao menu:")


    elif opção == 5:
        novasalanum = input("Qual o número da sala que queres criar: ")
        while novasalanum in numerosalas:
            novasalanum = input("Essa sala já existe, tenta novamente: ")

        numerosalas.append(novasalanum)  
        cinema.append(sala())  
        print(f"Sala {novasalanum}")
        print(cinema[-1])

        input("Carrega para voltares ao menu: ")


print("Volte sempre!")
