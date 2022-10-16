from sympy.solvers import solve

from sympy import *
from sympy import functions
from sympy.plotting import plot
import math
x = Symbol('x')
def bissecion(f,x0,x1,e):
    x_new = (x1-x0)/2 +x0
    n = math.ceil(math.log((x1-x0)/e)/math.log(2))
    for _ in range(n):
        if Abs(x0-x1)< e:
            return x_new
        elif f.subs(x,x_new)* f.subs(x,x0) > 0:
            x0 = x_new
            x_new = (x1-x0)/2 +x0
        elif f.subs(x,x_new)* f.subs(x,x1) > 0:
            x1 = x_new
            x_new = (x1 - x0) / 2 + x0

    return x_new
def newtonRa(f,x0):
    derivada =diff(f,x)
    for _ in range(100):
        if (abs(f.subs(x,x0))<=0.00001):
            break
        x0 =x0-N(f.subs(x,x0)/derivada.subs(x,x0))
    return x0
f =x*sin(1/2*x**2)+exp(-x)
plot(f,(x,0,10))
#print(bissecion(f,2,3,0.0001))
print(newtonRa(f,1))
