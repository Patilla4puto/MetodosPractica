#import matplotlib.pyplot as plt
import numpy
import numpy as np
from sympy import *
import math
from sympy.plotting import plot

x = Symbol('x')

#1.- FÓRMULAS RECTANGULARES
"""
    Estas tres fórmulas funcionan igual. Pasamos como parámetro la función que queremos aproximar (para obtener f(x)),
    y a y b como valores inferior y superior del intervalo, respectivamente. Dentro de la función calculamos el valor real
    de la integral (con N(integrate(...))) y la solución que damos con el método del rectángulo. Después, cada método devuelve
    la solución dada con dicho método, y el error relativo
"""
def fRectanguloExtIzdo(f,a,b):
    i = N(integrate(f,(x,a,b)))
    sol = N(f.subs(x,a)*(b-a))
    return sol, abs(sol-i)/i
def fRectanguloExtDcho(f,a,b):
    i = N(integrate(f,(x,a,b)))
    sol = N(f.subs(x,b)*(b-a))
    return sol, abs(sol - i) / i
def fRectanguloMedio(f,a,b):
    i = N(integrate(f,(x,a,b)))
    sol = N(f.subs(x,(a+b)/2)*(b-a))
    return sol, abs(sol - i) / i

#2.- FÓRMULA DEL TRAPECIO
"""
    Este método es análogo a los del rectángulo. Nos pasan como parámetros la función f, y los límites inferior y superior del intervalo.
    Dentro de la misma, en vez de calcular la integral de la función, utilizamos la función trapz (que es análoga a la de Matlab), porque 
    hemos pensado que era lo que se pedía en este apartado, y comparamos los valoras de dicha función con los que obtenemos nosotros usando
    el error relativo
"""
def fTrapecio(f,a,b):
    i = N(numpy.trapz([a, b]))
    sol = N((b-a)*(f.subs(x,a)+f.subs(x,b))/2)
    return sol, abs(sol - i) / i

#3.- FÓRMULA DE SIMPSON 1/3
"""
    Esta función recibe como parámetro la función f y x_i, que es la ristra de 3 puntos que vamos a usar. Dentro de la misma definimos D = 6 (como
    en teoría) y c, que es el array de coeficientes que vamos a usar para calcular la suma en el for
"""
def fSimpson(f,xi):  #xi es el conjunto de puntos (3) [x0,x1,x2]
    a = N(integrate(f, (x, xi[0], xi[2])))
    D = 6
    c = [1,4,1]
    ret = 0
    for i in range(3):
        ret += c[i]*f.subs(x,xi[i])
    sol = N(ret*(xi[2]-xi[0])/D)
    return sol, abs(sol-a) / a

#4.- FÓRMULA DE MILNE
"""
    Esta función recibe como parámetro la función f y x_i, que es la ristra de 5 puntos que vamos a usar. Dentro de la misma definimos D = 90 (como
    en teoría) y c, que es el array de coeficientes que vamos a usar para calcular la suma en el for
"""
def fMilne(f, xi):
    a = N(integrate(f, (x, xi[0], xi[4])))
    D = 90
    c = [7, 32, 12, 32, 7]
    ret = 0
    for i in range(5):
        ret += c[i] * f.subs(x, xi[i])
    sol = N(ret * (xi[4] - xi[0]) / D)
    return sol, abs(sol - a) / a

if __name__ == "__main__":
    #A -> definimos la función (g) y corremos los métodos definidos arriba
    g = x**3 - 2*x**2 + 1
    a = 0
    b = 2
    xi = [0, 1, 2]
    print("A) FORMULA RECTANGULO EXTREMO DERECHO")
    s1, es1 = fRectanguloExtDcho(g,a,b)
    print(s1, es1)
    print("A) FORMULA RECTANGULO EXTREMO IZQUIERDO")
    s2, es2 = fRectanguloExtIzdo(g,a,b)
    print(s2, es2)
    print("A) FORMULA RECTANGULO PUNTO MEDIO")
    s3, es3 = fRectanguloMedio(g,a,b)
    print(s3, es3)
    print("A) FORMULA TRAPECIO")
    s4, es4 = fTrapecio(g,a,b)
    print(s4, es4)
    print("A) FORMULA SIMPSON 1/3")
    s5, es5 = fSimpson(g,xi)
    print(s5, es5)
    print("a) VALOR EXACTO DE LA INTEGRAL")
    print(N(integrate(g, (x, a, b))))

    #B -> definimos la función (f) y corremos los métodos definidos arriba
    f= cos(x**2-1)
    a = 0
    b = 2*pi
    xi = [0,pi,pi*2]
    print("B) FORMULA RECTANGULO EXTREMO DERECHO")
    s1, es1 = fRectanguloExtDcho(f,a,b)
    print(s1, es1)
    print("B) FORMULA RECTANGULO EXTREMO IZQUIERDO")
    s2, es2 = fRectanguloExtIzdo(f,a,b)
    print(s2, es2)
    print("B) FORMULA RECTANGULO PUNTO MEDIO")
    s3, es3 = fRectanguloMedio(f,a,b)
    print(s3, es3)
    print("B) FORMULA TRAPECIO")
    s4, es4 = fTrapecio(f,a,b)
    print(s4, es4)
    print("B) FORMULA SIMPSON 1/3")
    s5, es5 = fSimpson(f,xi)
    print(s5, es5)

    #C -> definimos la función (h) y corremos el método definido arriba, iterando para obtener los distintos subintervalos
    h = cos(x) - x*sin(x)
    print("PREGUNTA OPTATIVA MILNE")
    a = 1
    b = 3
    for i in range(1, 7):
        x_1 = a
        x_2 = b
        aux = 2**(i-1)
        inc = (x_2-x_1)/aux
        x_2 = x_1 + inc
        sol = []
        for j in range(aux):
            arr = np.arange(x_1, x_2 + (x_2-x_1)/4, (x_2-x_1)/4)
            x_1 = x_2
            x_2 = x_1 + inc
            s1, es1 = fMilne(h, arr)
            sol.append(s1)
        print('It {}: solución {} error {}'.format(i, sum(sol), N(integrate(h, (x, 1, 3))) - sum(sol)))
