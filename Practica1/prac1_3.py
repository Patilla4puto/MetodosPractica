import sympy
from sympy.plotting import plot
import numpy
import matplotlib.pyplot as plt
import math

x = sympy.symbols('x')


# 1.- MÉTODO BISECCION
def metodo_Biseccion(f, a, b, epsilon,
                     ite=0):  # f es la funcion, a es el punto a la izda y b el punto a la derecha (importante f(a) y f(b) deben ser de signo opuesto)
    x_m = (a + b) / 2
    if (abs(b - a) < epsilon):
        return x_m, ite
    if (f.subs(x, x_m) == 0):
        return x_m, ite
    elif (f.subs(x, x_m) * f.subs(x, a) > 0):
        return metodo_Biseccion(f, x_m, b, epsilon, ite + 1)
    else:
        return metodo_Biseccion(f, a, x_m, epsilon, ite + 1)


# 1.- MÉTODO NEWTON-RAPHSON
def metodo_NewtonRaphson(f, x_m, epsilon, ite=1, limit=-1):
    # Derivamos la funcion
    f_x = sympy.diff(f, x)
    x_Nuevo = x_m - (f.subs(x, x_m) / f_x.subs(x, x_m))  # CALCULO DEL NUEVO

    # SE CUMPLE CRITERIO DE PARADA
    if ((abs(x_m - x_Nuevo) <= epsilon) or limit == 0):
        return x_Nuevo, ite
    # EN EL CASO DE QUE NO TENGAMOS ITERACIONES LIMITADAS
    else:
        if (limit < 0):
            return metodo_NewtonRaphson(f, sympy.N(x_Nuevo), epsilon, ite + 1)
        else:  # SI LAS TENEMOS POR CADA ITERACIONES RESTAMOS UNA
            return metodo_NewtonRaphson(f, sympy.N(x_Nuevo), epsilon, ite + 1, limit - 1)


def metodo_Secante(f, x_n, x_m, epsilon, ite=0):
    if (abs(x_n - x_m) < epsilon):
        return x_n, ite
    else:
        x_Nuevo = x_n - f.subs(x, x_n) * ((x_n - x_m) / (f.subs(x, x_n) - f.subs(x, x_m)))
        return metodo_Secante(f, x_Nuevo, x_n, epsilon, ite + 1)


# 3.- METODO DE CONVERGENCIA DE NEWTON-RAPSHON
"""
Metodo auxiliar que recibe la funcion a analizar (f),el punto de partida (x_m), el epsilon
para comprobar convergencia(epsilon), el limite de iteraciones(limit) y la raiz real de la 
función y devuelve el resultado del metodo NEWTON-RAPSHON, el error absoluto del metodo y
las constantes de convergencia con ordenes del 1 al 3 aplicando el metodo hasta la iteracion limit 
"""


def conv_NewtonRapshon(f, x_m, epsilon, limit, x_0):
    if (limit > 0):
        # SI limit NO ES 0,APLICAMOS NEWTON_RAPSON HASTA LA ITERACION limit(n)
        aux = metodo_NewtonRaphson(f, x_m, epsilon, limit=limit)
        """
        Haciendo limit =limit, basicamente estamos especificando que la variable
        limit independientemente de donde se declarese en la cabecera de la funcion
         metodo_NewtonRaphson tenga valor limit
        """
    else:
        # SI limit ES CERO, ENTONCES X_N=x_m
        aux = [x_m]
    # VALOR DEVUELTO POR NEWTON_RAPSON EN LA ITERACION limit(n+1)
    aux1 = metodo_NewtonRaphson(f, x_m, epsilon, limit=limit + 1)

    # ERRORES E_n y E_n+1
    e_n = aux[0] - x_0
    e_n1 = aux1[0] - x_0

    k = []
    # ALMACENAMOS LOS K SEGUN la k
    for i in range(1, 4):
        k.append(abs(e_n1) / (abs(e_n) ** i)) #|E_n+1|/|E_n|^i
    return aux[0], e_n, k


