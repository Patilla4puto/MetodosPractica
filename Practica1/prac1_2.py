#import matplotlib.pyplot as plt
import numpy
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

#A (NO SE A QUE EJEMPLO HACER REFERENCIA)

#B
f= cos(x**2-1)
a = 0
b = 2*pi
xi = [0,pi,pi*2]
print("FORMULA RECTANGULO EXTREMO DERECHO")
s1, es1 = fRectanguloExtDcho(f,a,b)
print(s1, es1)
print("FORMULA RECTANGULO EXTREMO IZQUIERDO")
s2, es2 = fRectanguloExtIzdo(f,a,b)
print(s2, es2)
print("FORMULA RECTANGULO PUNTO MEDIO")
s3, es3 = fRectanguloMedio(f,a,b)
print(s3, es3)
print("FORMULA TRAPECIO")
s4, es4 = fTrapecio(f,a,b)
print(s4, es4)
print("FORMULA SIMPSON 1/3")
s5, es5 = fSimpson(f,xi)
print(s5, es5)
