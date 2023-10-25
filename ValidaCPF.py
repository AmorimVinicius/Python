# inicia variaveis
controle    = 10
soma        = 0
soma_mod    = 0


# valida se usuario digitou a quantidade correta de caracteres
while True:

    cpf = input("Digite o cpf: ")
    if ((len(cpf) > 11) or (len(cpf) < 11)):
        print("\nPor favor, Digite 11 caracteres")
    else:
        break


# captura posicoes
cpf_inicio      = cpf[0:9]
primeiro_digito = cpf[-2]
segundo_digito  = cpf[-1]


# valida 1º digito
for caractere in cpf_inicio:
    soma = soma + (int(caractere) * controle)
    controle -= 1


# com a soma da validacao anterior, multiplica por 10
soma *= 10


# com o resultado anterior, recupera o resto da divisao
soma_mod = soma % 11

if (soma_mod) > 9:
    print("Primeiro caractere deve ser 0")
else:
    print(f'O caractere deve ser {soma_mod}')