from random import randint

jogando = True
eh_jogador_1 = randint(1,2) == 1
sementes_na_mao = -1 #as variáveis estão com valor negativo para ficar inválido e inicializá-las
escolha = -1
linha = 0
coluna = 0
cova_escolhida = -1
mancala = [[0],[4,4,4,4,4,4],[4,4,4,4,4,4],[0]]
mancala_p2 = mancala[0][0] #mancala do jogador 2
mancala_p1 = mancala[3][0] #mancala do jogador 1

# Função para formatar a linha de area de jogada de cada jogador
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
    mancala_p2 = mancala[0][0] #mancala do jogador 2
    mancala_p1 = mancala[3][0] #mancala do jogador 1
    l1 = ("*--------<<< JOGADOR 2 <<<--------*")
    l2 = (f"| P2 |G  |H  |I  |J  |K  |L  | P1 |")
    l3 = (f"|    {formatar_linha(converte_para_str(mancala[2]))}    |")
    l4 = (f"| {mancala_p2:02d} |-----------------------| {mancala_p1:02d} |")
    l5 = (f"|    |A  |B  |C  |D  |E  |F  |    |")
    l6 = (f"|    {formatar_linha(converte_para_str(mancala[1]))}    |")
    l7 = ("*-------->>> JOGADOR 1 >>>--------*")

    print(f"{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}\n{l7}")
    
def proxima(linha, coluna, eh_jogador_1):
  if eh_jogador_1:
    if linha == 1:
        return (linha,coluna+1) if coluna < 5 else (3,0)
    elif linha == 2:
        return (linha,coluna - 1) if coluna > 0 else (1,0)
    elif linha == 3:
        return (2,5)
  else:
    if linha == 2:
        return (linha,coluna-1) if coluna > 0 else (0,0)
    elif linha == 1:
        return (linha,coluna+1) if coluna < 5 else (2,5)
    elif linha == 0:
        return (1,0)

def esvaziar_cova(linha,coluna):
    mancala[linha][coluna] = 0

def capturar_sementes(mancala,linha,coluna):
      if linha == 1 and mancala[1][coluna] == 1 and sementes_na_mao == 0 and mancala[2][coluna] != 0 and eh_jogador_1:
            mancala[3][0] = mancala[2][coluna] + mancala[1][coluna] + mancala[3][0]
            mancala[2][coluna] = 0
            mancala[1][coluna] = 0
      elif linha == 2 and mancala[2][coluna] == 1 and sementes_na_mao == 0 and mancala[1][coluna] != 0 and not(eh_jogador_1):
            mancala[0][0] = mancala[2][coluna] + mancala[1][coluna] + mancala[0][0]
            mancala[2][coluna] = 0
            mancala[1][coluna] = 0
      return 

def zerar_linha(linha):
     for i in range(len(linha)):
          linha[i] = 0
          
def soma_sementes(linha):
     soma = 0
     for cova in linha:
          soma += cova
     return soma

def eh_fim_de_jogo(mancala):
     soma_jogador_1 = soma_sementes(mancala[1])
     soma_jogador_2 = soma_sementes(mancala[2])
     
     if soma_jogador_1 > 0 and soma_jogador_2 > 0:
          return False
     
     if soma_jogador_2 == 0:
          mancala[3][0] += soma_jogador_1
          zerar_linha(mancala[1])
     if soma_jogador_1 == 0:
         mancala[0][0] += soma_jogador_2
         zerar_linha(mancala[2])

     return True

#Função para verificar se aquela cova pode retornar as mancalas, se não o jogar não joga de volta
def pode_jogar_novamente(linha, coluna, eh_jogador_1): 
     if eh_jogador_1:
          return linha == 3 and coluna == 0
     else:
          return linha == 0 and coluna == 0   

