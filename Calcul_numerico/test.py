###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Cupons de Desconto I
# Nome: Maria Isabell Heiduk
# RA: 247918
###################################################
# Leitura de dados
X1 = int(input())    # desconto do cupom 1
Z1 = int(input())    # limite mínimo para ter o desconto
X2 = int(input())    # desconto do cupom 2 (em %)
Z2 = int(input())    # máximo desconto que pode ter
X3 = int(input())    # desconto do cupom 3 (em %)
Z3 = int(input())    # limite mínimo para ter o desconto
n = int(input())     # quantidade de compras
listaC = []          # lista com as compras       
listaD1 = []         # lista com descontos CUPOM 1
listaD2 = []
listaD3 = []

Q = 0
while Q < n:
    C = int(input())
    listaC.append(C)
    Q = Q + 1

# Cálculo da melhor atribuição de cupons
for i in range(len(listaC)):
    for j in range(len(listaC)):
        for k in range(len(listaC)):
            if i != j and i != k and j != k:
                if listaC[i] > Z1:
                    desconto_1 = X1
                    listaD1.append(desconto_1)
                else: 
                    desconto_1 = 0
                    listaD1.append(desconto_1)
                if (X2/100) * listaC[j] >= Z2:
                    desconto_2 = Z2
                    listaD2.append(desconto_2)
                elif (X2/100) * listaC[j] < Z2:
                    desconto_2 = (X2/100) * listaC[j]
                    listaD2.append(desconto_2)
                if listaC[k] >= Z3:
                    desconto_3 = (X3/100) * listaC[k]
                    listaD3.append(desconto_3)
                else:
                    desconto_3 = 0
                    listaD3.append(desconto_3)

maximo = 0 
p = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            somadescontos = listaD1[i] + listaD2[j] + listaD3[k]
            if i != j and i != k and k != j:
                somadescontos = listaD1[i] + listaD2[j] + listaD3[k]
                if somadescontos > maximo:
                    maximo = somadescontos
                    I = i + 1
                    J = j + 1
                    K = k + 1

# Impressão da resposta
print("Cupom 1:", I)
print("Cupom 2:", J)
print("Cupom 3:", K)