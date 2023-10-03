import matplotlib.pyplot as plt
import numpy as np

nday = 2500
dt = 1 / 60
beta = 1.1 * (1 / 50)
gamma = 1 / 480

S = np.zeros(nday)
I = np.zeros(nday)
R = np.zeros(nday)

t = np.linspace(0, 100, nday)

I[0] = 0.1
S[0] = 1 - I[0]


for i in range(nday - 1):
    S[i+1] = S[i] - beta * (S[i] * I[i])
    I[i+1] = I[i] + beta * (S[i] * I[i]) - gamma * I[i]
    R[i+1] = R[i] + gamma * I[i]


plt.plot(t, I, color='red', label='infectious')
plt.plot(t, S, color='orange', label='suspicious')
plt.plot(t, R, color='black', label='recovered')

plt.title("case: I(0) = 100")

plt.ylabel('percentage')
plt.xlabel('time')

plt.legend()
plt.show()


