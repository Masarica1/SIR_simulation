import matplotlib.pyplot as plt
import numpy as np

nday = 100000
dt = 1 / 60
beta = 0.8 * (1 / 35)
gamma = 1 / 480

S = np.zeros(nday)
I = np.zeros(nday)
R = np.zeros(nday)

t = np.arange(nday)

I[0] = 0.001
S[0] = 1 - I[0]


for i in range(nday - 1):
    S[i+1] = S[i] - beta * (S[i] * I[i]) * dt
    I[i+1] = I[i] + beta * (S[i] * I[i]) * dt - gamma * I[i] * dt
    R[i+1] = R[i] + gamma * I[i] * dt


plt.plot(t, I)
plt.plot(t, S, color='orange')
plt.plot(t, R, color='black')

plt.show()
print(max(I))


