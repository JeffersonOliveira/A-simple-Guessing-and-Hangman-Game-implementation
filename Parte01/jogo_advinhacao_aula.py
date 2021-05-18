# -*- coding: utf-8 -*-
#@Author: Jefferson Oliveira
import time
import os
import random

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def cabecalho_do_programa():
        """
        Created on Mon May 10 13:16:26 2021
        O objetivo do código é fazer um jogo de advinhação.
        Teremos a principio um valor fixo de número a ser advinhado;
        A pessoa irá tentar acertar o valor que julga ser o "sorteado";
        O programa tem que dizer se o valor é maior, menor ou se foi o acertado;
        """
        print("***************************************************************")
        print("***************************INICIO******************************")
        print("")
        print( RED + "      Bem vindo ao jogo de Advinhação!!!  " + RESET)
        print("")
        print("***************************************************************")
        print(GREEN+ " Desenvolvido por: Jefferson Oliveira")
        print(" Contatos:")
        print("    Linkedin: https://www.linkedin.com/in/jeffersonnsoliveira/ ")
        print("      Github: https://github.com/JeffersonOliveira/ "+ RESET)
        print(" *************************************************************** \033[0;0m")

def principal():
    os.system("cls")    
    cabecalho_do_programa()
    
    #numero_advinhacao = round(random.random() * 100) # 0.0 1.0
    print(RED + "Vamos realizar um sorteio, você deve escolher abaixo o intervalo que deseja!" + RESET)
    valor_max = int(input("Digite de 1 até qual número você desejar realizar o sorteio: "))
    numero_advinhacao = random.randrange(1,valor_max+1)
    total_de_tentativas = 0

    print("Qual nível de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Díficil")

    nivel = int(input("Defina um nível: "))

    if (nivel == 1):
        total_de_tentativas = 9
    elif (nivel == 2):
        total_de_tentativas = 6
    else:
        total_de_tentativas = 3    

    print(numero_advinhacao)

    for  rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas));
        chute_str = input(f"Digite um número entre 1 e {valor_max}:  ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)
        acertou         = chute == numero_advinhacao
        chute_foi_maior = chute > numero_advinhacao
        chute_foi_menor = chute < numero_advinhacao
       
        if(chute < 1 or chute > valor_max):
            print(RED + f"Você deve digitar um número entre 1 e {valor_max}"+ RESET)
            print("")
            continue

        if (acertou):
            print(GREEN + "Parabéns, você acertou o número! " + RESET)
            print("")
            break
        elif (chute_foi_maior):
            print(RED + "Você errou! O número ",chute," é maior o número a ser advinhado "+ RESET)
            print("")
        elif (chute_foi_menor):
            print(RED +"Você errou! O número ",chute," é menor o número a ser advinhado "+ RESET)
            print("")

# Essa função não está sendo mais utilizada:
def reinicia_jogo():
    resposta = input("Deseja tentar novamente ('y'/'n') ?")
    print("Você digitou: ", resposta)
    time.sleep(3)
    while (resposta != "y" or resposta != "n"):
        if (resposta == "n"):
            print("")
            print(BLUE +"Foi bom jogar com você até mais!" + RESET);
            break

        elif (resposta == "y"):
            print("Reiniciando o jogo!");
            time.sleep(1)

            os.system("cls")
            print("Você terá mais uma chance!")
            principal()
            break
            
        else:
            print("Valor inválido! ")
            resposta = input("Por favor,escolha 'y' ou 'n'!")       
    

principal()
print(BLUE + "Fim do Jogo!!!" + RESET)
print("***************************************************************")
time.sleep(3)