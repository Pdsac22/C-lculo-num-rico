from decimal import *

a = Decimal(input("digite o coeficiente a: "))
b = Decimal(input("digite o coeficiente b: "))
c = Decimal(input("digite o coeficiente c: "))

getcontext().prec = 22


def vamoai(num):

    n1 = Decimal(round(num, 0))
    n2 = Decimal(num) - Decimal(n1)
    num = Decimal(n1) + Decimal(n2)
    return num


a = vamoai(a)
b = vamoai(b)
c = vamoai(c)

delta = Decimal(b**2 - 4*a*c)

if b ** 2 > 4*a*c and a != 0:
    x1 = Decimal((-b + (delta ** Decimal(0.5)))/(2 * a))
    x2 = Decimal((-b - (delta ** Decimal(0.5)))/(2 * a))

    if x1 > x2:
        x2 = c/(a*x1)

    elif x2 > x1:
        x1 = c/(a*x2)

    print("x1: {} e x2: {}".format(x1, x2))

elif b ** 2 > 4*a*c and a == 0:
    x1 = -c/b
    print("x1: {} (equação linear)".format(x1))

elif b ** 2 == 4*a*c:
    if (a, b, c) == (0, 0, 0):
        print("Reta real")
    elif (a, b) == (0, 0) and c != 0:
        print('equação inconsistente')
    else:
        x1 = Decimal((-b + (delta ** Decimal(0.5))) / (2 * a))
        x2 = Decimal((-b - (delta ** Decimal(0.5))) / (2 * a))
        print("x1: {} e x2: {}".format(x1, x2))

elif b ** 2 < 4*a*c:
    if a != 0:
        x1 = -b/(2*a)
        x2 = x1
        x1i = ((-delta) ** (Decimal(0.5))) / (2 * a)
        x2i = -Decimal(x1i)
        print("x1: {} + {}i e x2: {} + {}i".format(x1, x1i, x2, x2i))
