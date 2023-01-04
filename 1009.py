nome = input()
salariofx = float(input())
venda = float(input())
comissao = 0.15 * venda
calc = comissao + salariofx
print(f'TOTAL = {calc:.2f}')