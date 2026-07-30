import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#1. 타이틀, 라벨, 범례 추가하기
#x = np.linspace(0, 10, 100) 데이터 및 y1 = np.sin(x), y2 = np.cos(x) 계산
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

#한 화면에 y1, y2 그래프 그리기 (label='sin(x)', label='cos(x)' 각각 지정)
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')

#타이틀 'Sin and Cos Graphs' 추가 (plt.title)
plt.title('Sin and Cos Graphs')

#X축 라벨 'X values', Y축 라벨 'Function values' 추가 (plt.xlabel, plt.ylabel)
plt.xlabel('X values')
plt.ylabel('Function values')

#범례 표시 (plt.legend())
plt.legend()

#result_day1-2_q1.png 파일로 저장 후 plt.clf()로 그래프 초기화
plt.savefig('result_day1-2_q1.png')
plt.clf()

#2. 색상, 선 스타일, 마커 커스텀하기
x = np.linspace(0, 10, 40)

y1 = np.sin(x) 
plt.plot(x, y1, color='red', linestyle='dashed', marker='o', label='sin(x)')

y2 = np.cos(x)
plt.plot(x, y2, color='blue', linestyle='solid', marker='s', label='cos(x)')

y3 = np.sin(x) * np.cos(x)
plt.plot(x, y3, color='green', linestyle='dashdot', marker='^', label='sin(x)*cos(x)')

#범례 표시 (plt.legend())
plt.legend()
plt.show()
#result_day1-2_q2.png 파일로 저장 후 plt.clf()로 그래프 초기화
plt.savefig('result_day1-2_q2.png')
plt.clf()

#3. 축 범위 설정하기 (xlim, ylim)
#x = np.linspace(0, 10, 100), y = np.sin(x) 그래프 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)


#X축 범위 0 ~ 2 * np.pi 로 제한 (plt.xlim)
plt.xlim(0, 2 * np.pi)

#Y축 범위 -1.5 ~ 1.5 로 제한 (plt.ylim)
plt.ylim(-1.5, 1.5)


#타이틀 'Sin Graph with Custom Axis Limits' 추가
plt.title('Sin Graph with Custom Axis Limits')

#result_day1-2_q3.png 파일로 저장
plt.savefig('result_day1-2_q3.png')
plt.clf()