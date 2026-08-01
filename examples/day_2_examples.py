import matplotlib.pyplot as plt
import numpy as np


plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

#example1
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('sin - line')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example1')
plt.clf()

#example2
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y,
         color='purple',
         linestyle='dashdot',
         linewidth=2,
         marker='o',
         markersize=5,
         markerfacecolor='yellow',
         markeredgecolor='red',
         markeredgewidth=1.5,  
         label='sin(x)')
plt.legend()
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example2')
plt.clf()

#example3
x=np.random.rand(100)
y=np.random.rand(100)

plt.scatter(x, y)
plt.title('산점도')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example3')
plt.clf()

#example4
x=np.random.rand(50)
y=np.random.rand(50)
colors=np.random.rand(50)
sizes = 1000*np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis', edgecolors='red', linewidths=2)
plt.title('산점도-올랜덤')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example4')
plt.clf()

#example5
data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.title('히스토그램 정규분포')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example5')
plt.clf()

#example6
data = np.random.randn(1000)
plt.hist(data, bins=30, range=(-3, 3), density=True, alpha=0.7, color='g', edgecolor='black', label='레이블이 제대로 안 보이는데요??')
from scipy.stats import norm
x = np.linspace(-3, 3, 1000)
y = norm.pdf(x, 0, 1)
plt.plot(x, y, 'r--', label='정규분포')
plt.legend()
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example6')
plt.clf()

#example7
l = ['1', '2', '3', '4', '5']
v = [7, 3, 6, 2, 5]

plt.bar(l, v)
plt.title('막대기')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example7')
plt.clf()

#example8
l = ['1', '2', '3', '4', '5']
v = [7, 3, 6, 2, 5]

plt.bar(l, v, width = 0.4, bottom=2, align='center', color='lightblue', edgecolor='blue')
plt.title('막대기-변형')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example8')
plt.clf()

#example9
l = ['1', '2', '3', '4']
v = [15, 30, 45, 10]

plt.pie(v, labels=l, autopct='%1.1f%%')
plt.title('파이')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example9')
plt.clf()

#example10
l = ['1', '2', '3', '4']
v = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0) 
fig1, ax1 = plt.subplots()
ax1.pie(v, explode=explode, labels=l, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')  
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example10')
plt.clf()

#example11
data = np.random.randn(1000)
plt.boxplot(data)
plt.title('Box Plot')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example11')
plt.clf()

#example12
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
bp = ax.boxplot(data, patch_artist = True, notch = True, vert = 0)
plt.title("Customized box plot")
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example12')
plt.clf()

#example13
x = np.linspace(0, 10, 10)
y = x ** 2
errors = np.random.rand(10) * 5
plt.errorbar(x, y, yerr=errors, fmt='o')
plt.title('Error Bar')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example13')
plt.clf()

#example14
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='.k', ecolor='lightgray', elinewidth=3, capsize=0)
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example14')
plt.clf()

#example15
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contourf(X, Y, Z, cmap='viridis')
plt.title('Contour Plot')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example15')
plt.clf()

#example16
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)
plt.contourf(X, Y, Z, levels=20, cmap='RdGy')
plt.title('Contour Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example16')
plt.clf()


from mpl_toolkits.mplot3d import Axes3D

#example17
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title('3D Plot')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example17')
plt.clf()

#example18
x = np.linspace(-6, 6, 100)
y = np.linspace(-6, 6, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_title('Surface Plot')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2-example18')
plt.clf()
