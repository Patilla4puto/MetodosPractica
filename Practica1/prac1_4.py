import numpy as np
def convergencia(e,x_k,x_k1):
    i=0
    conv = True
    while(i<len(x_k) and conv):
        if(abs(x_k[i]-x_k1[i])> e):
            conv = False
        i+=1
    return conv

def jacobi(A,b,x_0,e):
    x_k1 = np.copy(x_0) + 1
    x_k = np.copy(x_0)
    k=1

    while (not convergencia(e, x_k1, x_k)):
        x_k1 = np.copy(x_k)

        for i in range(len(x_0)):
            aux = b[i]
            for j in range(len(x_0)):
                if (j != i):
                    aux -= A[i, j] * x_k1[j]
            x_k[i] = aux/A[i,i]
        print(k,":",x_k)
        k+=1
    return x_k

def Gauss_Seidel(A,b,x_0,e):
    x_k1 = np.copy(x_0)+1
    k=1
    x_k= np.copy(x_0)
    while(not convergencia(e,x_k1,x_k)):

        x_k1=np.copy(x_k)

        for i in range(len(x_0)):
            aux = b[i]
            for j  in range(len(x_0)):
                if(j != i):
                    aux -=A[i,j]*x_k[j]
            x_k[i]=aux/A[i,i]
        print(k,":",x_k)
        k+=1

    return x_k

A = np.array([[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])
b= np.array([7.85,-19.3,71.4])
x_0 = np.zeros(3)
print("********Apartado 1**********")
print("Sol:",Gauss_Seidel(A,b,x_0,1e-1))
print("Sol:",jacobi(A,b,x_0,1e-1),"\n")
A = np.array([[5,2,-1,1],[1,7,3,-1],[-1,4,9,2],[1,-1,1,4]])
b =np.array([12,2,1,3])
x_0 = np.zeros(4)
print("********Apartado 2**********")
print("Sol:",Gauss_Seidel(A,b,x_0,1e-1))
print("Sol:",jacobi(A,b,x_0,1e-1))

