class Personagem(object):

  def __init__(self,nome,ataque,hp,defesa,capacidade,moedas):
    self.nome = nome
    self.ataque = ataque
    self.hp = hp
    self.defesa = defesa
    self.capacidade = capacidade
    self.moedas = moedas
    self.inventario = []
    
  def imprimir_personagem(self):
    print("===============================")
    print("nome:\t\t",self.nome)
    print("ataque:\t\t",self.ataque)
    print("hp:\t\t\t",self.hp)
    print("defesa:\t\t",self.defesa)
    print("capacidade:\t",self.capacidade)
    print("peso atual:\t",self.calcula_peso_atual())
    print("moedas:\t",self.moedas)
    print("===============================")
  
  def imprime_inventario(self):
    for item in self.inventario:
      print("\n===============================")
      item.imprimir_item()

  def comprar(self, item):
    if item.preco < self.moedas and item.peso < (self.capacidade - self.calcula_peso_atual()):
      self.moedas = self.moedas - item.preco
      self.inventario.append(item)
      return True
    else:
      return False

  def calcula_peso_atual(self):
    peso = 0
    for item in self.inventario:
      peso = peso + item.peso
    
    return peso