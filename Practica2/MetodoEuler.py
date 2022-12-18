import numpy as np
from sympy import *
import matplotlib.pyplot as plt
x= symbols('x')
y= symbols('y')

u= symbols('u')
v= symbols('v')

def eulerImplicito(start,stop,step,f,y0):
    sop = np.arange(start, stop + step, step)
    y_list = [y0]
    for i in range(len(sop)-1 ):
        y_n1 = y_list[-1] + step * f.subs({'x': sop[i+1]})
        resolve = y-y_n1
        y_list.append(solve(resolve,y)[0])
    return (y_list,sop)
def eulerExplicito(start,stop,step,f,y0):
    sop = np.arange(start,stop+step,step)
    y_list=[y0]
    for i in range(len(sop)-1):
        y_n1=y_list[-1]+step*f.subs({'x':sop[i],'y':y_list[-1]})
        y_list.append(y_n1)
    return(y_list,sop)

def eulerExplicito2Orden(start,stop,step, fu, fv,u0, v0):
    sop = np.arange(start,stop+step-0.001,step)
    u_list=[u0]
    v_list=[v0]
    for i in range(len(sop)-1):
        u_n1=u_list[-1]+step*fu.subs({'x':sop[i],'u':u_list[-1], 'v': v_list[-1]})
        v_n1 = v_list[-1] + step * fv.subs({'x': sop[i], 'u': u_list[-1], 'v': v_list[-1]})
        u_list.append(u_n1)
        v_list.append(v_n1)
    return(u_list, v_list ,sop)

def rungeKuta2(start,stop,step,f,y_0,a1):
    a2= 1-a1
    p1= 0.5/a2
    q11= 0.5/a2
    sop = np.arange(start,stop+step,step)
    y_sol =[y_0]
    for i in range(len(sop) - 1):
        k1= f.subs({'x':sop[i],'y':y_sol[-1]})
        k2= f.subs({'x':sop[i] +p1*step,'y':y_sol[-1]+q11*k1*step})
        y_n1 = y_sol[-1] + (a1*k1+a2*k2)*step
        y_sol.append(y_n1)
    return y_sol
def rungeKuta3(start,stop,step,f,y_0):
    sop = np.arange(start, stop + step, step)
    p1=1/2
    q21=-1
    y_sol = [y_0]
    for i in range(len(sop) - 1):
        k1= f.subs({'x':sop[i],'y':y_sol[-1]})
        k2= f.subs({'x':sop[i]+step/2,'y':y_sol[-1]+(k1*step)/2})
        k3= f.subs({'x':sop[i]+step,'y':y_sol[-1]-k1*step+2*k2*step})
        y_n1= y_sol[-1]+1/6*(k1+4*k2+k3)*step
        y_sol.append(y_n1)
    return y_sol
def rungeKuta4(start, stop, step, f, y_0):
    sop = np.arange(start, stop + step, step)
    y_sol = [y_0]
    for i in range(len(sop) - 1):
        k1 = f.subs({'x': sop[i], 'y': y_sol[-1]})
        k2 = f.subs({'x': sop[i] + step / 2, 'y': y_sol[-1] + (k1 * step) / 2})
        k3 = f.subs({'x': sop[i] + step/2, 'y': y_sol[-1] + k2*step/2})
        k4= f.subs({'x': sop[i] + step, 'y': y_sol[-1] + k3*step})
        y_n1 = y_sol[-1] + (1/6 * k1 + 1/3 * k2 + 1/3 * k3 + 1/6 * k4) * step
        y_sol.append(y_n1)
    return y_sol

if __name__ == '__main__':
    f = y-x**2+1
    expl=eulerExplicito(0,1,0.2,f,0.5)

    imp=eulerImplicito(0,1,0.2,f,0.5)

    g= (x+1)**2-0.5*exp(x)
    real = [g.subs({'x':t}) for t in [0, 0.2, 0.4, 0.6, 0.8, 1]]

    plt.plot(expl[1],expl[0],label="explicito")
    plt.plot(imp[1],imp[0],label="implicito")
    plt.plot(np.arange(0,1.2,0.2),real,label="real")
    plt.legend()
    plt.show()
    h = -2*x**3+12*x**2-20*x+8.5
    h_s=-0.5*x**4+4*x**3-10*x**2+8.5*x+1
    rungeHeun = rungeKuta2(0,1,0.5,h,1,1/2)
    rungePm = rungeKuta2(0,1,0.5,h,1,0)
    rungeR = rungeKuta2(0,1,0.5,h,1,1/3)
    l =[0,0.5,1]
    real2=[h_s.subs({'x':t}) for t in l]
    plt.plot(l,rungeHeun,label="Heun")
    plt.plot(l,rungePm,label="Punto Medio")
    plt.plot(l,rungeR,label="Ralston")

    plt.plot(l,real2,label="real")
    plt.legend()
    plt.show()
    k=y-x**2+1
    for step in [0.5,0.2,0.1,0.05,0.01]:
        l = np.arange(0,1+step,step)

        r3 = rungeKuta3(0,1,step,k,1/2)
        r4 = rungeKuta4(0,1,step,k,1/2)
        plt.plot(l,r3, label = "Runge-Kutta 3")
        plt.plot(l, r4, label="Runge-Kutta 4")
        plt.title("Runge-kutta(step ={})".format(step))
        plt.legend()
        plt.show()

    # Una vez hecha la transformación que sabemos para pasar de orden 2 a 2 de orden 1 (apuntes Rodri o Tián), tenemos lo siguiente
    # hacemos Euler explícito tal que
    M = 10
    B = 50
    k = 200
    u_0 = 0
    v_0 = 1
    f_u = v
    f_v = (-1/M)*(B*abs(v)*v+k*u)

    u_sol, v_sol, sop = eulerExplicito2Orden(0, 0.1, 0.05, f_u, f_v, u_0, v_0)
    plt.plot(sop, u_sol, label='u')
    plt.plot(sop, v_sol, label='u\'')
    plt.title("EDO de orden 2 por Euler Explícito")
    plt.legend()
    plt.show()
    u_sol_ant, v_sol_ant, sop = eulerExplicito2Orden(0, 0.1, 1/90, f_u, f_v, u_0, v_0)
    err = []
    print(u_sol_ant, v_sol_ant, sop)
    plt.plot(sop, u_sol_ant, label='u')
    plt.plot(sop, v_sol_ant, label='u\'')
    plt.title("EDO de orden 2 por Euler Explícito con step: {}".format(1 / 90))
    plt.legend()
    plt.show()
    for i in range(100, 150, 10):
        u_sol, v_sol, sop = eulerExplicito2Orden(0, 0.1, 1/i, f_u, f_v, u_0, v_0)
        print(u_sol, v_sol, sop)
        err.append(abs(u_sol_ant[1] - u_sol[1]))
        u_sol_ant = u_sol
        plt.plot(sop, u_sol, label='u')
        plt.plot(sop, v_sol, label='u\'')
        plt.title("EDO de orden 2 por Euler Explícito con step: {}".format(1/i))
        plt.legend()
        plt.show()
    print(err)
    plt.plot([1, 2, 3, 4, 5], err)
    plt.title("Estudio de la convergencia")
    plt.legend()
    plt.show()




