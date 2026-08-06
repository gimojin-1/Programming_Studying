import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1번 문제

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x,y, label='sin(x)')
#plt.savefig("result_day2_q1_1.png")
plt.clf()
plt.plot(x,y, color='purple', linestyle='dashdot', marker='o', markerfacecolor='yellow')
#plt.savefig("result_day2_q1_2.png")
plt.clf()

# 2번 문제

x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000*np.random.rand(100)

plt.scatter(x,y)
#plt.savefig("result_day2_q2_1.png")
plt.clf()
plt.scatter(x,y,c=colors, s=sizes, alpha=0.3, cmap='viridis', edgecolors='red')
#plt.savefig("result_day2_q2_2.png")

# 3번 문제

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.savefig("result_day2_q3_1.png")
plt.clf()
plt.hist(data, bins=30, density=True, range=(-3, 3))

from scipy.stats import norm

x = np.linspace(-3,3,1000)
y = norm.pdf(x, 0, 1)
plt.plot(x, y, 'r--', label='Normal distribution')
plt.savefig("result_day2_q3_2.png")
plt.clf()

# 4번 문제 

categories = ['A','B','C','D','E']
values = [7,4,5,6,2]

plt.bar(categories, values)
plt.savefig("result_day2_q4_1.png")
plt.clf()

plt.bar(categories, values, width=0.4, bottom=2, color='lightblue', edgecolor='blue')
plt.savefig("result_day2_q4_2.png")
plt.clf()

# 5번 문제

labels=['Democrat','Republic','People power','Doubled democrat']
sizes=[10,20,40,30]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.savefig("result_day2_q5_1.png")
plt.clf()

explode=(0, 0, 0.1, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.savefig("result_day2_q5_2.png")
plt.clf()

# 6번 문제

data1 = np.random.randn(1000)

plt.boxplot(data1)
plt.savefig("result_day2_q6_1.png")
plt.clf()

data2 = [np.random.normal(0, std, 100) for std in range(1,5)]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
bp = ax.boxplot(data2, patch_artist = True, notch = True, vert = 0)
plt.savefig("result_day2_q6_2.png")
plt.clf()

# 7번 문제

x = np.linspace(0, 10, 10)
y = x**2
errors = np.random.rand(10)*5

plt.errorbar(x,y,yerr=errors, fmt='o')
plt.savefig("result_day2_q7_1.png")
plt.clf()

x = np.linspace(0,20,50)
dy = 0.8
y = np.sin(x) + dy*np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt='.k', ecolor='lightgray', elinewidth=3, capsize=0)
plt.savefig("result_day2_q7_2.png")
plt.clf()

# 8번 문제

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X**2+Y**2))

plt.contourf(X, Y, Z,cmap='viridis')
plt.savefig("result_day2_q8_1.png")
plt.clf()

Z = np.sqrt(X**2+Y**2)
plt.contour(X, Y, Z, levels=20, cmap='RdGy')
plt.savefig("result_day2_q8_2.png")
plt.clf()

# 9번 문제

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X**2+Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.savefig("result_day2_q9_1.png")
plt.clf()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
plt.savefig("result_day2_q9_2.png")













