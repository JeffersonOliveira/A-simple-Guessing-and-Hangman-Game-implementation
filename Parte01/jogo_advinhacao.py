# -*- coding: utf-8 -*-
#@Author: Jefferson Oliveira
import time
import os

def cabecalho_do_programa():
        """
        Created on Mon May 10 13:16:26 2021
        O objetivo do código é fazer um jogo de advinhação.
        Teremos a principio um valor fixo de número a ser advinhado;
        A pessoa irá tentar acertar o valor que julga ser o "sorteado";
        O programa tem que dizer se o valor é maior, menor ou se foi o acertado;
        """
        print("*************************************************")
        print("*****************INICIO**************************")
        print("")
        print("      Bem vindo ao jogo de Advinhação!!!         ")
        print("")
        print("*************************************************")
        print("    Desenvolvido por: Jefferson Oliveira")
        print("    Contato:xxxxxxxxxxxxxxxxx")
        print("*************************************************")

def principal():
    
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
        print("Parabéns, você acertou o número!")
        print("")
    elif (chute_foi_maior):
        print("")
        print("Você errou! O número ",chute," é maior o número a ser advinhado")
        print("")
    elif (chute_foi_menor):
        print("")
        print("Você errou! O número ",chute," é menor o número a ser advinhado")
        print("")

def reinicia_jogo():

    resposta = input("Deseja tentar novamente ('y'/'n') ?")
    print("Você digitou: ", resposta)
    while (resposta != "y" or resposta != "n"):
        if (resposta == "n"):
            print("")
            print("Foi bom jogar com você até mais!");
            break

        elif (resposta == "y"):
            print("Reiniciando o jogo!");
            time.sleep(1)

            os.system("cls")
            principal()
            
        else:
            print("Valor inválido! ")
            resposta = input("Por favor,escolha 'y' ou 'n'!")       
    

principal()
reinicia_jogo()
print("")
print("**********************FIM************************")
