
from item import Item
from personagem import Personagem
from loja import Loja
from batalha import Batalha


"""
lojinha = Loja("Padaria e Cia. do João", 'João');


gustavo = Personagem('Gustavo', 100, 250, 100, 120, 150)
ygor = Personagem('Ygor', 80, 300, 80, 150, 150)

lojinha.recepcao(gustavo)

gustavo.imprimir_personagem()
gustavo.imprime_inventario()

"""


gustavo = Personagem(nome="Gustavo", ataque=50, hp=300, defesa=20, capacidade=100, moedas=500)

motoqueiro = Personagem(nome="Motoqueiro Generico", ataque=30, hp=150, defesa=10, capacidade=50, moedas=100)

batalha_inicial = Batalha(gustavo, motoqueiro)