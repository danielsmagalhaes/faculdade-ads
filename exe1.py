# Qual roupa devo sair?
print()
print ('Olá, vamos saber qual roupa escolher para sair hoje?\n')
temp = int(input('Qual é a temperatura agora? '))
if temp < 7:
    print ('Congelando!')
elif temp < 10:
        print ('Frio!')
elif temp > 26:
        print ('Ótimo!')
else:
    print ('Use o que achar mais confortavel.')
