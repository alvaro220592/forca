# Codificação:
# -*- coding = utf-8 -*-

# Para as palavras aleatórias:
import random


# Se acertar a letra, a palavra vai sendo preenchida. se errar, o sistema mostra a posição seguinte da lista abaixo:
board = ['''

    -=FORCA=-

    +---+
        |
        |
        |
        |
    =========''', '''

    +---+
    O   |
        |
        |
        |
    =========''', '''

    +---+
    O   |
    |   |
        |
        |
    =========''', '''

     +---+
     O   |
    /|   |
         |
         |
    =========''', '''

     +---+
     O   |
    /|\  |
         |
         |
    =========''', '''

     +---+
     O   |
    /|\  |
    /    |
         |
    =========''', '''

     +---+
     O   |
    /|\  |
    / \  |
         |
    =========''']


class Forca():
    # Mostrando o tabuleiro:
    def __init__(self, board):
        self.b = board
        print(self.b)

# Pegando aleatoriamente uma palavra do banco de palavras:
class Palavra():
    # Pegando aleatoriamente uma palavra do banco de palavras:
    def rand():
        with open('palavras.txt', 'r') as f:
            leitura = f.readlines()
            aleatoria = random.choice(leitura)
            p = aleatoria.strip()
            return p

    def digitando(self):
        word = Palavra.rand()
        digitadas = []
        print(f'Digitadas: {len(digitadas)}')
        print(f'{word} - {len(word)}')
        while len(digitadas) < len(word):
            digitadas.append(str(input('Digite uma letra: ')))
        print()





f1 = Forca(board[0])


# Instanciando a classe Palavra:
p1 = Palavra()

p1.digitando()






#### RASCUNHOS ####
# with open('palavras.txt', 'r') as arquivo:
#     leitura = arquivo.readlines()
#     aleatoria = random.choice(leitura)
#     p = aleatoria.strip()
#     print(p)


"""
Mostrar apenas a letra certa na palavra secreta:

palavra = 'alvaro'
letra = 'w'

j = 0
for i in palavra:
    if letra == palavra[j]:
        print (letra)
    else:
        print('_')
    j += 1



"""
