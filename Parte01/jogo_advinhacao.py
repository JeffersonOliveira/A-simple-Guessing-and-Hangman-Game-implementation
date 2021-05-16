# -*- coding: utf-8 -*-
#@Author: Jefferson Oliveira
import time
import os

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
    numero_advinhacao = 42

    # Teste a branch novo
    chute_str = input("Digite um chute com o número que acha que é o certo: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou         = chute == numero_advinhacao
    chute_foi_maior = chute > numero_advinhacao
    chute_foi_menor = chute < numero_advinhacao
    
    if (acertou):
        print("")
        print(GREEN + "Parabéns, você acertou o número! " + RESET)
        reinicia_jogo()
        print("")
    elif (chute_foi_maior):
        print("")
        print(RED + "Você errou! O número ",chute," é maior o número a ser advinhado "+ RESET)
        reinicia_jogo()
        print("")
    elif (chute_foi_menor):
        print("")
        print(RED +"Você errou! O número ",chute," é menor o número a ser advinhado "+ RESET)
        reinicia_jogo()
        print("")


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
print("Tchau!!!")
print("***************************************************************")
time.sleep(3)
