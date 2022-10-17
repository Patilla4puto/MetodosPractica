#import matplotlib.pyplot as plt
import numpy
import numpy as np
from sympy import *
import math
from sympy.plotting import plot

x = Symbol('x')

#1.- FÓRMULAS RECTANGULARES
def fRectanguloExtIzdo(f,a,b):
    i = N(integrate(f,(x,a,b)))
    sol = N(f.subs(x,a)*(b-a))
    return sol, abs(sol-i)/i
def fRectanguloExtDcho(f,a,b):
    i = N(integrate(f,(x,a,b)))
    sol = N(f.subs(x,b)*(b-a))
    return [sol, abs(sol - i) / i]
def fRectanguloMedio(f,a,b):
    i = N(integrate(f,(x,a,b)))
    sol = N(f.subs(x,(a+b)/2)*(b-a) * (b - a))
    return [sol, abs(sol - i) / i]

#2.- FÓRMULA DEL TRAPECIO
def fTrapecio(f,a,b):
    i = N(numpy.trapz([a, b]))
    sol = N((b-a)*(f.subs(x,a)+f.subs(x,b))/2)
    return sol, abs(sol - i) / i

#3.- FÓRMULA DE SIMPSON 1/3
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
def fMilne(f, xi):
    a = N(integrate(f, (x, xi[0], xi[4])))
    D = 90
    c = [7, 32, 12, 32, 7]
    ret = 0
    for i in range(5):
        ret += c[i] * f.subs(x, xi[i])
    sol = N(ret * (xi[4] - xi[0]) / D)
    return sol, abs(sol - a) / a

#A (NO SE A QUE EJEMPLO HACER REFERENCIA)
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


#B
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

#C
h = cos(x) - x*sin(x)
print(N(integrate(h, (x, 1, 3))))
a = 1
b = 3
for i in range(1, 100):
    x_1 = a
    x_2 = b
    sol = 0
    aux = 2**(i-1)
    inc = (x_2-x_1)/aux
    x_2 = x_1 + inc
    arr1 = []
    for j in range(aux):
        arr = np.arange(x_1, x_2 + (x_2-x_1)/4, (x_2-x_1)/4)
        x_1 = x_2
        x_2 = x_1 + inc
        s1, es1 = fMilne(h, arr)
        arr1.append(s1)
    print('It {}: {}'.format(i, sum(arr1)))
