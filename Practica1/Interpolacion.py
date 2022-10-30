import numpy as np
import math
import matplotlib

# Las librerías anteriores se usan para el tratamiento de arrays y operaciones matemáticas simples. La librería simpy es la que utilizamos para cálculo simbólico
from sympy import *
from sympy.plotting import plot

# Definimos las variables que usamos
x = symbols('x ')

# Función para calcular los polinomios base de Lagrange. Recibe como parámetro una lista de puntos y devuelve la lista de polinomios asociado a dicha lista
def polinomiosLagrange (list):
    result = [] # Lista resultado polinomios
    for i in range(len(list)):
        l_i =  1 # Definimos L_i como la identidad, para luego ir haciendo el producto
        for j in range(len(list) ):
            if j == i : # Evitamos el caso del sumatorio i == j
                continue
            l_i = l_i*(x-list[j])/(list[i]-list[j]) # En el resto de casos, multiplicamos lo que llevásemos en L_i por la (x - x_j)/(x_i - x_j)
        result.append(l_i)
    return result

# Función para calcular el polinomio interpolador, dada la lista de puntos y la función a aproximar como parámetro. Devuelve el polimio interpolador
def polinomiosInterpoladores(list_x,f):
    p_Lagrange = polinomiosLagrange(list_x) # Llamamos a la función para calcular los polinomios base
    p_inter_n =0 # Definimos el polinomio interpolador como la identidad para ir sumando
    for i in range(len(list_x)):
        p_inter_n  += f.subs({'x':list_x[i]})*p_Lagrange[i] # f.subs(x: list_x[i]) es f(x_i), y lo multplicamos por p_Lagrange[i], que es L_i
    return p_inter_n

# Función para pintar los polinomios base de Lagrange
def plotPolLagrange(interval):
    polinomios_L = polinomiosLagrange(interval) # Obetenemos los polinomios base
    for i in polinomios_L:
        print(N(i))
    plot = compoundFunctions(polinomios_L,interval) # Llamamos a la función auxiliar para pintarlo correctamente
    plot.show() # Pintamos

# Función para pintar el polinomio interpolador
def plotPolInter(interval,func):
    polinomios_Int = polinomiosInterpoladores(interval,func) #Obetenmos los polinomios interpladores de con func y el intervalo de puntos
    compoundFunctions([func,polinomios_Int],interval).show()


# Esta función es auxiliar. La usamos para poder pintar dos funciones a la vez
def compoundFunctions(list,interval):
    plots =[] # Los gráficos a pintar
    for e in list:
        plots.append(plot(e,(x,interval[0],interval[-1]), show = False)) # Por cada elemento que queremos pintar, lo pintamos con la var x entre a y b
    first = plots[0]
    plots.remove(first)
    for e in plots:
        first.extend(e)
    return first


if __name__ == '__main__':
    # Ejercicio ejemplo, primera parte con dos puntos x_0 = 0, x_1 = pi/4
    plotPolLagrange([0,math.pi/4])
    plotPolInter([0,math.pi/4],sin(3*x))

    # Ejercicio ejemplo, segunda parte con tres puntos x_0 = 0, x_1 = pi/8, x_2 = pi/4
    plotPolLagrange([0, math.pi/8, math.pi/4])
    plotPolInter([0, math.pi/8, math.pi/4], sin(3 * x))

    # Definimos los puntos equidistantes en el intervalo (0, 2) para 2, 3 y 4 puntos
    interval = np.arange(0,2,1)
    interval2 =np.arange(0,2,2/3)
    interval3 = np.arange(0,2,1/2)
    # Definimos la función que nos piden
    f = exp(-x)+cos(4*x/math.pi)

    # Lo hacemos con dos puntos
    plotPolLagrange(interval)
    plotPolInter(interval,f)

    # Lo hacemos con 3 puntos
    plotPolLagrange(interval2)
    plotPolInter(interval2,f)

    # Lo hacemos con 4 puntos
    plotPolLagrange(interval3)
    plotPolInter(interval3,f)
