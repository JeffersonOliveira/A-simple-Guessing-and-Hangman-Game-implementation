# -*- coding: utf-8 -*-
#@Author: Jefferson Oliveira
import time
import os
import random
import forca
import adivinhacao


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
        print("")
        print( RED + "               Escolha seu jogo!!!  " + RESET)
        print("")
        print("***************************************************************")
        print(GREEN+ " Desenvolvido por: Jefferson Oliveira")
        print(" Contatos:")
        print("    Linkedin: https://www.linkedin.com/in/jeffersonnsoliveira/ ")
        print("      Github: https://github.com/JeffersonOliveira/ "+ RESET)
        print(" *************************************************************** \033[0;0m")

def principal():
    #os.system("cls")    
    cabecalho_do_programa()

    print("(1) Forca | (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1 ):
        print("Foi escolhido o Jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Foi escolhido o Jogo da Advinhação")
        adivinhacao.jogar()

    
principal()
print(BLUE + "Fim do Jogo!!!" + RESET)
print("***************************************************************")
time.sleep(3)
