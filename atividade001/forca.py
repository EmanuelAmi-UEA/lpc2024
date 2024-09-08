import random

palavras = open("br-sem-acentos.txt", "r")
lista_palavras = []


for i in palavras:
    i = i.replace("\n", "")
    lista_palavras.append(i)

palavra_selecionada = random.choice(lista_palavras)

letras_escritas = []

tentativas = 0
status = False

while tentativas < 6:

    for letter in palavra_selecionada:
        if letter in letras_escritas:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")

    print(f'\n{letras_escritas}\n')
    jogo = input("Digite uma letra: ").lower()
    letras_escritas.append(jogo)

    if jogo not in palavra_selecionada:
        tentativas += 1
        print(f'{6-tentativas} de 6 tentativas')

    status = True
    for letter in palavra_selecionada:
        if letter not in letras_escritas:
            status = False

    if status:
        break

if status:
    print("PARABENS VOCÊ GANHOUUU!!!!")

else:
    print(f'Que pena, não foi dessa vez. A palavra era {palavra_selecionada}')
