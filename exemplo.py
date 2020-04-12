def calculadora():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    operacao = input('Digite a operação (+, -, *, /): ')

    resultado = num1

    if operacao == '+':
        resultado += num2
    elif operacao == '-':
        resultado -= num2
    elif operacao == '*':
        resultado *= num2
    elif operacao == '/':
        resultado /= num2
    else:
        print('Operação não reconhecida. Tente de novo!')
    print('O resultado é: %f' % resultado)