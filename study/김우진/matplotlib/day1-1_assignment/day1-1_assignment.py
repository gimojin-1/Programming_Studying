import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 2*np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.savefig('result_q2.png')
plt.show()

df = pd.DataFrame({'X_val' : x, 'Sin_val' : y1, 'Cos_val' : y2})
print(df.head())

plt.plot(df['X_val'], df['Sin_val'])
plt.savefig('result_q3.png')
plt.show()