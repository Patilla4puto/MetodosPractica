import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from sympy.functions import exp

x= symbols('x')

def convergencia(e,x_k,x_k1):
    i=0
    conv = True
    while(i<len(x_k) and conv):
        if(abs(x_k[i]-x_k1[i])> e):
            conv = False
        i+=1
    return conv

def Gauss_Seidel(A,b,x_0,e):
    #De momento  es igual a jacobi
    x_k1 = np.copy(x_0)+2*e
    k=1
    x_k= np.copy(x_0)
    while(not convergencia(e,x_k1,x_k)):
        x_k1=np.copy(x_k)
        for i in range(len(x_0)):
            aux = b[i]
            for j  in range(len(x_0)):
                if(j != i):
                    aux -=A[i,j]*x_k[j]#En vez de usar el vector de la iteracion anterior
                    #usamos los valores del de la itearacion actual que depende de la fila
                    # en la que estemos habran sido ya modificados
            x_k[i]=aux/A[i,i]
        k+=1

    return x_k


# coef = [D, v, q]
def condicionesContorno(star, stop, step, coef, f_x, u_0, u_n):
    alpha = -coef[0]/step**2-coef[1]/(2*step)
    beta = 2*coef[0]/step**2+coef[2]
    gamma =  -coef[0]/step**2+coef[1]/(2*step)
    inter = np.arange(star,stop+step,step)
    if (len(inter) == 3):
        f_1 = f_x.subs({'x':inter[1]})
        u_1= (f_1 -alpha*u_0-gamma*u_n)/beta
        return [u_0,u_1,u_n],inter
    else:
        n = len(inter)
        A = np.zeros((n,n))
        b = []
        for i in range(n):
            if(i == 0 or i == n-1):
                A[i,i]=1
                if(i==0):
                    b.append(u_0)
                else:
                    b.append(u_n)
            else:
                A[i,i] = beta
                A[i,i-1] = alpha
                A[i,i+1] = gamma
                b.append(f_x.subs({'x':inter[i]}))
        u_arr = np.zeros(n)
        return Gauss_Seidel(A, b, u_arr, 1/1000), inter

if __name__ == '__main__':

    #Ejercicio 1
    coef = [1, 1, 0]
    u_0 = 0
    u_n = 1
    f_x = 0*x
    sol_aprox, inter = condicionesContorno(0, 1, 0.5, coef, f_x, u_0, u_n)
    f_real = (exp(x)-1)/(exp(1)-1)
    sol_real = [0, N(f_real.subs({'x':0.5})), 1]
    error_relativo = abs(sol_aprox[1] - sol_real[1])
    print('Error: {}'.format(error_relativo))
    plt.plot(inter,sol_real,label = "real")
    plt.plot(inter, sol_aprox, label="aproximada")
    plt.legend()
    plt.show()
    '''for i in range(10):
        step = 1/(i+3)
        sol_aprox, inter = difFinitas(0, 1, step, coef, f_x, u_0, u_n)
        sol_real = [N(f_real.subs({'x': j})) for j in np.arange(0, 1 + step, step)]
        plt.plot(inter, sol_real, label="real")
        plt.plot(inter, sol_aprox, label="aproximada")
        plt.legend()
        plt.show()'''

    #Ejercicio 2
    coef = [-1, 0, -0.01]
    f_x = -0.01*20 + 0*x
    t_0 = 40
    t_n = 200
    for i in range(10):
        step = 10/(i+2)
        sol_aprox, inter = condicionesContorno(0, 10, step, coef, f_x, t_0, t_n)
        print(sol_aprox, inter)
        plt.plot(inter, sol_aprox, label="aproximada")
        plt.legend()
        plt.show()

 
