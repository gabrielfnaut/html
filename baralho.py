import random

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

def criar_baralho():
    baralho = []
    naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for naipe in naipes:
        for valor in valores:
            baralho.append(Carta(valor, naipe))
    return baralho

def distribuir_cartas(baralho):
    random.shuffle(baralho)
    pilhas = [[] for _ in range(8)]  # Criando as oito pilhas
    for i, carta in enumerate(baralho):
        pilhas[i % 8].append(carta)  # Distribuindo as cartas nas pilhas
    return pilhas

def exibir_mesa(pilhas):
    for i, pilha in enumerate(pilhas, start=1):
        print(f'Pilha {i}: {[carta.valor + carta.naipe for carta in pilha]}')

# Criando o baralho
baralho = criar_baralho()

# Distribuindo as cartas nas pilhas
pilhas = distribuir_cartas(baralho)

# Exibindo a configuração atual da mesa
exibir_mesa(pilhas)