# PRUEBAS PARTE 1
# BISECCION
g = x + sympy.cos(x)
resultado = metodo_Biseccion(g, -2, 10, 0.0001)
raiz = resultado[0]
# print(resultado)
# print(g.subs(x,-2))
# print((g.subs(x,10)))
# print((g.subs(x,raiz)))
p1 = sympy.plot(g, (x, -5, 10), line_color='red', show=False)
# p1.show()


h = x - x ** 2
resultado = metodo_Biseccion(h, 0.4, 2, 0.01)
# print(resultado)
raiz = resultado[0]
# print(h.subs(x,0.5))
# print((h.subs(x,2)))
# print((h.subs(x,raiz)))
# p1 = sympy.plot(h,(x, -2, 4),line_color='red', show=False)
# p1.show()

# NEWTON-RAPHSON
resultado = metodo_NewtonRaphson(g, -2, 0.0001)
# print(resultado)
resultado = metodo_NewtonRaphson(h, 0.4, 0.01)
# print(resultado)


print("******1******")
f = x * sympy.sin(0.5 * x ** 2) + sympy.exp(-x)
# p1 = sympy.plot(f,(x, -2, 10),line_color='red', show=False)
# p1.show()
print("BISECCION")
resultado = metodo_Biseccion(f, 0, 3, 0.01)
print("sol:{}  (n:{})".format(sympy.N(resultado[0]), resultado[1]))
resultado = metodo_Biseccion(f, 3, 4, 0.01)
print("sol:{}  (n:{})".format(sympy.N(resultado[0]), resultado[1]))
resultado = metodo_Biseccion(f, 4, 5, 0.01)
print("sol:{}  (n:{})".format(sympy.N(resultado[0]), resultado[1]))

print("NEWTON-RAPHSON")
resultado = metodo_NewtonRaphson(f, 0, 0.01)
print("sol:{}  (n:{})".format(sympy.N(resultado[0]), resultado[1]))
resultado = metodo_NewtonRaphson(f, 3, 0.01)
print("sol:{}  (n:{})".format(sympy.N(resultado[0]), resultado[1]))
resultado = metodo_NewtonRaphson(f, 4, 0.01)
print("sol:{}  (n:{})".format(sympy.N(resultado[0]), resultado[1]))
resultado = metodo_NewtonRaphson(f, 5, 0.01)
print("sol:{}  (n:{})".format(sympy.N(resultado[0]), resultado[1]))

print('epsilon distintos')
resultado = metodo_NewtonRaphson(f, 3, 0.0001)
print("sol:{}  (n:{})".format(sympy.N(resultado[0]), resultado[1]))
resultado = metodo_NewtonRaphson(f, 3, 0.02)
print("sol:{}  (n:{})".format(sympy.N(resultado[0]), resultado[1]))

