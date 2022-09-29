import numpy as np
import math

from sympy import *
from matplotlib import pyplot as plt
x = symbols('x ')

def rectangulo(f,sop):
    d = sop[1]-sop[0]
    l = [f.subs({'x':sop[0]})*d,f.subs({'x':sop[1]})*d,f.subs({'x':(sop[0]+sop[1])/2})*d]
    return l

def trapecio(f,sop):
    return (sop[1]-sop[0])*(f.subs({'x':sop[0]})+f.subs({'x':sop[1]}))/2

def Simpson(f,sop):
    return(sop[1]-sop[0])*(f.subs({'x':sop[0]})+4*f.subs({'x':(sop[0]+sop[1])/2})+f.subs({'x':sop[1]}))/6

def plotRectangle(f,sop):
    nums = rectangulo(f,sop)
    sopExtnd = np.arange(sop[0],sop[1],(sop[1]-sop[0])/100)
    function = []
    for i in sopExtnd:
        function.append(f.subs({'x':i}))
    result = f.integrate((x,0,2*pi))
    plt.plot(sopExtnd,function, label ="funcion real: {}".format(float(result)))
    puntoM= float(f.subs({'x':(sop[0]+sop[1])/2}))
    plt.plot(sop,[float(f.subs({'x':sop[0]})),float(f.subs({'x':sop[0]}))],label = 'extremo izquierdo: {}'.format(float(nums[0])))
    plt.plot(sop, [float(f.subs({'x':sop[1]})),float(f.subs({'x':sop[1]}))], label='extremo derecho: {}'.format(float(nums[1])))
    plt.plot(sop, [puntoM, puntoM], label='punto medio: {}'.format(float(nums[2])))
    plt.legend()
    plt.show()

def plottrapecio(f,sop):
    num = trapecio(f,sop)
    sopExtnd = np.arange(sop[0],sop[1],(sop[1]-sop[0])/100)
    function = []
    for i in sopExtnd:
        function.append(f.subs({'x':i}))
    result = f.integrate((x,0,2*pi))
    plt.plot(sopExtnd,function, label ="funcion real: {}".format(float(result)))
    plt.fill_between(sop,[float(f.subs({'x':sop[0]})),float(f.subs({'x':sop[1]}))],label = 'Trapecio: {}'.format(float(num)),alpha =0.1)

    plt.legend()
    plt.show()

def plotSimpson(f,sop):
    num = Simpson(f, sop)
    sopExtnd = np.arange(sop[0], sop[1], (sop[1] - sop[0]) / 100)
    function = []
    for i in sopExtnd:
        function.append(f.subs({'x': i}))
    result = f.integrate((x, 0, 2 * pi))
    plt.plot(sopExtnd, function, label="funcion real: {}".format(float(result)))

    plt.plot(sop, [float(f.subs({'x': sop[0]})), float(f.subs({'x': sop[1]}))],
             label='Simpson: {}'.format(float(num)))

    plt.legend()
    plt.show()

f = cos(x**2-1)
interval = [0, 2*math.pi]
plotRectangle(f,interval)
plottrapecio(f,interval)
plotSimpson(f,interval)