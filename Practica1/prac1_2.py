from sympy import *
import math
x = Symbol('x')

#1.- FÓRMULAS RECTANGULARES
def fRectanguloExtIzdo(f,a,b):
    return f.subs(x,a)*(b-a)
def fRectanguloExtDcho(f,a,b):
    return f.subs(x,b)*(b-a)
def fRectanguloMedio(f,a,b):
    return f.subs(x,(a+b)/2)*(b-a)

#2.- FÓRMULA DEL TRAPECIO
def fTrapecio(f,a,b):
    return (b-a)*(f.subs(x,a)+f.subs(x,b))/2

#3.- FÓRMULA DE SIMPSON 1/3
def fSimpson(f,xi):  #xi es el conjunto de puntos (3) [x0,x1,x2]
    D = 6
    c = [1,4,1]
    ret = 0
    for i in range(3):
        ret += c[i]*f.subs(x,xi[i])
    return ret*(xi[2]-xi[0])/D

#A (NO SE A QUE EJEMPLO HACER REFERENCIA)

#B
f= cos(x**2-1)
a = 0
b = math.pi*2
xi = [0,math.pi,math.pi*2]
print("FORMULA RECTANGULO EXTREMO DERECHO")
print(N(fRectanguloExtDcho(f,a,b)))
print("FORMULA RECTANGULO EXTREMO IZQUIERDO")
print(N(fRectanguloExtIzdo(f,a,b)))
print("FORMULA RECTANGULO PUNTO MEDIO")
print(N(fRectanguloMedio(f,a,b)))
print("FORMULA TRAPECIO")
print(N(fTrapecio(f,a,b)))
print("FORMULA SIMPSON 1/3")
print(N(fSimpson(f,xi)))
print("INTEGRAL CON FUNCION TRAPZ")
print(N(integrate(f,(x,a,b))))
#   QUEDAN LOS ERRORES RELATIVOS JEJE

