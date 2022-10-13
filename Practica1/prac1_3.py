import sympy
import math

x = sympy.symbols('x')

#1.- MÉTODO BISECCION
def metodo_Biseccion(f,a,b,epsilon):#f es la funcion, a es el punto a la izda y b el punto a la derecha (importante f(a) y f(b) deben ser de signo opuesto)
    x_m = (a+b)/2
    if(abs(f.subs(x,x_m)) < epsilon):
        return x_m
    if(f.subs(x,x_m)*f.subs(x,a) > 0):
        return metodo_Biseccion(f,x_m,b,epsilon)
    else:
        return metodo_Biseccion(f,a,x_m,epsilon)

#1.- MÉTODO NEWTON-RAPHSON
def metodo_NewtonRaphson(f,x_m,epsilon):#f es la funcion, a es el punto a la izda y b el punto a la derecha (importante f(a) y f(b) deben ser de signo opuesto)
    
    if(abs(f.subs(x,x_m)) < epsilon):
        return x_m
    else:
        f_x = sympy.diff(f,x)
        x_Nuevo = x_m - (f.subs(x,x_m)/f_x.subs(x,x_m))
        #print(sympy.N(f.subs(x,x_Nuevo)))
        return metodo_NewtonRaphson(f,x_Nuevo,epsilon)







f = x * sympy.sin(0.5*x**2) + sympy.exp(-x)
print(sympy.N(metodo_NewtonRaphson(f,0,0.00001))) #Si pones 0 parece que no converge, si pones 10 si, si pintas la funcion sube y baja. probablemente te de la raiz mas cercana a la derecha del punto seleccionado



