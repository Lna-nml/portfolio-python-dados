# Classificador de desempenho de vendas

Segundo projeto do meu portfólio de Python para dados. O programa recebe o nome de um vendedor, o valor vendido e duas metas, classificando o desempenho em uma de três faixas.

## Problema resolvido

Uma empresa precisa diferenciar vendas abaixo da meta, vendas que alcançaram a meta mínima e vendas que alcançaram a meta máxima.

## Conceitos praticados

- Entrada de texto e números com `input()` e `float()`
- Preenchimento de mensagens com `.format()`
- Formatação monetária com `:.2f`
- Comparações com `>=`
- Três caminhos de decisão com `if`, `elif` e `else`
- Ordem das condições e prioridade das classificações

## Decisão principal do projeto

A meta máxima é verificada primeiro. Se essa condição for verdadeira, a sequência termina. Quando ela é falsa, o programa testa a meta mínima com `elif`. O `else` representa os valores abaixo das duas metas.

## Como executar

No terminal, entre nesta pasta e execute:

```text
python classificador_desempenho_vendas.py
```

Informe o nome do vendedor, o valor vendido, a meta mínima e a meta máxima.

## Cenários usados para conferir o resultado

1. Venda abaixo da meta mínima.
2. Venda exatamente igual à meta mínima.
3. Venda entre a meta mínima e a máxima.
4. Venda exatamente igual à meta máxima.
5. Venda acima da meta máxima.