while (jogando):
            print("")
            print_mancala(mancala)
            print("")

            if eh_fim_de_jogo(mancala):
                  print_mancala(mancala)
                  print("\nFim de jogo!")
                  placar_p1 = 0
                  placar_p2 = 0
                  if mancala[3][0] > mancala[0][0]:
                      print("\nJogador 1 ganhou!")
                      placar_p1 += 1
                  elif mancala[3][0] < mancala[0][0]:
                      print("\nJogador 2 ganhou!")
                      placar_p2 += 1
                  else:
                      print("Empatou :(")
                      placar_p1 += 1
                      placar_p2 += 1
                  print("")
                  print("*------PLACAR-----*")
                  print(f"| P1 | {placar_p1} X {placar_p2} | P2 |")
                  print("*-----------------*")

                  jogando = False
                  
                  novo_jogo = input("\nVocê quer jogar mais uma rodada? Digite Sim ou Não. ")
                  if novo_jogo == "Sim":
                        mancala = [[0],[4,4,4,4,4,4],[4,4,4,4,4,4],[0]] #Aqui faz um reset no tabuleiro
                        jogando = True
                  else:
                        print("\nObrigada por jogar, até a próxima!")
                  
            else:
                  escolha_feita = False
                  while not escolha_feita:
                        if eh_jogador_1:
                              escolha = input("\nJogador 1, escolha uma cova de A a F ou digite 'x' para desistir: ")
                              print("")
                        else:
                              escolha = input("\nJogador 2,escolha uma cova de G a L  ou digite 'x' para desistir: ")
                              print("")
            
                        if escolha == "x":
                              jogando = False
                              escolha_feita = True

                        elif eh_jogador_1 and escolha == "A":
                              cova_escolhida = (1,0)
                              escolha_feita = True
                        elif eh_jogador_1 and escolha == "B":
                              cova_escolhida = (1,1)
                              escolha_feita = True
                        elif eh_jogador_1 and escolha == "C":
                              cova_escolhida = (1,2)
                              escolha_feita = True
                        elif eh_jogador_1 and escolha == "D":
                              cova_escolhida = (1,3)
                              escolha_feita = True
                        elif eh_jogador_1 and escolha == "E":
                              cova_escolhida = (1,4)
                              escolha_feita = True
                        elif eh_jogador_1 and escolha == "F":
                              cova_escolhida = (1,5)
                              escolha_feita = True
                        elif not(eh_jogador_1) and escolha == "G":
                              cova_escolhida = (2,0)
                              escolha_feita = True
                        elif not(eh_jogador_1) and escolha == "H":
                              cova_escolhida = (2,1)
                              escolha_feita = True
                        elif not(eh_jogador_1) and escolha == "I":
                              cova_escolhida = (2,2)
                              escolha_feita = True
                        elif not(eh_jogador_1) and escolha == "J":
                              cova_escolhida = (2,3)
                              escolha_feita = True
                        elif not(eh_jogador_1) and escolha == "K":
                              cova_escolhida = (2,4)
                              escolha_feita = True
                        elif not(eh_jogador_1) and escolha == "L":
                              cova_escolhida = (2,5)
                              escolha_feita = True
                        else:
                              print("\nEscolha inválida, tente novamente!\n")
                        
                        if jogando and escolha_feita:
                              linha, coluna = cova_escolhida
                              sementes_na_mao = mancala[linha][coluna]
                              if sementes_na_mao == 0:
                                    print("\nEscolha inválida, sem sementes nessa cova!\n")
                              else:
                                    escolha_feita = True
                                    esvaziar_cova(linha,coluna)
                                    while sementes_na_mao > 0:
                                          linha, coluna = proxima(linha,coluna,eh_jogador_1)
                                          sementes_na_mao -= 1
                                          mancala[linha][coluna] += 1
                                          capturar_sementes(mancala,linha,coluna)
                                    jogar_novamente = pode_jogar_novamente(linha,coluna,eh_jogador_1)
                                    if not jogar_novamente:
                                          eh_jogador_1 = not(eh_jogador_1)
                                    else:
                                          print("Pode jogar novamente! \n")