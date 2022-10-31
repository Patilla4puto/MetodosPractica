import numpy as np
#METODO QUE ANALIZA SI SE CUMPLE LA CONDICION DE CONVERGENCIA
"""
Metodo auxiliar que recibe un error de convergencia (e), el vector de esta
iteracion (x_k)y el vector de la iteracion anterior(x_k1), y devulve un 
booleano a true si se da la condicion de convergencia 
"""
def convergencia(e,x_k,x_k1):
    i=0
    conv = True
    while(i<len(x_k) and conv):
        if(abs(x_k[i]-x_k1[i])> e):
            conv = False
        i+=1
    return conv

#METODO DE JACOBI
"""
Metodo que recibe una matriz con los coeficientes de tamaño nxn (A), un vector v
de tamaño n con los resultados de las ecuaciones(b), un vector de tamaño n de
soluciones iniciales (x_0) y el error de convergencia(e), y devuelve el vector
de soluciones finales
"""
def jacobi(A,b,x_0,e):
    x_k1 = np.copy(x_0) + 2*e #Copiamos el vector x_0 y sumamos a todos sus elementos
    #2e para que el bucle se ejecute al menos una vez (python no tiene repeat until)
    x_k = np.copy(x_0) #Se copia un vector con los mismos elementos
    k=1 #Variable que alamcena el numero de la iteración

    while (not convergencia(e, x_k1, x_k)):#Mientras no haya convergencia
        x_k1 = np.copy(x_k)#Copiamos los valores de x_k en para sustituir los de la
        #iteracion anterior

        for i in range(len(x_0)): # recorrido de las filas
            aux = b[i] #variable acumulativa del cambio que va a sufrir la x de la fila i
            for j in range(len(x_0)): # recorrido en columnas
                if (j != i):
                    aux -= A[i, j] * x_k1[j]#Acumulamos el resultado de A_i,j * x_j
                    # de la iteracion anterior
            x_k[i] = aux/A[i,i] #Dividimos por el elemento de la diagonal
        print(k,":",x_k)
        k+=1
    return x_k
#METODO DE Gauss_Seidel
"""
Metodo que recibe una matriz con los coeficientes de tamaño nxn (A), un vector v
de tamaño n con los resultados de las ecuaciones(b), un vector de tamaño n de
soluciones iniciales (x_0) y el error de convergencia(e), y devuelve el vector
de soluciones finales
"""
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
        print(k,":",x_k)
        k+=1

    return x_k

A = np.array([[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])#creacion de la matriz de coeficientes
b= np.array([7.85,-19.3,71.4])#Resultados de las ecuaciones
x_0 = np.zeros(3) #Vector de soluciones inicial(vector nulo de tamaño 3)
print("********Apartado 1**********")
print("Sol:",Gauss_Seidel(A,b,x_0,1e-1))
print("Sol:",jacobi(A,b,x_0,1e-1),"\n")
A = np.array([[5,2,-1,1],[1,7,3,-1],[-1,4,9,2],[1,-1,1,4]])#creacion de la matriz de coeficientes
b =np.array([12,2,1,3])#Resultados de las ecuaciones
x_0 = np.zeros(4)#Vector de soluciones inicial
print("********Apartado 2**********")
print("Sol:",Gauss_Seidel(A,b,x_0,1e-1))
print("Sol:",jacobi(A,b,x_0,1e-1))

