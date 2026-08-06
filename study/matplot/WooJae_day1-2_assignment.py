import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 이우재
# 1-2 1번 문제

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label='sin(x)')
plt.plot(x,y2, label='cos(x)')

plt.title('Sin and Sos Graph')
plt.xlabel('X values')
plt.ylabel('Function values')
plt.legend()

plt.savefig("result_day1-2_q1.png")
plt.clf()

# 1-2 1번 문제

x = np.linspace(0,10,40)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x)*np.cos(x)

plt.plot(x, y1, color='red', linestyle='dashed', marker='o', label='sin(x)')
plt.plot(x, y2, color='blue', linestyle='solid', marker='s', label='cos(x)')
plt.plot(x, y3, color='green', linestyle='dashdot', marker='^', label='sin(x)*cos(x)')
plt.legend()

plt.savefig("result_day1-2_q2.png")
plt.clf()

# 1-2 3번 문제

x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x,y, label='sin(x)')
plt.title('Sin Graph with Custom Axis Limits')
plt.xlim(0,2 * np.pi)
plt.ylim(-1.5,1.5)
plt.savefig("result_day1-2_q3.png")
