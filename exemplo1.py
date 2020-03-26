# Na Prática, Indrodução ã Lógica de Programação e ambiente Python
# Programa de auxílio ao calculo do preço de custo e preço final

# v_couro é o valor do couro para fabricação unitária
v_couro = float (input('Digite o valor de COURO:'))

# v_solado é o valor do solado para fabricação unitária
v_solado = float (input('Digite o valor do SOLADO:'))

# v_cordoes é o valor de cordões e ilhoses para fabricação unitária
v_cordoes = float (input('Digite o valor de CORDÕES E ILHOSES:'))

# v_insumos é o valor dos insumos para fabricação unitária
v_insumos = float (input('Digite o valor de INSUMOS:'))

# v_MaoObra é o valor de mão de obra para fabricação unitária
v_MaoObra = float (input('Digite o valor da MÃO DE OBRA:'))

# v_marketing é o valor do marketing e propaganda dividido pela produção
v_marketing = float (input('Digite o valor de MARKETING:'))

# v_vendas é o valor do custo de vendas dividido pela produção
v_vendas = float (input('Digite o valor dos CUSTOS DE VENDA:'))

# Calculo do preço de custo
preco_custo = (v_couro*0.30) + (v_solado*0.20) + (v_cordoes*0.05) + (v_insumos*0.05) + (v_MaoObra*0.20) + (v_marketing*0.10) + (v_vendas*0.10)
print ('O preço de custo unitário deste modelo de sapato é:' ,preco_custo)

# Calculando o preço final

# Calculando o preço adicionando o lucro do fabricante
preco_lucro = preco_custo*1.30

# Calculando o preço adicionando perdas de capital
preco_perda = preco_lucro*1.15

# Calculando o preço adicionando impostos federais
preco_impostos_fed = preco_perda*1.15

# Calculando o preço adicionando da margem de vendas
preco_venda = preco_impostos_fed*1.25

# Calculando o preço adicionando impostos estaduais e municipais
preco_impostos_est= preco_venda*1.30

# Preço final, acrescido de todos os impostos e margens de lucro
preco_final = preco_impostos_est
print('O preço final ao consumidor deste modelo de sapato é:' ,preco_final)
