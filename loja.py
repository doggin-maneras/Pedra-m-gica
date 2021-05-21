from item import Item

def eh_inteiro(s):
  try:
      int(s)
      return True
  except ValueError:
      return False

class Loja(object):

  def __init__(self,nome,vendedor):
    self.nome = nome;
    self.vendedor = vendedor;
    self.estoque = {}
    self.itens = []
    self._inicializa_estoque();

  def _inicializa_estoque(self):
    espadinha = Item('Espada da galinha', 100, 10, ataque=25, alcance=1)
    escudinho = Item('Escudo de bambu', 50, 15, defesa=10)
    runa = Item('Runa', 500, 5, durabilidade=10, alcance=6, ataque=80)
    picles = Item('picles', 15, 1, durabilidade=1, recuperacao=15)
    teclado_magico = Item('teclado magico', 188, 20, ataque=50, alcance=10)

    self.estoque[escudinho] = 5
    self.estoque[espadinha] = 3
    self.estoque[runa] = 10
    self.estoque[picles] = 100
    self.estoque[teclado_magico] = 1

    self.itens.append(espadinha)
    self.itens.append(escudinho)
    self.itens.append(runa)
    self.itens.append(picles)
    self.itens.append(teclado_magico)

  def exibir_produtos(self):
    for i, item in enumerate(self.itens):
      if self.estoque[item] > 0:
        print("\n===============================")
        print("Item", i)
        item.imprimir_item()
  
  def escolher_produtos(self, personagem):
    print("===============================");
    print("Algum produto te interessou %s? Digite o número" % personagem.nome)
    opcao = input()
    if eh_inteiro(opcao):
      opcao = int(opcao)
      if opcao < 0:
        print("Opção inválida!")
        return -1
      elif opcao >= len(self.itens):
        print("Opção inválida!")
        return -1
      elif self.estoque[self.itens[opcao]] < 1:
        print("Este produto está em falta!")
        return -1
    else:
      print("Opção inválida!")
      return -1

    print("Detalhes do produto:")
    self.itens[opcao].imprimir_item()

    print("Deseja comparar o item? [s/n]")
    confirmacao = input()
    if (confirmacao == 's'):
      self.vender(self.itens[opcao])
      situacao_venda = personagem.comprar(self.itens[opcao])
      if situacao_venda:
        print("Parabéns, você comprou um %s" % self.itens[opcao].nome)
      else:
        print("Dá o fora daqui seu pé rapado!")
        return -1
    elif (confirmacao == 'n'):
      print("Poxa, que pena!")
      return 0;
    else:
      print("Oi? não entendi...")
      return -1

  def vender(self, item):
    self.estoque[item] = self.estoque[item] - 1

  def recepcao(self, personagem):
    print("============================");
    print("Seja bem vindo à %s, %s! Eu sou o %s, como posso te ajudar?" % (self.nome, personagem.nome, self.vendedor))
    paciencia = 5;

    while (paciencia > 0):
      print("Gostaria de verificar nossos produtos? [s/n]")
      opcao = input()
      if opcao == 's':
        self.exibir_produtos()
        resultado = -1
        resultado = self.escolher_produtos(personagem)
        if resultado == -1:
          paciencia = paciencia - 1
      elif opcao == 'n':
        print("Tudo bem, adeus!")
        paciencia = 0
      elif paciencia == 1:
        print("Ah vai se ferrar então! Seu burro!")
        paciencia = paciencia - 1;
      else:
        print("Oi? não entendi...")
        paciencia = paciencia - 1;

    print("===============================");