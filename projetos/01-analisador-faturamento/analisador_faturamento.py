#Metas semanal e vendas díarias
meta_semanal = float(input("Determine a meta semanal: "))
vendas_seg = float(input("Qual o valor de vendas de segunda-feira?"))
vendas_ter = float(input("Qual o valor de vendas de terça-feira?"))
vendas_quarta = float(input("Qual o valor de vendas de quarta-feira?"))
vendas_quinta = float(input("Qual o valor de vendas de quinta-feira?"))
vendas_sexta = float(input("Qual o valor de vendas de sexta-feira?"))

total_semanal = vendas_seg + vendas_ter + vendas_quarta + vendas_quinta + vendas_sexta
metas_mensal = float(input("Determine a meta mensal: "))
meta_atingida = float(input("Qual o valor de vendas do mês?"))

if total_semanal >= meta_semanal:
    print("Parabéns! A meta foi atingida com sucesso! O total vendido foi de R$ {:.2f}".format(total_semanal))
else:
    print("Infelizmente a meta não foi atingida. O total vendido foi de R$ {:.2f}".format(total_semanal))
if meta_atingida >= metas_mensal:
    print("Parabéns! A meta mensal foi atingida com sucesso! O total vendido foi de R$ {:.2f}".format(meta_atingida))
else:
    print("Infelizmente a meta mensal não foi atingida. O total vendido foi de R$ {:.2f}".format(meta_atingida))
    
print("Analise completa do faturamento semanal e mensal")


                              
    
