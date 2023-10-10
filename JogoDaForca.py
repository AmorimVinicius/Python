# Importar bibliotecas
import random
import sys

# Variáveis
lista_letras            = []
lista_palavras          = ["bolacha", "rinoceronte", "computador"]
palavra_escolhida       = random.choice(lista_palavras)
palavra_escondida       = "*" * len(palavra_escolhida)
lista_palavra           = list(palavra_escolhida)
palavra_criptografada   = list("*" * len(palavra_escolhida))
chance                  = 0

while True:
    while True:
        print(f'\n\nPalavra escondida: {palavra_escondida}')

        letra_digitada = input("Digite apenas uma letra: ").lower()

        # verifica se somente uma letra foi digitada
        tamanho_letra = len(letra_digitada)
        if (tamanho_letra != 1 and letra_digitada.isdigit()):
            continue
        else:
            # verifica se letra já foi inserida anteriormente
            if (letra_digitada in lista_letras):
                print(f'\n******************************\nA letra [{letra_digitada}] já foi inserida. Favor, informar outra letra\n******************************')
                continue

            # adiciona letra digitada na lista
            lista_letras.append(letra_digitada)

            # zera variáveis de controle
            auxiliar        = 0
            acertou_letra   = 0

            # percorre cada caractere da palavra escolhida
            for letra in lista_palavra:
                # se a letra foi encontrada, altera variável
                if (letra_digitada == letra):
                    palavra_criptografada[auxiliar] = letra
                    acertou_letra = 1
                
                auxiliar += 1
            
            # verifica se letra foi encontrada
            if (acertou_letra == 0):
                chance += 1

            # verifica se a quantidade de vezes foi atingida
            if (chance == 3):
                print("\n\n****************************** Você não conseguiu dessa vez :( ******************************\n")
                while True:
                    resposta = input("Deseja tentar novamente: [sim] ou [nao]: ").lower()
                    
                    if (resposta == "sim"):
                        continue
                    elif (resposta == "nao"):
                        print("****************************** Até uma próxima ! ******************************\n")
                        break
                    else:
                        print("Eu não entendi sua resposta\n")

            else:
                palavra_escondida = "".join(palavra_criptografada)

                if (palavra_escondida == palavra_escolhida):
                    print(f"\n****************************** Parabéns, você acertou a palavra: {palavra_escondida} ******************************\n")
                    sys.exit()
                    
                   
