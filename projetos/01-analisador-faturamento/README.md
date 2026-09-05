# Analisador de faturamento semanal e mensal

Primeiro projeto do meu portfólio de Python para dados. O programa recebe metas e valores de vendas, calcula o faturamento semanal e avalia separadamente os resultados semanal e mensal.

## Problema resolvido

Uma pessoa precisa informar as vendas dos cinco dias úteis, comparar o total com uma meta semanal e também comparar as vendas do mês com uma meta mensal.

## Conceitos praticados

- Variáveis e operações matemáticas
- Entrada de dados com `input()`
- Conversão de texto com `float()`
- Formatação monetária com `.format()` e `:.2f`
- Condições com `if` e `else`
- Comparações com `>=`
- Condições combinadas com `and`
- Indentação e decisões independentes

## Evolução durante o projeto

A primeira versão colocava a análise mensal dentro do `else` semanal. Depois, uma tentativa combinou as duas metas usando `and`, o que não identificava corretamente os cenários mistos. A versão atual usa decisões independentes para informar o resultado de cada período.

## Como executar

No terminal, entre nesta pasta e execute:

```text
python analisador_faturamento.py
```

Depois, informe as metas e os valores solicitados usando ponto para separar as casas decimais.

## Cenários usados para conferir o resultado

1. Meta semanal e meta mensal atingidas.
2. Meta semanal atingida e meta mensal não atingida.
3. Meta semanal não atingida e meta mensal atingida.
4. Meta semanal e meta mensal não atingidas.

