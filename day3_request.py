import matplotlib.pyplot as plt
import numpy as np

#Q1. Figure 기본 속성 설정

#$x in [0, 2pi]$ (100개 구간) 데이터 생성
#plt.figure() 옵션 적용: figsize=(10, 5), dpi=100, facecolor='lightgray'
#$y =sin(x)$ 그래프 작성 (타이틀 'Sine Wave', x/y 축 레이블 설정)
#result_day3_q1.png 이미지 저장

x = np.linspace(0, 2*np.pi, 100)
plt.figure(figsize=(10, 5), dpi=100, facecolor='lightgray')
y= np.sin(x)

plt.title("Sine Wave")
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x, y)
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day3\result_day3_q1.png')
plt.clf()


#Q2. plt.subplots() 2x2 그리드 배열

#각 위치별 그래프 작성:

#axs.flat 반복문으로 축 레이블 설정 및 plt.tight_layout() 조절
#result_day3_q2.png 이미지 저장

x = np.linspace(0, 2*np.pi, 100)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, np.sin(x))
axs[0, 1].plot(x, np.cos(x))
axs[1, 0].plot(x, np.sin(2*x))
axs[1, 1].plot(x, np.cos(2*x))

for i in axs.flat:
    i.set(xlabel='x value', ylabel='function values')
    i.label_outer()

plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day3\result_day3_q2.png')
plt.clf()


#Q3. add_subplot() 응용 (극좌표 & 축 공유)

#fig = plt.figure(figsize=(10, 8)) 생성
#서브플롯 3개 구성:
#ax1: add_subplot(2, 2, 1, projection='polar') $\rightarrow$ $y = \sin(x^2)$
#ax2: add_subplot(2, 2, 2) $\rightarrow$ $y = \sin(x^2)$
#ax3: add_subplot(2, 1, 2, sharex=ax2) $\rightarrow$ $y = \cos(x^2)$ (ax2와 x축 공유)
#각 플롯 타이틀 지정 및 plt.tight_layout() 조절
#result_day3_q3.png 이미지 저장

fig = plt.figure(figsize=(10, 8))
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x**2)
y2 = np.cos(x**2)


ax1 = fig.add_subplot(2, 2, 1, projection='polar')
ax1.plot(x, y1)
ax1.set_title("Polar: sin(x^2)")

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, y1)
ax2.set_title("sin(x^2)")

ax3 = fig.add_subplot(2, 1, 2, sharex=ax2)
ax3.plot(x, y2)
ax3.set_title("cos(x^2)")

plt.tight_layout()
plt.savefig(r'C:\Users\kimji\OneDrive\Desktop\personal_project\study\day3\result_day3_q3.png')
plt.clf()