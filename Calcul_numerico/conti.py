
from decimal import getcontext
getcontext().prec = 10


print(decimal)
lista = list(str(num))


lista_int = []
lista_dec = []
i = 0

while lista[i] != '.':
    lista_int.append(str(lista[i]))
    print(lista_int)
    i += 1

for x in lista:
    if x not in lista_int:
        lista_dec.append(x)

lista_dec.pop(0)
print(lista_dec)

#Consigo converter float em 2 listas, uma para inteiro e outra para decimal.
#Agora preciso traduzir as listas para números, de números para binários
