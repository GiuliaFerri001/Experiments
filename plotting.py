import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 4 * np.pi, 500)
y1 = np.cos(t) 
y2 = np.cos(t) * np.exp(-0.2 * t)

fig, ax = plt.subplots()
ax.plot(t, y1, label='cosine')
ax.plot(t, y2, label='damped cosine')
ax.set_xlabel('t')
ax.set_ylabel('amplitude')
ax.set_title('Sine and Cosine Functions')
ax.legend()
plt.savefig("damped_cosine.pdf")
plt.show()