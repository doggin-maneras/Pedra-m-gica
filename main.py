from item import Item
from personagem import Personagem
from loja import Loja

lojinha = Loja("Padaria e Cia. do João", 'João');


gustavo = Personagem('Gustavo', 100, 250, 100, 120, 150)
ygor = Personagem('Ygor', 80, 300, 80, 150, 150)

lojinha.recepcao(gustavo)

gustavo.imprimir_personagem()
gustavo.imprime_inventario()