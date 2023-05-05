import math
import numpy as np

p1 = input("digite o ponto inicial x;y da raiz 1: ")
p2 = input("digite o ponto inicial x;y da raiz 2: ")
p3 = input("digite o ponto inicial x;y da raiz 3: ")
p4 = input("digite o ponto inicial x;y da raiz 4: ")
# as entradas deverão ser pares de pontos, separados por ";".
# exemplo: (1.21;1)

coord1 = [float(p1) for p1 in p1.split(";")]
print(coord1)
coord2 = [float(p2) for p2 in p2.split(";")]
coord3 = [float(p3) for p3 in p3.split(";")]
coord4 = [float(p4) for p4 in p4.split(";")]

list_coordenadas = coord1 + coord2 + coord3 + coord4
print(list_coordenadas)
# list_coordenadas contêm os valores em float de cada uma das coordenadas x;y
# informadas uma exatamente ao lado da outra [(1.21), (1.0), ...].

i = 0

# este vai ser o índice que indicará qual o par de ponto que estaremos analisando
# def
x = list_coordenadas[i]
y = list_coordenadas[i+1]
sin = math.sin(2*x - 1)
f = [[(x**2 + y**2)**2 - 16*x*y], [sin - 2*y**2]]
jf = [[8*x, 2*y], [3*x**2, 2*y]]

print(f)
print(jf)
# criar função para computar valor de f e jf para cada ponto
# (x,y) assumem os valores k e k+1 da list_coordenadas, para cada ponto em análise (criar uma sub lista para ser
# constantemente atualizada até a condição de parada - abandonei esta ideia)

# def
jf_aumentada = np.hstack((jf, f))
print(jf_aumentada)
maximo_valor = jf_aumentada[0][0]
k = 0
for linha in jf_aumentada:
    if linha[0] > maximo_valor:
        maximo_valor = linha[0]
        k += 1
        print(k)
    else:
        maximo_valor = jf_aumentada[0][0]
print(maximo_valor)

if k == 0:
    multiplicador = jf_aumentada[1][0]/jf_aumentada[0][0]
    for j in range(3):
        jf_aumentada[1][j] -= multiplicador*jf_aumentada[0][j]
# k == 0 implica que o maior valor está na primeira linha.
# k != 0 implica que o maior valor está na segunda linha. Neste caso,
# queremos permutar L1 com L2

else:
    jf_aumentada[0], jf_aumentada[1] = jf_aumentada[1], jf_aumentada[0]
    # Permutar as linhas
    multiplicador = jf_aumentada[0][0] / jf_aumentada[1][0]
    for j in range(3):
        jf_aumentada[1][j] -= multiplicador * jf_aumentada[0][j]

print(jf_aumentada)

# criar função para resolver matriz triangular superior por método regressivo
termos_indendentes = jf_aumentada[:, -1]
matriz_triang_sup = jf_aumentada[:, :-1]
print(termos_indendentes)
print(matriz_triang_sup)

n = len(termos_indendentes)

# criando um vetor de zeros para armazenar os valores das incógnitas
conj_resolvido = np.zeros(n)

for i in range(n-1, -1, -1):
    conj_resolvido[i] = (termos_indendentes[i] - np.dot(matriz_triang_sup[i, i+1:], conj_resolvido[i+1:])) / matriz_triang_sup[i, i]

print(conj_resolvido)

# criar condições de parada em relação a um máximo de iteraçõs Kmax, com a precisão de 10^-6 do valor de f(X) e de x
