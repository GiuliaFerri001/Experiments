import math 
import time
import numpy as np
angles = np.linspace(0, 2 * np.pi, 50_000)
t0 = time.perf_counter()
y = np.sin(angles)**2 + 0.5 * np.cos(2 * angles)
t1 = time.perf_counter()
print(f"Vectorized computation took {t1 - t0:.6f} seconds.")

for x in angles:
    y = math.sin(x)**2 + 0.5 * math.cos(2 * x)
t2 = time.perf_counter()
print(f"Loop computation took {t2 - t1:.6f} seconds.")

Loop_time = t2 - t1
Vectorized_time = t1 - t0
print(f"Vectorized computation is {Loop_time / Vectorized_time:.2f} times faster than loop computation.")

