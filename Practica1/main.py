import numpy as np
import math
import matplotlib.pyplot as plt
def polinomiosLagrange (x,list):
    result = []
    for i in range(len(list)):
        l_i =  1
        for j in range(len(list) ):
            if j == i :
                continue
            l_i = l_i*(x-list[j])/(list[i]-list[j])
        result.append(l_i)
    return result
def polinomiosInterpoladores(x,list_x,f):
    p_Lagrange = polinomiosLagrange(x,list_x)
    p_inter_n =0
    for i in range(len(list_x)):
        p_inter_n  += f(list_x[i])*p_Lagrange[i]
    return p_inter_n
interval = [0,math.pi/4]
def plotPolLagrange():
    polinomios =[]
    for i in interval:
        polinomios.append([])
    x_axis =np.arange(0,math.pi/4,math.pi/400)
    for i in x_axis:
        polinomios_L = polinomiosLagrange(i,interval)
        for i in range(len(polinomios_L)):
            polinomios[i].append(polinomios_L[i])
    for i,e in enumerate(polinomios):
        plt.plot(x_axis,e,label="{}".format(i))
def plotPolInter():
    polinomios_Int = []
    x_axis = np.arange(0, math.pi / 4, math.pi / 400)
    for i in x_axis:
        polinomios_Int.append(polinomiosInterpoladores(i, interval,lambda x:math.sin(3*x)))
    print(polinomios_Int)
    plt.plot(x_axis, polinomios_Int, label="Polinomio Interpolador")
plotPolInter()
plt.show()
print(polinomiosInterpoladores(math.pi/8,[0,math.pi/4],lambda x:math.sin(3*x)))