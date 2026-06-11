import numpy as np
angles = np.linspace(0, 2 * np.pi, 50_000)
y = np.sin(angles)**2 + 0.5 * np.cos(2 * angles)
result_np = np.sum(y)
print(result_np)