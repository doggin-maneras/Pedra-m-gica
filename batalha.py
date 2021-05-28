from personagem import Personagem

class Batalha(object):

  def __init__(self, jogador, adversario):
    self.jogador = jogador
    self.adversario = adversario
    self.jogador.imprimir_personagem()
    self.adversario.imprimir_personagem()
    self.encerrada = False
    self.modo_ataque_defesa = None

  def ataque_jogador(self):
    dano_ataque = self.jogador.calcula_dano_ataque()
    self.adversario.hp = max(0, self.adversario.hp - dano_ataque)
    if self.adversario.hp == 0:
      self.encerrar_batalha()
    else:
      print("HP adversário", self.adversario.hp)

  def ataque_adversario(self):
    dano_ataque = self.adversario.calcula_dano_ataque()
    self.jogador.hp = max(0, self.jogador.hp - dano_ataque)
    if self.jogador.hp == 0:
      self.encerrar_batalha()
    else:
      print("HP jogador", self.jogador.hp)

  def rodada(self):
    print("Escolha modo de [a]taque ou [d]efesa:")
    input
    if not self.encerrada:
      self.ataque_jogador()
      self.ataque_adversario()
    else:
      print("Esta batalha já encerrou!")

  def encerrar_batalha(self):
    self.encerrada = True
    print("Batalha encerrada!!!")
    self.jogador.imprimir_personagem()
    self.adversario.imprimir_personagem()








#def calcular_dano_modo_defesa(ataque, defesa):
#  fator_defesa = random.random()
#  dano = ataque - (2 * defesa * fator_defesa)
#  dano_arredondado = max(0, dano)
#  return int(dano_arredondado)


#def calcular_dano_modo_ataque(ataque, defesa):
#  fator_defesa = random.random()
#  dano = ataque - (defesa * fator_defesa)
#  return int(dano)


#def gera_numero_aleatorio():
#  aleatorio = random.randint(0, 10)
#  return aleatorio

"""
while (HP > 0 and motoqueiro_generico_hp > 0):
	print("Escolha [a]tacar ou [d]efender")
	estrategia = input()
	if estrategia == "a":
		dano_monstro = calcular_dano_modo_ataque(ATAQUE,
		                                         motoqueiro_generico_defesa)
		dano_carlinhos = calcular_dano_modo_ataque(motoqueiro_generico_ataque,
		                                           DEFESA)
	elif estrategia == "d":
		dano_monstro = 0
		dano_carlinhos = calcular_dano_modo_defesa(motoqueiro_generico_ataque,
		                                           DEFESA)
		if (dano_carlinhos) == 0:
			print("aaaa você eroouuuuuu!")
	else:
		print("oi?")
		dano_monstro = 0
		dano_carlinhos = 0
	HP = max(0, HP - dano_carlinhos)
	motoqueiro_generico_hp = max(0, motoqueiro_generico_hp - dano_monstro)
	print("Carlinhos:", HP)
	print("MG:", motoqueiro_generico_hp)
	print("")
  """