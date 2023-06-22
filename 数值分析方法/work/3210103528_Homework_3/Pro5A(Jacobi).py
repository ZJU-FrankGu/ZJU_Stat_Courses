# Jacobi Method
import numpy as np

D = np.diag([3,6,7])
L = np.array([[0,0,0],
              [-3,0,0],
              [-3,-3,0]])
U = np.array([[0,1,-1],
              [0,0,-2],
              [0,0,0]])
M = np.dot(np.linalg.inv(D),(L+U))
b = np.array([1,0,4])
x1 = 0;x2 = 0;x3 = 0
x = np.array([x1,x2,x3])

for i in range(20):
    t = np.dot(M,x.T)+np.dot(np.linalg.inv(D),b.T)
    if (abs(max(t-x))<0.001): # 无穷范数<0.001
        x = t
        break
    else:
        x = t
print("After",i,"iterations,we get the final root: ")
print(x)