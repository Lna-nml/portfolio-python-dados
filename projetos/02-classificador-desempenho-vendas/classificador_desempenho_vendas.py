vendedor = str(input("Nome do vendedor :"))
Valor_vendido = float(input("Qual o valor vendido pelo {}?".format(vendedor)))
valor_meta_minima = float(input("Qual o valor da meta mínima de vendas?"))
valor_meta_maxima = float(input("Qual o valor da meta máxima de vendas?"))

print("O vendedor {} vendeu R$ {:.2f}".format(vendedor, Valor_vendido))

if Valor_vendido >= valor_meta_maxima:
    print("Parabéns! O vendedor {} atingiu a meta máxima de vendas!".format(vendedor))
elif Valor_vendido >= valor_meta_minima:
    print("O vendedor {} atingiu a meta mínima de vendas.".format(vendedor))
else:
    print("Infelizmente o vendedor {} não atingiu a meta mínima de vendas, que era de R$ {:.2f}".format(vendedor, valor_meta_minima))