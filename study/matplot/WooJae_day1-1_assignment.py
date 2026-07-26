import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 이우재
# 1-1 2번 문제

x = np.linspace(0, 2*np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label='sin(x)')
plt.plot(x,y2, label='cos(x)')

plt.title('sin and cos graph')
plt.xlabel('x value')
plt.ylabel('y value')
plt.legend()

#plt.savefig("result_q2.png", format='png')
plt.clf()

# 1-1 3번 문제

df=pd.DataFrame({'X_val':x,'Sin_val': y1, 'Cos_val': y2})
print(df.head())
vis1=df['X_val']
vis2=df['Sin_val']
plt.plot(vis1, vis2, label='sin(x)')
plt.title('sin graph')
plt.savefig("result_q3.png", format='png')


