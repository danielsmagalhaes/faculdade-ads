from datetime import date
dataAtual = date.today()

def obterLimite():
    nomeVendedor = 'Daniel Sampaio Magalhães'
    print ('\n\nOlá, está é a Nemesis Store! Seja bem-vindo! Me chamo', nomeVendedor, 'e vou te ajudar hoje.')
    print ('Vamos precisar de alguns dados seu para realizar sua análise de crédito, tudo bem?')
    cargoAtual = input ('\nPara comerçarmos, qual seu cargo na empresa em que trabalha atualmente? ')
    salarioAtual = float(input ('Humm, certo! e qual seu salário? '))
    anoNascimento = int(input ('E por último, qual o ano em que você nasceu? (ex: 1900): '))
    print ('\nVamos ver se está tudo certo, ok?')
    print ('\nSeu cargo atual é: ', cargoAtual, '\nSeu salário é de: ', salarioAtual, '\nVocê nasceu em: ', anoNascimento)
    anoAtual = dataAtual.year
    idadeCliente = anoAtual - int(anoNascimento)
    print ('Sua idade é:', idadeCliente, 'anos')
    limiteCliente = (salarioAtual * (idadeCliente / 1000)) + 100
    print ('\nSegundo nosso sistema, você poderá gastar em nossa loja R$', limiteCliente)
    
    return limiteCliente, nomeVendedor, idadeCliente

def verificarProduto(obterLimite):

    itens = int(input('Quantos produtos gostaria de comprar? '))
    precoTotal = 0
    for quantidadeProduto in range(itens):

        print('\n=== Produto {} ==='.format(quantidadeProduto + 1))
        produto = input('Qual o produto que você quer comprar? ')
        preco = float(input('E qual seu valor do {}? '.format(produto)))

        precoTotal = precoTotal + preco

        print ('Resta R$', limiteCliente - precoTotal, 'do seu limte.')

    print()
    
    if precoTotal <= limiteCliente * 0.60:
        print('Liberado!')
    elif precoTotal > limiteCliente * 0.60 and precoTotal <= limiteCliente * 0.90:
        print('Liberado ao parcelar em até 2 vezes.')
    elif precoTotal > limiteCliente * 0.90 and precoTotal <= limiteCliente * 100:
        print('Liberado ao parcelar em 3 ou mais vezes.')
    else:
        print('Bloqueado, escolha um produto de menor valor.')
    
    quantidadeLetrasNome = len(nomeVendedor)
    if precoTotal <= quantidadeLetrasNome or precoTotal <= idadeCliente:
        print('\nParabéns, você ganhou um desconto de 6%!')
        print('O valor a ser pago já com o desconto é: R$', precoTotal - precoTotal * 0.06)
        print('\n\nObrigado, volte sempre!\n\n')
    else:
        print('\n\nObrigado, volte sempre!\n\n')

    return precoTotal


limiteCliente, nomeVendedor, idadeCliente = obterLimite()

precoTotal = verificarProduto(obterLimite)