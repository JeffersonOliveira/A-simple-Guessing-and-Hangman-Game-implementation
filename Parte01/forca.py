# -*- coding: utf-8 -*-
# @Author: Jefferson Oliveira
import time
import os


def jogar():
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
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
        print(RED + "               Bem vindo ao jogo da Forca!!!  " + RESET)
        print("")
        print("***************************************************************")
        print(GREEN + " Desenvolvido por: Jefferson Oliveira")
        print(" Contatos:")
        print("    Linkedin: https://www.linkedin.com/in/jeffersonnsoliveira/ ")
        print("      Github: https://github.com/JeffersonOliveira/ " + RESET)
        print(" *************************************************************** \033[0;0m")

    def principal():
        #os.system("cls")
        cabecalho_do_programa()

        palavra_secreta = "banana".upper()
        letras_acertadas = ["_", "_", "_", "_", "_", "_"]
        chutes_realizados = []

        enforcou = False
        acertou = False
        erros = 0
        max_de_chances_para_erros = 6
        qtd_chutes = 1

        #print(letras_acertadas)

        while (not enforcou and not acertou):
            #print("")
            #print("Jogando...{}° tentativa e teve {} erro(s)".format(qtd_chutes,erros))

            print(""); print("Letras Acertadas")
            print(letras_acertadas)

            chute = input("Digite uma letra para o chute da forca: ")
            chute = chute.strip().upper()

            if(chute in palavra_secreta):
                index = 0
                for letra in palavra_secreta:
                    if (chute == letra):
                        letras_acertadas[index] = letra
                    index += 1
            else:
                erros += 1
                print("Ops.. Você errou.Ainda tem {} chances para errar, cuidado!".format(max_de_chances_para_erros-erros))

            enforcou = erros == max_de_chances_para_erros
            acertou  = "_" not in letras_acertadas #acertou  = letras_acertadas.count("_") == 0

            chutes_realizados.append(chute.upper())
            print("Você já fez {} chute(s) e teve {} erro(s) :".format(qtd_chutes, erros))
            print(chutes_realizados)

            qtd_chutes = qtd_chutes + 1

        if(acertou):
            print("");print("Você Ganhou!")
        else:
            print("Você perdeu!")

            '''
            qtd_letras_acertadas = len(letras_acertadas) - letras_acertadas.count("_")
            if qtd_letras_acertadas == len(letras_acertadas):
                print('Parabéns, você acertou todas as letras da palavra!')
                acertou = True
            else:
                print("Você acertou {} de {} letra(s) da palavra!".format(qtd_letras_acertadas,len(letras_acertadas)))
            '''

    principal()
    print(BLUE + "Fim do Jogo!!!" + RESET)
    print("***************************************************************")
    time.sleep(3)

if (__name__ == '__main__'):
    jogar()
