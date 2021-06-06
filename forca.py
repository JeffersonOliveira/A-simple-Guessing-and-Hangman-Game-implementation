# -*- coding: utf-8 -*-
# @Author: Jefferson Oliveira
import time
import os
from random import randrange

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

def jogar():

    imprime_mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    chutes_realizados = []
    enforcou = False
    acertou = False
    erros = 0
    max_de_chances_para_erros = 7
    qtd_chutes = 1

    while (not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
             marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros, max_de_chances_para_erros)

        enforcou = erros == max_de_chances_para_erros
        acertou  = "_" not in letras_acertadas #acertou  = letras_acertadas.count("_") == 0
        chutes_realizados.append(chute.upper())

        imprime_mensagem_de_atualizacao_de_jogadas(letras_acertadas, chutes_realizados, qtd_chutes, erros)

        qtd_chutes = qtd_chutes + 1

    if(acertou):
        imprime_mensagem_vencedor(letras_acertadas)
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    mensagem_de_final_de_jogo()


def imprime_mensagem_de_abertura():
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
    print(RED + "               Bem vindo ao jogo da Forca!!!  " + RESET)
    print("")
    print("***************************************************************")
    print(GREEN + " Desenvolvido por: Jefferson Oliveira")
    print(" Contatos:")
    print("    Linkedin: https://www.linkedin.com/in/jeffersonnsoliveira/ ")
    print("      Github: https://github.com/JeffersonOliveira/ " + RESET)
    print(" *************************************************************** \033[0;0m")
    print(BLUE + "Você está no jogo da forca e tem 7 chances de acertar antes de se enforcar!!!"+ RESET)

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r', encoding='utf-8')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    indice_palavras = randrange(0, len(palavras))
    palavra_secreta = palavras[indice_palavras].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra] # list comprehensions

def pede_chute():
    chute = input("Digite uma letra para o chute da forca: ")
    chute = chute.strip().upper()
    return(chute)

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor(letras_acertadas):
    print("Parabéns, você ganhou!")
    print("A palavra era {}".format(letras_acertadas))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_de_atualizacao_de_jogadas(letras_acertadas, chutes_realizados, qtd_chutes, erros):
    print("");
    print("Letras Acertadas")
    print(letras_acertadas,"\n\n");
    print(RED +"-------------------------------------"+RESET)
    print("Você já fez {} chute(s) e teve {} erro(s) :".format(qtd_chutes, erros))
    print(chutes_realizados)
    print(RED + "-------------------------------------\n" + RESET)

def mensagem_de_final_de_jogo():
    print(BLUE + "Fim do Jogo!!!" + RESET)
    print("***************************************************************")
    time.sleep(3)

def desenha_forca(erros, max_de_chances_para_erros):
    print("Ops.. Você errou.Ainda tem {} chances para errar, cuidado!".format(max_de_chances_para_erros - erros))
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == '__main__'):
    jogar()
