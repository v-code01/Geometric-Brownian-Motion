import numpy as np
import matplotlib.pyplot as plt
mu = 0.1
n = 1000
t = 1
m = 100
s0 = 100
sigma = 0.3
dt = t/n
St = np.exp(
    (mu - sigma ** 2 / 2) * dt
    + sigma * np.random.normal(0, np.sqrt(dt), size=(m, n)).T
)
St = np.vstack([np.ones(m), St])
St = s0 * St.cumprod(axis=0)
time = np.linspace(0, t, n+1)
tt = np.full(shape=(m, n+1), fill_value=time).T
plt.plot(tt, St)
plt.xlabel("Years $(t)$")
plt.ylabel("Stock Price $(S_t)$")
plt.show()
