import numpy as np
from sympy import *
import matplotlib.pyplot as plt
"""
Función que nos devuelve la Matriz A y b del problema asociaso al problema eliptico que se nos plantea,
con tamaños de distretizacion nxn
"""
def matriz(n,h):
    #Inicializamos las matrices a ceros
    n2 = int(n**2)
    A= np.zeros((n2,n2))
    b= np.zeros(n2)
    for i in range(n2):
        for j in range(n2):
            di = i//n
            #Hacemos que las matrices correspondientes a las variables i= 1, i=n-1 sean diagonales
            if di==0 or di==n-1:
                if(i==j):
                    A[i,j]=1
            else:
                #Recabamos información de con que variable estamos tratando con los restos y divisores enteros de las filas y columnas
                ri = i%n
                dj = j//n
                rj = j%n
                #Damos valor a las varibles en las digonales secundarias, donde solo sus elementos diagonales con ri distinto de 0 y n-1
                #son distintos de 0
                if((ri!=0.0 and ri!=n-1) and rj==ri and (di==dj-1 or di == dj+1  )):

                    A[i,j]=1
                #Aquí nos fijamos en las submatrices de la diagonal principal
                if (di==dj ):
                    #Los elementos ri =0,n-1 los inicializamos a 1
                    if((rj == 0.0 and ri==0.0)  or (ri==n-1 and rj == n-1 )   ):
                        A[i,j]=1
                    #Aquí solo inicilizamos los elementos de la diagonal (no incluidos en la condición anterior y los de la diagonal de esa misma fila
                    elif (ri == rj):
                        A[i,j]= -4
                        A[i,j-1]=1
                        A[i,j+1]=1
                        #Aprovechamos esta condición e inicializamos la fila corresponiente de b con el valor (pues es en esta fila donde tenemos la ecuación correspondiente
                        # al problema
                        b[i]=-2*h**2
    return A,b
#Reutilizamo el codigo de Gauss-Seidel
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

# Función que devuelve el vector de los xi,j del problema eliptico que se nos pide pasandole los limites de definición y los pasos de discretización
def elipctica(paso,start,stop):

    n = abs(start - stop) / paso + 1            #Obtenemos el numero de puntos
    A,b = matriz(n,paso)                        #Obtenemos la matriz A y el vector b de la función que hemos definido al principio
    xi_j= np.zeros(int(n*n))                    #Inicializamos el vector x_i_j con 0's
    return(Gauss_Seidel(A,b,xi_j,1e-4),int(n))  #Resolvemos con Gauss-Seidel el sistema A*x_i_j=b y devolvemos el resultado
start,stop =-1,1

#Realizamos 8 pruebas con casos de discretizacion de entre 3 a 11 puntos
for step,limit in [((stop-start)/n,n) for n in range(2,11)]:
    #Aqui suele haber un error y aveces se crean intervalos de n+1 puntos, suponemos que debido a la precisión de float
    inter = np.arange(start,stop+step,step)
    #Corregimos el problema de arange
    if (len(inter)>limit):
        inter = inter[0:limit+1]

    mesh,n =elipctica(step,start, stop) #Recuperamos los puntos z y el tamaño de discretización
    #Realizamos los pasos necesarios para mostrar la gráfica
    mesh=mesh.reshape(n,n)
    X, Y = np.meshgrid(inter, inter)
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot_surface(X,Y,mesh)
    plt.show()