###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Cupons de Desconto I
# Nome: Maria Isabell Heiduk
# RA: 247918
###################################################
# Leitura de dados
X1 = int(input())
Z1 = int(input())
X2 = int(input())
Z2 = int(input())
X3 = int(input())
Z3 = int(input())
n = int(input())

p = 0
compras = []
possibilidades = []

# inputando lista compras
while p < n:
    compras.append(int(input()))
    p += 1
# calculando todas as combinações de compras
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                possibilidades.append([compras[i], compras[j], compras[k]])

compras_escolhidas = []
desconto_max = 0
# calculando o maior desconto possivel com o uso dos cupons
for x, y, z in possibilidades:
    desconto = 0
    # cupom 1
    if x > Z1:
        desconto += X1
    # cupom 2
    if y*X2/100 >= Z2:
        desconto += Z2

    elif y*X2/100 < Z2:
        desconto += y*X2/100
    # cupom 3
    if z > Z3:
        desconto += z*X3/100
    # desconto maximo
    if desconto_max < desconto:
        desconto_max = desconto
        compras_escolhidas = [x, y, z]

# removendo os valores de compras que ja foram encontrados
posicao1 = compras.index(compras_escolhidas[0])
compras[posicao1] = None

posicao2 = compras.index(compras_escolhidas[1])
compras[posicao2] = None

posicao3 = compras.index(compras_escolhidas[2])
compras[posicao3] = None
# output
print('Cupom 1: ', posicao1 + 1)
print('Cupom 2: ', posicao2 + 1)
print('Cupom 3: ', posicao3 + 1)
