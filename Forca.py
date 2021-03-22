# Codificação:
# -*- coding = utf-8 -*-

# Para gerar as palavras aleatórias:
import random


# Se acertar a letra, a palavra vai sendo revelada. Se errar, o sistema mostra a posição seguinte da lista abaixo, simulando a adição de menbros do boneco:
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

class Palavra():
    # Pegando aleatoriamente uma palavra do banco de palavras:
    def rand():
        # Comando para abrir um arquivo .txt em modo de leitura('r' de 'read') e atribuindo o nome 'f' para ele:
        with open('palavras.txt', 'r') as f:
            leitura = f.readlines() # O 'readlines' lê as linhas do arquivo 'f'
            aleatoria = random.choice(leitura) # A função 'choice' do módulo random escolhe aleatoriamente uma palavra e a atribui à variável 'aleatoria'
            p = aleatoria.strip() # O 'strip' garante o retorno da palavra sem espaços no início e no fim. Isso foi atribuído à variável 'p'
            return p

    def digitando(self):
        # Função referente ao processo de digitação das letras:
        corpo = 0 # Variável valendo zero que receberá incremento à medida em que o usuário erre as letras
        f1 = Forca(board[corpo]) # Instância da classe Forca, recebendo como parâmetro o board, que neste caso vem na posição zero

        word = Palavra.rand() # Palavra aleatória retornada pela função 'rand()' desta classe e atribuída à variável 'word'
        digitadas = [] # Criação de uma lista vazia que receberá as letras digitadas no decorrer do jogo

        # Referência de ajuda no desenvolvimento:
        # print(f'{word} - {len(word)} letras')

        print('_ ' * len(word)) # Exibição dos underlines que representam a palavra oculta

        print()

        while True:
            entrada = str(input('\nDigite uma letra: '))
            # Em desenvolvimento:
            # if type(entrada) != str:
                # print('Insira apenas letras')
                # continue
            if entrada not in word: # Se a letra inserida não estiver na palavra:
                corpo += 1 # Será mostrado o board da posição seguinte, com um membro a mais do boneco
                print(board[corpo])
                if corpo == 6: # Se a posição do board for a última, o usuário perdeu e o jogo acaba.
                    print('\n============')
                    print('Você perdeu!')
                    print('============')
                    exit()
            else:
                print(board[corpo]) # Senão, o board atual é mostrado
            digitadas.append(entrada) # A letra digitada é agregada à lista de letras digitadas
            print(f'\nLetras digitadas:')
            for d in digitadas: # Para cada item na lista de letras digitadas, aparecerão os itens, ou seja, as letras
                print(d, end = ' ') # O "end = ' '" evita a quebra de linhas a cada item mostrado, pois sem isso, o python entenderia como '\n'


            print()

            print('\nPalavra secreta:')
            i = 0 # Variável valendo zero, que sofrerá incremento e representará o tanto de acertos
            for w in word:
            # Para cada item(letra) na palavra oculta, se este item estiver entre as letras já digitadas, será revelado e o valor 1 será somado como acerto
                if w in digitadas:
                    print(w, end = ' ')
                    i += 1
                    if i >= len(word): # Se o valor de acertos chegar ao comprimento da palavra oculta, significa que o usuário ganhou
                        print('\n============')
                        print('Você ganhou!')
                        print('============')
                        exit()
                else:
                    print('_', end = ' ') # Se não houver letras inseridas combinando com a palavra oculta, seráo exibidos underlines

        print()


# Instanciando a classe Palavra:
p1 = Palavra()

# Chamando a função 'digitando' da classe Palavra
p1.digitando()





# ### RASCUNHOS ####
# with open('palavras.txt', 'r') as arquivo:
#     leitura = arquivo.readlines()
#     aleatoria = random.choice(leitura)
#     p = aleatoria.strip()
#     print(p)
#
#
#
# Mostrar apenas a letra certa na palavra secreta:
#
# palavra = 'alvaro'
# letra = 'w'
#
# for i in palavra:
#     if letra == i:
#         print (letra)
#     else:
#         print('_')
#
# Mostrar as letras corretas já jogadas:
#
# letras = ['a', 'r', 'l', 'x', 'z']
#
# for p in palavra:
#     if p in letras:
#         print(p, end = ' ')
#     else:
#         print('_', end = ' ')
