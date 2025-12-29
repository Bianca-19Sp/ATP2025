#TPC3

operação = (-1)
lista = []
import random

while operação != 0:
    print(""" MENU:
1) Criar Lista
2) Ler Lista
3) Soma
4) Média
5) Maior 
6) Menor
7) Ordenada por ordem crescente?
8) Ordenada por ordem decrescente?
9) Procura um elemento
10) Sair""")
    
    operação = int(input('Escolha uma operação: '))
    
    if operação == 1:
        tamanho = int(input('Quantos elementos quer que a sua lista tenha? '))
        lista = [random.randrange(1,101) for x in range(tamanho)]
        print(lista)

    elif operação == 2:
        tamanho = int(input('Quantos elementos quer que a sua lista tenha? '))
        i = 0
        while tamanho > 0:
            i = i + 1
            num = int(input(f'Introduza o {i}º número da sua lista: '))
            lista.append(num)
            tamanho = tamanho - 1
        print(lista) 
    
    elif operação == 3:
        if lista == []:
            print(lista)
            tamanho = len(lista)
            i = 0
            soma = 0
            while i < tamanho:
                num = lista[i]
                i = i + 1
                soma = soma + num
                print(f'O resultado da soma é {soma}.')

    elif operação == 4:
        if lista == []:
            print('É necessário uma lista, para a execução desta função. No menu, escolha a opção 1 ou 2.')
        else:
            print(lista)
            tamanho = len(lista)
            i = 0
            soma = 0
            while i < tamanho:
                num = lista[i]
                i = i + 1
                soma = soma + num
            média = soma / tamanho
            print(f'A média é de {média}!')
    
    elif operação == 5:
        if lista == []:
            print('É necessário uma lista, para a execução desta função. No menu, escolha a opção 1 ou 2.')
        else:
            print(lista)
            tamanho = len(lista)
            i = 0
            maior = 0
            while i < tamanho:
                num = lista[i]
                i = i + 1
                if num > maior:
                    maior = num
            print(f'O maior número é {maior}!')
    
    elif operação == 6:
        if lista == []:
            print('É necessário uma lista, para a execução desta função. No menu, escolha a opção 1 ou 2.')
        else:
            print(lista)
            tamanho = len(lista)
            i = 0
            menor = 0
            while i < tamanho:
                num = lista[i]
                i = i + 1
                if num < menor:
                    maior = num
            print(f'O menor número é {menor}!')
    
    elif operação == 7:
        if lista == []:
            print('É necessário uma lista, para a execução desta função. No menu, escolha a opção 1 ou 2.')
        else:
            print(lista)
            tamanho = len(lista) - 1
            i = 0
            while i < tamanho:
                if lista [i] < lista[i + 1]:
                    i = i + 1
                    if i == tamanho:
                        print('Sim!')
                else: 
                    print('Não!')
                    i = tamanho

    elif operação == 8:
        if lista == []:
            print('É necessário uma lista, para a execução desta função. No menu, escolha a opção 1 ou 2.')
        else:
            print(lista)
            tamanho = len(lista) - 1
            i = 0
            while i < tamanho:
                if lista [i] > lista[i + 1]:
                    i = i + 1
                    if i == tamanho:
                        print('Sim!')
                else:
                    print('Não!')
                    i = tamanho
    
    elif operação == 9:
        if lista == []:
            print('É necessário uma lista, para a execução desta função. No menu, escolha a opção 1 ou 2.')
        else:
            print(lista)
            tamanho = len(lista) - 1
            i = 0
            elem = int(input('Introduza o elemento que pretende procurar na lista: '))
            if elem in lista:
                while i < tamanho:
                    if lista[i] == elem:
                        print(f'A sua posição é {i + 1}.')
                        i = tamanho
                    else:
                        i = i + 1
            else:
                print('A sua posição é -1.')
            
print('O programa terminou!')
