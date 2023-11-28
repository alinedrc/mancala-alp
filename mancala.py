#mancala

# Função para formatar a linha de area de cada jogador
def formatar_linha(lista):
  resultado = "|"
  for elemento in lista:
    resultado += "%3s" % elemento
    resultado += "|"
  return resultado

# Função para converter uma lista de inteiros para uma lista de strings
def converte_para_str(lista_de_ints):
  resultado = []
  for i in lista_de_ints:
    resultado.append(str(i))
  return resultado

#Função para formatar o tabuleiro da mancala
def print_mancala(mancala):
    m1 = mancala[0][0] #mancala do jogador 2
    m2 = mancala[3][0] #mancala do jogador 1
    l1 = ("*---------------------------------*")
    l2 = (f"| P2 |G  |H  |I  |J  |K  |L  | P1 |")
    l3 = (f"|    {formatar_linha(converte_para_str(mancala[2]))}    |")
    l4 = (f"|  {m1} |-----------------------|  {m2} |")
    l5 = (f"|    |A  |B  |C  |D  |E  |F  |    |")
    l6 = (f"|    {formatar_linha(converte_para_str(mancala[1]))}    |")
    l7 = ("*---------------------------------*")

    print(f"{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}\n{l7}")
    
def proxima(linha, coluna, eh_jogador_1):
  if eh_jogador_1:
    if linha == 2 and coluna < 5:
      return linha, coluna + 1
    elif linha == 2 and coluna == 5:
      return 3, 0
    elif linha == 3 and coluna == 0:
      return 1, 5
    elif linha == 1 and coluna > 0:
      return linha, coluna - 1
    elif linha == 1 and coluna == 0:
       return 2, 0

  elif not(eh_jogador_1):
    if linha == 1 and coluna > 0:
      return linha, coluna - 1
    elif linha == 1 and coluna == 0:
      return 0, 0
    elif linha == 0 and coluna == 0:
      return 2, 0
    elif linha == 2 and   coluna < 5:
      return linha, coluna + 1
    elif  linha == 2 and coluna == 5:
      return 1, 5

  return 

jogando = True
eh_jogador_1 = True
sementes_na_mao = -1
ultima_cova = -1
escolha = -1
linha = 0
coluna = 0

while (jogando):
  
  mancala = [[0],[4,4,4,4,4,4],[4,4,4,4,4,4],[0]]

  print("")
  print_mancala(mancala)
  print("")
  
  if eh_jogador_1:
    escolha = input("Jogador 1, escolha uma cova de A a F ou digite 'x' para desistir: ")
  elif not(eh_jogador_1):
    escolha = input("Jogador 2,escolha uma cova de G a L  ou digite 'x' para desistir: ")
  print("")

  if escolha == "x":
        jogando = False 
  elif eh_jogador_1 and escolha == "A":
        cova_escolhida = int(mancala[1][0])
  elif eh_jogador_1 and escolha == "B":
        cova_escolhida = int(mancala[1][1])
  elif eh_jogador_1 and escolha == "C":
        cova_escolhida = int(mancala[1][2])	
  elif eh_jogador_1 and escolha == "D":
        cova_escolhida = int(mancala[1][3])
  elif eh_jogador_1 and escolha == "E":
        cova_escolhida = int(mancala[1][4])
  elif eh_jogador_1 and escolha == "F":
        cova_escolhida = int(mancala[1][5])
  elif not(eh_jogador_1) and escolha == "G":
        cova_escolhida = int(mancala[2][0])
  elif not(eh_jogador_1) and escolha == "H":
        cova_escolhida = int(mancala[2][1])
  elif not(eh_jogador_1) and escolha == "I":
        cova_escolhida = int(mancala[2][2])
  elif not(eh_jogador_1) and escolha == "J":
        cova_escolhida = int(mancala[2][3])
  elif not(eh_jogador_1) and escolha == "K":
        cova_escolhida = int(mancala[2][4])
  elif not(eh_jogador_1) and escolha == "L":
        cova_escolhida = int(mancala[2][5])
  else:
        print("\nEscolha inválida, tente novamente!")
  
  eh_jogador_1 = not(eh_jogador_1)

  #print(cova_escolhida) #print pra ver se as variáveis estão sendo reconhecidas 
  cova_escolhida = mancala[linha][coluna]
  mancala[linha][coluna] = 0
  if int(cova_escolhida) >= 0:
      sementes_na_mao= mancala[linha][coluna]
      mancala[linha][coluna]= 0

  while sementes_na_mao > 0:
        linha, coluna = proxima(linha, coluna, mancala, eh_jogador_1)
        sementes_na_mao -= 1
        mancala[linha][coluna] += 1
  
  eh_jogador_1 = not(eh_jogador_1)


#PENSA EM UM FOR SUA ANTA
