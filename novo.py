#!/usr/bin/env python

from mx.DateTime import *

Diasemana = ('segunda feira','terceira feira','quarta feira',
             'quinta feira','sexta feira','sabado','domingo')
Meses=('janeiro','fevereiro','mar','abril','maio','junho',
       'julho','agosto','setembro','outubro','novembro','dezembro')
agora = now()
aniversario =Date(1971,12,23)

mes=(agora.month-1)
diadoano=(agora.day_of_year)
diadasemana = agora.day_of_week
print 'Hoje e dia:' agora.strftime('%d/%m/%Y %H:%M:%S')
print 'Hoje e:' ,Diasemana[diadasemana]
print 'Mes:', Meses[mes]
print 'Somando-se 2 dias:', (agora + DateTimeDelta(2)).strftime('%d/%m/%Y')
print 'Somando-se 3 meses:', (agora + DateTimeDelta(90)).strftime('%d/%m/%Y')
print 'Somando-se 1 ano:', (agora + DateTimeDelta(365)).strftime('%d/%m/%Y')
idade=(agora - aniversario)
print 'Idade:', (idade.day)/365 , 'To ficando veio...'

# strftime() clase datetime %M minutos, %H horas, %y ano 2 digitos

# from datatime import datatime

# hoje = datatime.now()

# ano = hoje.strftime('%Y')
# print ('Ano:', ano)

# mes = hoje.strftime('%m')
# print ('Mês:', mes)

# dia = hoje.strftime('%d')
# print('Dia:', dia)
