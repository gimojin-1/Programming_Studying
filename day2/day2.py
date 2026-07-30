import matplotlib.pyplot as plt
import numpy as np
#1. Line Plot (선 그래프)
#1-1. 기본 Line Plot (sin 그래프) 

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q1_1.png')
plt.clf()

#1-2. 세부 세팅 Line Plot (color='purple', linestyle='dashdot', marker='o', markerfacecolor='yellow' 등 적용) 
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, color='purple', linestyle='dashdot', marker='o', markerfacecolor='yellow', label='sin(x)')
plt.legend()
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q1_2.png')
plt.clf()

#2. Scatter Plot (산점도)

#2-1. 기본 Scatter Plot (난수 100개 점) 
x=np.random.rand(100)
y=np.random.rand(100)
plt.scatter(x, y)
plt.title('scatter')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q2_1.png')
plt.clf()


#2-2. 세부 세팅 Scatter Plot (c=colors, s=sizes, alpha=0.3, cmap='viridis', edgecolors='red') 
x=np.random.rand(100)
y=np.random.rand(100)
colors=np.random.rand(100)
sizes = 1000*np.random.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis', edgecolors='red')
plt.title('scatter')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q2_2.png')
plt.clf()

#3. Histogram (히스토그램)
#3-1. 기본 Histogram (data = np.random.randn(1000), bins=30) 
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title('histogram')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q3_1.png')
plt.clf()


#3-2. 세부 세팅 Histogram (density=True, range=(-3, 3)) + scipy.stats.norm 정규분포 곡선 겹치기 
data = np.random.randn(1000)
plt.hist(data, bins=30, range=(-3, 3), density=True, alpha=0.7, color='g', edgecolor='black', label='레이블이 제대로 안 보이는데요??')
from scipy.stats import norm
x = np.linspace(-3, 3, 1000)
y = norm.pdf(x, 0, 1)
plt.plot(x, y, 'r--', label='standard')
plt.legend()
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q3_2.png')
plt.clf()

#4. Bar Plot (막대 그래프)
#4-1. 기본 Bar Plot (카테고리 A~E, 값 비교) 
l = ['A', 'B', 'C', 'D', 'E']
v = [7, 3, 6, 2, 5]
plt.bar(l, v)
plt.title('bar')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q4_1.png')
plt.clf()

#4-2. 세부 세팅 Bar Plot (width=0.4, bottom=2, color='lightblue', edgecolor='blue') 
l = ['1', '2', '3', '4', '5']
v = [7, 3, 6, 2, 5]
plt.bar(l, v, width = 0.4, bottom=2, align='center', color='lightblue', edgecolor='blue')
plt.title('bar_setteing')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q4_2.png')
plt.clf()

#5. Pie Chart (원형 차트)
#5-1. 기본 Pie Chart (autopct='%1.1f%%') 
l = ['1', '2', '3', '4']
v = [15, 30, 45, 10]
plt.pie(v, labels=l, autopct='%1.1f%%')
plt.title('pie')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q5_1.png')
plt.clf()

#5-2. 세부 세팅 Pie Chart (explode=(0, 0.1, 0, 0), shadow=True, startangle=90, ax1.axis('equal')) 
l = ['1', '2', '3', '4']
v = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0) 
fig1, ax1 = plt.subplots()
ax1.pie(v, explode=explode, labels=l, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')  
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q5_2.png')
plt.clf()

#6. Box Plot (상자 수염 그림)

#6-1. 기본 Box Plot (난수 1000개 분포) 
data = np.random.randn(1000)
plt.boxplot(data)
plt.title('Box Plot')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q6_1.png')
plt.clf()

#6-2. 세부 세팅 Box Plot (4개 그룹 데이터, patch_artist=True, notch=True, vert=0 수평 배치) 
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
bp = ax.boxplot(data, patch_artist = True, notch = True, vert = 0)
plt.title("Customized box plot")
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q6_2.png')
plt.clf()

#7. Error Bar (오차 막대)

#7-1. 기본 Error Bar (y = x**2, yerr=errors, fmt='o') 
x = np.linspace(0, 10, 10)
y = x ** 2
errors = np.random.rand(10) * 5
plt.errorbar(x, y, yerr=errors, fmt='o')
plt.title('Error Bar')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q7_1.png')
plt.clf()

#7-2. 세부 세팅 Error Bar (y = sin(x) + dy * randn, fmt='.k', ecolor='lightgray', elinewidth=3) 
x = np.linspace(0, 10, 10)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(10)
plt.errorbar(x, y, yerr=dy, fmt='.k', ecolor='lightgray', elinewidth=3)
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q7_2.png')
plt.clf()


#8. Contour Plot (등고선 플롯)

#8-1. 기본 Contour Plot (meshgrid 생성, Z = sin(sqrt(X^2 + Y^2)), contourf) 
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contourf(X, Y, Z, cmap='viridis')
plt.title('Contour Plot')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q8_1.png')
plt.clf()


#8-2. 세부 세팅 Contour Plot (Z = sqrt(X^2 + Y^2), levels=20, cmap='RdGy') 
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)
plt.contourf(X, Y, Z, levels=20, cmap='RdGy')
plt.title('Contour Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q8_2.png')
plt.clf()


from mpl_toolkits.mplot3d import Axes3D

#9. 3D Plot (3차원 서피스)

#9-1. 기본 3D Surface (Axes3D, projection='3d', plot_surface) 
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title('3D Plot')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q9_1.png')
plt.clf()


#9-2. 세부 세팅 3D Surface (rstride=1, cstride=1, edgecolor='none') 
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_title('Surface Plot')
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day2\q9_2.png')
plt.clf()
