import numpy as np
A1 = np.array([[2., 1.], [1., 3.]]) # well-conditioned?
A2 = np.array([[1., 1.], [1., 1.001]]) # ill-conditioned?
b = np.array([5., 10.])
print(np.linalg.cond(A1)) 
print(np.linalg.cond(A2))
print(np.linalg.solve(A1, b))
print(np.linalg.solve(A2, b))
b2 = b + np.array([0, 0.001])
print(np.linalg.solve(A1, b2))
print(np.linalg.solve(A2, b2))

