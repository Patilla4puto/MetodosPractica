import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from sympy.functions import exp

def matriz(n,h):

    n2 = int(n**2)

    A= np.zeros((n2,n2))
    b= np.zeros(n2)
    for i in range(n2):
        for j in range(n2):
            di = i//n
            if di==0 or di==n-1:
                if(i==j):

                    A[i,j]=1
            else:
                ri = i%n
                dj = j//n
                rj = j%n
                if((ri!=0.0 and ri!=n-1) and rj==ri and (di==dj-1 or di == dj+1  )):

                    A[i,j]=1
                if (di==dj  ):
                    if((rj == 0.0 and ri==0.0)  or (ri==n-1 and rj == n-1 )   ):

                        A[i,j]=1
                    elif (ri == rj):
                        A[i,j]= -4
                        A[i,j-1]=1

                        A[i,j+1]=1
                        b[i]=-2*h**2
    return A,b
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
def elipctica(paso,start,stop):
    n = abs(start - stop) / paso + 1

    A,b = matriz(n,paso)
    xi_j= np.zeros(int(n*n))
    return(Gauss_Seidel(A,b,xi_j,1e-4),int(n))
start,stop,step =-1,1,1/4
inter = np.arange(start,stop+step,step)

mesh,n =elipctica(step,start, stop)
mesh=mesh.reshape(n,n)
X, Y = np.meshgrid(inter, inter)
print(mesh)
ax = plt.figure().add_subplot(projection='3d')
ax.plot_surface(X,Y,mesh)
plt.show()