import numpy as np
import math
k = 1
N = 100
TOL = 0.05
x1 = 0
x2 = 0
x3 = 0
def g_func(m1,m2,m3):
    return  pow((10.0*m1-2*m2*m2+m2-2*m3-5.0),2)+pow((8*m2*m2+4*m3*m3-9),2)+pow((8*m2*m3+4),2)
while (k<=N):
    g1 = g_func(x1,x2,x3)
    F = np.array([10.0*x1-2*x2*x2+x2-2*x3-5.0,8*x2*x2+4*x3*x3-9,8*x2*x3+4])
    J = np.array([[10.0,1.0-4*x2,-2.0],[0.0,16.0*x2,8.0*x3],[0.0,8.0*x3,8.0*x2]])
    z = 2*np.dot((J.T),F)
    z0 = math.sqrt(np.dot(z,z.T))
    
    if (z0 == 0):
        print("Zero gradient!")
        print(x1," ",x2," ",x3)
        break
    
    z = z/z0
    a1 = 0
    a3 = 1
    g3 = g_func(x1-a3*z[0],x2-a3*z[1],x3-a3*z[2])

    while(g3>=g1):
        a3 = a3/2
        g3 = g_func(x1-a3*z[0],x2-a3*z[1],x3-a3*z[2])

    a2 = a3/2
    g2 = g_func(x1-a2*z[0],x2-a2*z[1],x3-a2*z[2])

    h1 = (g2-g1)/a2
    h2 = (g3-g2)/(a3-a2)
    h3 = (h2-h1)/a3

    a0 = 0.5*(a2-h1/h3)
    g0 = g_func(x1-a0*z[0],x2-a0*z[1],x3-a0*z[2])

    if (g0>g3):
        a = a0
    else:
        a = a0
    g = g_func(x1-a*z[0],x2-a*z[1],x3-a*z[2])
    x1 = x1 - a*z[0]
    x2 = x2 - a*z[1]
    x3 = x3 - a*z[2]

    if (abs(g-g1)<TOL):
        print("x1 = ",x1)
        print("x2 = ",x2)
        print("x3 = ",x3)
        break
    k+=1
