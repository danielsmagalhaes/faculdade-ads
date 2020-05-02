def cadastro():

    print("Bem-vindo ao seu Planejador de viajens\n")
    print("Vamos preencher seu cadastro? \n")

    nome = input("Qual seu nome? ")
    teto = float(input("Qual valor máximo que deseja gastar na viagem? "))
    qtde = int(input("Quantas paradas sua viagem terá? "))

    return teto, qtde


def destinos(qtde):
    print("\nAgora vamos incluir seus destinos? ")
    totaldias = 0
    for c in range(qtde):

        print("\n=== Destino {} ===".format(c + 1))
        destino = input("Informe a cidade/país de destino: ")
        dias = int(input("Quantos dias prentende ficar em {}?".format(destino)))

        totaldias = totaldias + dias

    return totaldias

def gasto_diario(teto, totaldias):
    print("\nVocê poderá gastar em média R$ {0:.2f} por dia".format(teto/totaldias))

# Chamada a função de cadastro
# Recebe o retorno do teto de gastos e qtde de destinos
teto, qtde = cadastro()

# Chamada a função de destinos
# Passa a quantidade de destinos por parâmetro
# E recebe o total de dias como retorno
totaldias = destinos(qtde)

# Chamada a função de gasto_diario
# Passa o teto de gastos e total de dias por parâmetro
gasto_diario(teto, totaldias)