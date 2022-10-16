import sympy
import math

x = sympy.symbols('x')

#1.- MÉTODO BISECCION
def metodo_Biseccion(f,a,b,epsilon,ite=0):#f es la funcion, a es el punto a la izda y b el punto a la derecha (importante f(a) y f(b) deben ser de signo opuesto)
    x_m = (a+b)/2
    if(abs(b-a) < epsilon):

        return x_m,ite
    if(f.subs(x,x_m)*f.subs(x,a) > 0):
        return metodo_Biseccion(f,x_m,b,epsilon,ite+1)
    else:
        return metodo_Biseccion(f,a,x_m,epsilon,ite+1)

#1.- MÉTODO NEWTON-RAPHSON
def metodo_NewtonRaphson(f,x_m,epsilon,x_n,ite=0):#f es la funcion, a es el punto a la izda y b el punto a la derecha (importante f(a) y f(b) deben ser de signo opuesto)
    
    if(abs(x_m-x_n) < epsilon):
        return x_m,ite
    else:
        f_x = sympy.diff(f,x)
        x_Nuevo = x_m - (f.subs(x,x_m)/f_x.subs(x,x_m))
        #print(sympy.N(f.subs(x,x_Nuevo)))
        return metodo_NewtonRaphson(f,x_Nuevo,epsilon,x_m,ite+1)






print("******1******")
f = x * sympy.sin(0.5*x**2) + sympy.exp(-x)
#print("sol:{}  (n:{})".format(sympy.N(metodo_NewtonRaphson(f,1,0.01,0)))) #Si pones 0 parece que no converge, si pones 10 si, si pintas la funcion sube y baja. probablemente te de la raiz mas cercana a la derecha del punto seleccionado
print("******2.1******")
#2.1
f=sympy.sin(x)-0.3*sympy.exp(x)
#2.1
aux = metodo_Biseccion(f,1,4,0.01)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
#2.1  Newton-Rapshon
aux = metodo_NewtonRaphson(f,1,0.01,2)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
print("******2.2******")
#2.2
f= sympy.sqrt(x)-sympy.cos(x)
print("a)")
#2.2 a)biseccion
aux = metodo_Biseccion(f,0,4,0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
#2.2 a)Newton-Rapshon
aux = metodo_NewtonRaphson(f,1,0.001,0)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
#2.2 b)biseccion
print("b)")
aux = metodo_Biseccion(f,0.5,1,0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
#2.2 b)Newton-Rapshon
aux = metodo_NewtonRaphson(f,0.5,0.001,0)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))

#2.3
print("******2.3******")
f=2*x**3-11.7*x**2+17.7*x-5
print("a)")
#2.3 a)biseccion (0,1)
aux = metodo_Biseccion(f,0,1,0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
#2.3 a)biseccion (1,3)
aux = metodo_Biseccion(f,1,3,0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
#2.3 a)biseccion (3,5)
aux = metodo_Biseccion(f,3,5,0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
print("b)")
#2.3 b)Newton-Rapshon 0.5
aux = metodo_NewtonRaphson(f,0.5,10**(-10),0)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
#2.3 b)Newton-Rapshon 1.5
aux = metodo_NewtonRaphson(f,1.5,10**(-10),0)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
#2.3 b)Newton-Rapshon 4
aux = metodo_NewtonRaphson(f,4,10**(-10),0)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))

#2.4
print("******2.4******")
f = sympy.exp(1/2*x)+5*x-5
#2.4 a)biseccion
print("a)")
aux = metodo_Biseccion(f,0,4,0.001)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
#2.4 b)Newton-Raphson
print("b)")
aux = metodo_NewtonRaphson(f,1,0.001,0)
print("sol:{}  (n:{})".format(sympy.N(aux[0]),aux[1]))
print("******2.5******")
f = x**2+x+3
f_1=f.diff()
print(f_1)
#2.4 a)biseccion
print("a)")
aux = metodo_Biseccion(f_1,-2,2,0.001)
print("sol:{},{}  (n:{})".format(sympy.N(aux[0]),f.subs(x,sympy.N(aux[0])),aux[1]))
#2.4 b)Newton-Raphson
print("b)")
aux = metodo_NewtonRaphson(f_1,0,0.001,1)
print("sol:{},{}  (n:{})".format(sympy.N(aux[0]),f.subs(x,sympy.N(aux[0])),aux[1]))

