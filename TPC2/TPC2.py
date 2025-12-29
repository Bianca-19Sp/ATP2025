#TPC2 - Jogo dos 21 Fósforos

def menu():
    print('-='*20)
    print('Seja bem-vindo ao JOGO DOS 21 FÓSFOROS!')
    print('-='*20)
    print('''Aqui estão as regras do jogo:
          -Cada jogador retira 1 a 4 fósforos, á vez;
          -Quem retirar o último fósforo perde!''')
    print('1. Quero ser o primeiro jogador!')
    print('2. Quero ser o segundo jogador!')
    print('3. Sair.')

#Se o primeiro jogador for o jogador:
def pri():
    fosf = 21
    while fosf > 1:
        salto = int(input('Quantos fósforos queres retirar?'))
        while salto > 4 or salto < 1:
            print('Só pode retirar entre 1 a 4 fósforos! Tenta outra vez.')
            salto = int(input('Quantos fósforos queres retirar?'))
        fosf = fosf -salto
        comp = 5 - salto
        fosf = fosf - comp
        print(f'Eu retiro {comp} fósforos. É a tua vez, sobram {fosf}.') 
    print('Perdeste porque ficaste com o último fósforo!') 

#Se o segundo jogador for o jogador:
def seg():
    from random import randint
    fosf = 21
    while fosf > 1:
        comp = randint(1,4)
        fosf = fosf - comp
        salto = int(input(f'Eu retiro {comp} fósforos. Sobram {fosf}. Quantos retiras?'))
        while salto > 4:
            print('Só pode retirar, no MÁXIMO, 4 fósforos!')
            salto = int(input('Quantos fósforos queres retirar?'))
        while salto < 1:
            print('Tens de retirar, no MÍNIMO 1, fósforo!') 
            salto = int(input('Quantos fósforos queres retirar?'))
        fosf = fosf - salto
        if fosf == 1:
            print('Fiquei com o último fósforo. Perdi! :( ')

        if salto != 5 - comp:
            if fosf > 16:
                comp = fosf - 16
            elif fosf > 11:
                comp = fosf - 11
            elif fosf > 5:
                comp = fosf - 5
            elif fosf > 1:
                comp = fosf - 1
            
            fosf = fosf - comp
            while fosf > 1:
                salto = int(input(f'Eu retiro {comp} fósforos. Sobram {fosf}. Quantos queres retirar?'))
                while salto > 4:
                    print('Só pode retirar no MÁXIMO 4 fósforo! Tenta outra vez.')
                    salto = int(input('Quantos fósforos queres tirar?'))
                while salto < 1:
                    print('Tens de retirar no MÍNIMO 1 fósforo. Tenta outra vez.')
                    salto = int(input(f'Quantos fósforos queres tirar?'))
                fosf = fosf - salto
                comp = 5 - salto
                fosf = fosf - comp

            print('Perdeste porque ficaste com o último fósforo.')

def terc():
    print('Obrigada! Volte sempre.')

# Jogo dos fósforos

menu()
opção = int(input('Selecione uma das opções:'))

while opção != 3:
    if opção == 1:
        pri()
    elif opção == 2:
        seg()
    else:
        print('Opção inválida.')
    menu()
    opção = int(input('Selecione uma das opções:'))
terc()