print("******2.1******")
# 2.1
f = sympy.sin(x) - 0.3 * sympy.exp(x)
# p1 = sympy.plot(f,(x, -2, 4),line_color='red', show=False)
# p1.show()
# 2.1 Bisección
aux = metodo_Biseccion(f, 1, 4, 0.01)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
# 2.1  Newton-Rapshon
aux = metodo_NewtonRaphson(f, 1, 0.01)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
print("******2.2******")
# 2.2
f = sympy.sqrt(x) - sympy.cos(x)
# p1 = sympy.plot(f,(x, 0.1, 5),line_color='red', show=False)
# p1.show()
print("a)")
# 2.2 a)biseccion
aux = metodo_Biseccion(f, 0, 4, 0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
# 2.2 a)Newton-Rapshon
aux = metodo_NewtonRaphson(f, 1, 0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
# 2.2 b)biseccion
print("b)")
aux = metodo_Biseccion(f, 0.5, 1, 0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
# 2.2 b)Newton-Rapshon
aux = metodo_NewtonRaphson(f, 0.5, 0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))

# 2.3
print("******2.3******")
f = 2 * x ** 3 - 11.7 * x ** 2 + 17.7 * x - 5
# p1 = sympy.plot(f,(x, 0, 5),line_color='red', show=False)
# p1.show()
print("a)")
# 2.3 a)biseccion (0,1)
aux = metodo_Biseccion(f, 0, 1, 0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
# 2.3 a)biseccion (1,3)
aux = metodo_Biseccion(f, 1, 3, 0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
# 2.3 a)biseccion (3,5)
aux = metodo_Biseccion(f, 3, 5, 0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
print("b)")
# 2.3 b)Newton-Rapshon 0.5
aux = metodo_NewtonRaphson(f, 0.5, 10 ** (-10))
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
# 2.3 b)Newton-Rapshon 1.5
aux = metodo_NewtonRaphson(f, 1.5, 10 ** (-10))
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
# 2.3 b)Newton-Rapshon 4
aux = metodo_NewtonRaphson(f, 4, 10 ** (-10))
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))

# 2.4
print("******2.4******")
f = sympy.exp(1 / 2 * x) + 5 * x - 5
#p1 = sympy.plot(f, (x, 0, 5), line_color='red', show=False)
#p1.show()
# 2.4 a)biseccion
print("a)")
aux = metodo_Biseccion(f, 0, 4, 0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
# 2.4 b)Newton-Raphson
print("b)")
aux = metodo_NewtonRaphson(f, 1, 0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]), aux[1]))
print("******2.5******")
f = x ** 2 + x + 3
f_1 = f.diff()
print(f_1)
p1 = sympy.plot(f, (x, -5, 5), line_color='red', show=False)
p1.show()
p1 = sympy.plot(f_1, (x, -5, 5), line_color='red', show=False)
p1.show()
# 2.5 a)biseccion
print("a)")
aux = metodo_Biseccion(f_1, -2, 2, 0.001)
print("sol:{},{}  (n:{})".format(sympy.N(aux[0]), f.subs(x, sympy.N(aux[0])), aux[1]))
# 2.5 b)Newton-Raphson
print("b)")
aux = metodo_NewtonRaphson(f_1, 0, 0.001)
print("sol:{},{}  (n:{})".format(sympy.N(aux[0]), f.subs(x, sympy.N(aux[0])), aux[1]))
# 2.5 c) Secante
aux = metodo_Secante(f_1, -1.5, 1.5, 0.001)
print("sol:{},{}  (n:{})".format(sympy.N(aux[0]), f.subs(x, sympy.N(aux[0])), aux[1]))

f = x ** 3 - 3 * x + 2

# TABLA DE LA CONVERGENCIA DE NEWTON RAPSHON SEGUN EL NUMERO DE ITERACIONES
for i in range(0, 5):  # BUCLE  sobre (0,1,2,3,4) MARCANDO EL NUMERO DE ITERACIONES A REALIZAR
    print("********n={}********".format(i))
    aux = conv_NewtonRapshon(f, -3, 1e-6, i, -2)  # METODO QUE DEVUELVE LOS VALORES DE K yE_N

    print("sol: {} , E_N: {}  ".format(sympy.N(aux[0]), sympy.N(aux[1])))  # RESULTADO EN LA ITERACION i
    # DEL METODO NEWTON-RAPSHON Y EL ERROR COMETIDO

    for j, e in enumerate(aux[2]):  # ITERACION POR VALOR E INDICE SOBRE UN ARRAY CON LAS K
        # SEGUN EL VALOR DE k
        print("k{}:  {}".format(j+1, sympy.N(e)))

# CALCULO DE LA K REAL PARA EL METODO NEWTON-RAPSHON
f1 = sympy.diff(f, x)
print("K (with k=2):", abs(1 / 2 * sympy.diff(f1, x).subs(x, -2) / f1.subs(x, -2)))
