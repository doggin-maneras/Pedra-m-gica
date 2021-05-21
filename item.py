class Item(object):

  def __init__(self, nome, preco, peso, ataque=None, durabilidade=None, defesa=None, recuperacao=None, alcance=None):
    self.nome = nome
    self.ataque = ataque
    self.durabilidade = durabilidade
    self.defesa = defesa
    self.peso = peso
    self.preco = preco
    self.recuperacao = recuperacao
    self.alcance = alcance

  def imprimir_item(self):
    print("===============================");
    print("Nome:\t\t\t", self.nome)
    
    if self.ataque is not None:
      print("Ataque:\t\t\t", self.ataque)

    if self.defesa is not None:
      print("Defesa:\t\t\t", self.defesa)