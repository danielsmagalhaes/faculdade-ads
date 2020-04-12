from datetime import date

data_atual = date.today()

# Etapa 1
print ('\n\nOlá, esta é a Saldão Store! Seja bem-vindo! Aqui quem fala é Daniel Sampaio Magalhães')
print ('Vamos precisar de alguns dados seu para realizar sua análise de crédito, tudo bem?\n')

cargo = input ('Para comerçarmos, qual seu cargo na empresa em que trabalha atualmente? ')
salario = float(input ('Humm, certo! e qual seu salário atual? '))
ano = input('E por último, qual o ano em que você nasceu? (4 digitios): ')

print ('\nÓtimo! Vamos ver se está tudo certo, ok?')

print ('\nSeu cargo atual é:', cargo,', seu salário é de', salario, 'e você nasceu em', ano, '.')

# Etapa 2
anoAtual = data_atual.year
idade = anoAtual - int(ano)
print ('Sua idade é:' ,idade, 'anos')
limite = (salario * (idade / 1000)) + 100
print ('\nSegundo nosso sistema, você poderá gastar em nossa loja R$', limite)

# Epata 3
produto = input('\nPor favor, nos diga qual o produto que você quer comprar? ')
preco = float(input('E qual seu valor? '))

print()

if preco <= (limite * 0.60):
    print('Liberado!')
elif preco > (limite * 0.60) and preco <= (limite * 0.90):
    print('Liberado ao parcelar em até 2 vezes.')
elif preco > (limite * 0.90) and preco <= (limite * 100):
    print('Liberado ao parcelar em 3 ou mais vezes.')
else:
    print('Bloqueado.')
    print('Escolha um produto de menor valor.')

if preco <= 24 or preco <= idade:
    print('Parabéns, você ganhou um desconto de 6%!')
    print('O valor a ser pago já com o desconto é: ', (preco - preco * 0.06))
    print('\n\nObrigado, volte sempre!\n\n')
else:
    print('\n\nObrigado, volte sempre!\n\n')