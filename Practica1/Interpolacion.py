import numpy as np
import math

from sympy import *
from sympy.plotting import plot
x = symbols('x ')

def polinomiosLagrange (list):
    result = []

    for i in range(len(list)):
        l_i =  1
        for j in range(len(list) ):
            if j == i :
                continue

            l_i = l_i*(x-list[j])/(list[i]-list[j])
        result.append(l_i)
    return result
def polinomiosInterpoladores(list_x,f):
    p_Lagrange = polinomiosLagrange(list_x)
    p_inter_n =0
    for i in range(len(list_x)):
        p_inter_n  += f.subs({'x':list_x[i]})*p_Lagrange[i]
    return p_inter_n

def plotPolLagrange(interval):



    polinomios_L = polinomiosLagrange(interval)


    plot = compoundFunctions(polinomios_L,interval)
    plot.show()

def plotPolInter(interval,func):


    polinomios_Int = polinomiosInterpoladores( interval,sin(3*x))
    compoundFunctions([func,polinomios_Int],interval).show()

def compoundFunctions(list,interval):
    plots =[]
    for e in list:

        plots.append(plot(e,(x,interval[0],interval[-1]), show = False))
    first = plots[0]
    plots.remove(first)
    for e in plots:
        first.extend(e)
    return first


plotPolLagrange([0,math.pi/4])
plotPolInter([0,math.pi/4],sin(3*x))

interval = np.arange(0,2,1)
interval2 =np.arange(0,2,2/3)
interval3 = np.arange(0,2,1/2)
f = exp(-x)+cos(4*x/math.pi)

plotPolLagrange(interval)
plotPolInter(interval,f)

plotPolLagrange(interval2)
plotPolInter(interval2,f)

plotPolLagrange(interval3)
plotPolInter(interval3,f)
