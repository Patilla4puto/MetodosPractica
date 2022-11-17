import numpy as np
from sympy import *
x= symbols('x')
y= symbols('y')
def eulerImplicito(start,stop,step,f,y0):
    sop = np.arange(start, stop + step, step)
    y_list = [y0]
    for i in range(len(sop)-1 ):
        y_n1 = y_list[-1] + step * f.subs({'x': sop[i+1]})
        resolve = y-y_n1
        y_list.append(solve(resolve,y)[0])
    return (y_list)
def eulerExplicito(start,stop,step,f,y0):
    sop = np.arange(start,stop+step,step)
    y_list=[y0]
    for i in range(len(sop)-1):
        y_n1=y_list[-1]+step*f.subs({'x':sop[i],'y':y_list[-1]})
        y_list.append(y_n1)
    return(y_list)
f = y-x**2+1

print(eulerExplicito(0,1,0.2,f,0.5))
print(eulerImplicito(0,1,0.2,f,0.5))
