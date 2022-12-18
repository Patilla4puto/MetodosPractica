import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from sympy.functions import exp

x= symbols('x')
#Copiamos el codigo de Gauss-Seidel
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


# coef = [D, v, q],
def condicionesContorno(star, stop, step, coef, f_x, u_0, u_n):
    #Obtenemos el alpha,beta , gamma y el intervalo de discretización
    alpha = -coef[0]/step**2-coef[1]/(2*step)
    beta = 2*coef[0]/step**2+coef[2]
    gamma =  -coef[0]/step**2+coef[1]/(2*step)
    inter = np.arange(star,stop+step-1/10**6,step)
    #Si tiene tamaño 3 sustituimos directamente
    if (len(inter) == 3):
        f_1 = f_x.subs({'x':inter[1]})
        u_1= (f_1 -alpha*u_0-gamma*u_n)/beta
        return [u_0,u_1,u_n],inter
    else:
        #Si no, definimos la matriz A y el vector b y les damos valores
        n = len(inter)
        A = np.zeros((n,n))
        b = []
        for i in range(n):
            #Si estamos en el primer/ultimo valor asignamos 1 a A y u_o o u_n depende en que extremos estemos
            if(i == 0 or i == n-1):
                A[i,i]=1
                if(i==0):
                    b.append(u_0)
                else:
                    b.append(u_n)
            else:
                #Por otro lado asignamos a la diagonal principal y a las secundarias los valores de alpha,betta y gamma
                A[i,i] = beta
                A[i,i-1] = alpha
                A[i,i+1] = gamma
                #Y en la misma posición añadimos a b el resultado de sustituir xi en f_x
                b.append(f_x.subs({'x':inter[i]}))
        #Inicializamos x_i
        u_arr = np.zeros(n)
        #Devolvemos el resultado de resolver el sistema A*b=u_arr
        return Gauss_Seidel(A, b, u_arr, 1/1000), inter

if __name__ == '__main__':

    #Ejercicio 1
    #Definimos los coeficientes que componen nuestro problema -D, V y q, las condiciones en los extremos y la f_x
    coef = [1, 1, 0]
    u_0 = 0
    u_n = 1
    f_x = 0*x

    # Apartado a
    sol_aprox, inter = condicionesContorno(0, 1, 0.5, coef, f_x, u_0, u_n)
    print("Solución apartado a): {}".format(sol_aprox))

    # Apartado b
    f_real = (exp(x) - 1) / (exp(1) - 1)
    sol_real = [N(f_real.subs({'x': j})) for j in np.arange(0, 1 + 0.5, 0.5)]
    print("Solución real: {}".format(sol_real))
    error_relativo = abs(sol_aprox[1] - sol_real[1]) / sol_real[1]
    print("Error relativo: {}".format(error_relativo))
    error = []
    #Realizamos pruebas con pasos de discretización más pequeños para obserbar la convergencia
    for i in range(10):
        step = 1/(i+3)
        sol_aprox, inter = condicionesContorno(0, 1, step, coef, f_x, u_0, u_n)
        sol_real = [N(f_real.subs({'x': j})) for j in np.arange(0, 1 + step-1/10**6, step)]
        error_por_punto = [abs(x - y) for x, y in zip(sol_aprox, sol_real)]
        error_relativo = sum(error_por_punto)/len(error_por_punto)
        error.append(error_relativo)
        print('Error: {}'.format(error_relativo))  # Mostramos el error relativo
        plt.plot(inter, sol_real, label="real")
        plt.plot(inter, sol_aprox, label="aproximada")
        plt.title("Iteración {} con step {}".format(i, step))
        plt.legend()
        plt.show()

    plt.plot(range(10), error)
    plt.title("Evolución del error")
    plt.legend()
    plt.show()
    #Ejercicio 2

    #COo en el anterior definimos los  coeficientes que componen nuestro problema -D, V y q, las condiciones en los extremos y la f_x
    coef = [-1, 0, -0.01]
    f_x = -0.01*20 + 0*x
    t_0 = 40
    t_n = 200
    #Ahora aplicamos la misma secuencia aplicada en el apartado anterior para diferentes valores de discretización y lo mostramos
    for i in range(10):
        step = 10/(i+2)
        sol_aprox, inter = condicionesContorno(0, 10, step, coef, f_x, t_0, t_n)

        plt.plot(inter, sol_aprox, label="aproximada")
        plt.legend()
        plt.show()
