###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Cupons de Desconto I
# Nome: Gabriel Freitas Forlenza Gonçalves
# RA: 238324
###################################################

# Leitura de dados
x1 = int(input())
z1 = int(input())
x2 = int(input())
z2 = int(input())
x3 = int(input())
z3 = int(input())
n = int(input())

lista_compras = []

for i in range(n):
    lista_compras.append(int(input()))

# Cálculo da melhor atribuição de cupons

lista_descontos = []
desconto_max = 0
cupom1, cupom2, cupom3 = (0, 0, 0)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                desconto_total = 0
                #Condicional para cupom 1
                if lista_compras[i] > z1:
                    desconto1 = x1
                    desconto_total += desconto1
                # Condicionais para cupom 2
                if lista_compras[j]*x2/100 >= z2:
                    desconto2 = z2
                    desconto_total += desconto2

                if lista_compras[j] * x2 / 100 < z2:
                    desconto2 = lista_compras[j] * x2 / 100
                    desconto_total += desconto2
                # Condicional para cupom 3
                if lista_compras[k] > z3:
                    desconto3 = lista_compras[k] * x3 / 100
                    desconto_total += desconto3

                # atualiza o desconto máximo e os índices de compra que foram aplicados o cupom
                if desconto_total > desconto_max:
                    desconto_max = desconto_total
                    cupom1, cupom2, cupom3 = (i, j, k)

# impressão da resposta
print(f'Cupom 1: {cupom1 + 1}')
print(f'Cupom 2: {cupom2 + 1}')
print(f'Cupom 3: {cupom3 + 1}')