import numpy as np
from sympy import *
import matplotlib.pyplot as plt
x= symbols('x')
y= symbols('y')
def eulerImplicito(start,stop,step,f,y0):
    sop = np.arange(start, stop + step, step)
    y_list = [y0]
    for i in range(len(sop)-1 ):
        y_n1 = y_list[-1] + step * f.subs({'x': sop[i+1]})
        resolve = y-y_n1
        y_list.append(solve(resolve,y)[0])
    return (y_list,sop)
def eulerExplicito(start,stop,step,f,y0):
    sop = np.arange(start,stop+step,step)
    y_list=[y0]
    for i in range(len(sop)-1):
        y_n1=y_list[-1]+step*f.subs({'x':sop[i],'y':y_list[-1]})
        y_list.append(y_n1)
    return(y_list,sop)
f = y-x**2+1
expl=eulerExplicito(0,1,0.2,f,0.5)
print(expl)
imp=eulerImplicito(0,1,0.2,f,0.5)
print(imp)
g= (x+1)**2-0.5*exp(x)
real = list(map(lambda t: g.subs({'x':t}),np.arange(0,1.2,0.2)))
print(real)
fig,ax =plt.subplots(1,2)
ax[0].plot(expl[1],expl[0])
ax[0].plot(imp[1],imp[0])
aux=plot(g,(x,0,1),show=False)
ax[1].plot(aux.get_points()[0],aux.get_points()[1])

