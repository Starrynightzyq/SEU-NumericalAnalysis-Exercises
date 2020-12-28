'''
Author: your name
Date: 2020-12-28 15:13:05
LastEditTime: 2020-12-28 15:31:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /numerical_analysis/code/chapter5/q3_plot.py
'''
import os
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np

#定义坐标轴函数
def setup_axes(fig, rect):
    ax = axisartist.Subplot(fig, rect)
    fig.add_axes(ax)

    ax.set_ylim(0, 20)
    #自定义刻度
#    ax.set_yticks([-10, 0,9])
    ax.set_xlim(0,1.5)
    ax.axis[:].set_visible(False)

	#第2条线，即y轴,经过x=0的点
    ax.axis["y"] = ax.new_floating_axis(1, 0)
    ax.axis["y"].set_axisline_style("-|>", size=1.5)
#    第一条线，x轴，经过y=0的点
    ax.axis["x"] = ax.new_floating_axis(0, 0)
    ax.axis["x"].set_axisline_style("-|>", size=1.5)

    return(ax)

#设置画布
fig = plt.figure(figsize=(8, 8)) #建议可以直接plt.figure()不定义大小
ax1 = setup_axes(fig, 111)
ax1.axis["x"].set_axis_direction("bottom")
ax1.axis['y'].set_axis_direction('right')

#在已经定义好的画布上加入三角函数
x = np.arange(0,1.5,0.001)
y = np.arctan(x)/np.power(x, 3/2)
plt.plot(x,y)
plt.text(1, 10, r"$\frac{\mathrm{arctan}x}{x^{3/2}}$", horizontalalignment='center', fontsize=20)

# plt.show()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fq3.png'), dpi=300)
