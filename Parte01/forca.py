# -*- coding: utf-8 -*-
#@Author: Jefferson Oliveira
import time
import os
import random

def jogar():
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
            print( RED + "               Bem vindo ao jogo da Forca!!!  " + RESET)
            print("")
            print("***************************************************************")
            print(GREEN+ " Desenvolvido por: Jefferson Oliveira")
            print(" Contatos:")
            print("    Linkedin: https://www.linkedin.com/in/jeffersonnsoliveira/ ")
            print("      Github: https://github.com/JeffersonOliveira/ "+ RESET)
            print(" *************************************************************** \033[0;0m")
            print("")
            print( RED + BOLD + "         PROJETO EM DESENVOLVIMENTO  !!!  " + RESET)
            print("")
            print("***************************************************************")

    def principal():
    # os.system("cls")    
        cabecalho_do_programa()

        palavra_secreta = "banana"
        letras_acertadas =["_","_","_","_","_","_"]
        chutes_realizados=[]

        enforcou = False
        acertou  = False
        qtd_chutes = 1

        while(not enforcou and not acertou):
            
            chute = input("Digite uma letra para o chute da forca: ")
            chute = chute.strip()
            
            index = 0
            for  letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    #print("Encontrei a letra '{}' na posição {}".format(chute,index))
                    letras_acertadas[index] = letra
                index= index + 1    

            chutes_realizados.append(chute.lower())    
            print("Chutes já realizados:")
            print(chutes_realizados)
            print("")
            print("Letras Acertadas")
            print(letras_acertadas)
            print("Jogando...{}° tentativa...".format(qtd_chutes))
            qtd_chutes = qtd_chutes + 1
                
    principal()
    print(BLUE + "Fim do Jogo!!!" + RESET)
    print("***************************************************************")
    time.sleep(3)

if(__name__ == '__main__'):
    jogar()