'''
Author: zyq
Date: 2020-11-30 17:19:51
LastEditTime: 2020-11-30 22:55:47
LastEditors: Please set LastEditors
Description: 数值分析上机题 课本 P195 37题 3次样条插值
FilePath: /code/chapter4/q4-37-1.py
'''
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import sys, os

'''
description: 
param {*} x n+1 个插值点
param {*} y n+1 个插值点
return {*} n
'''
def Prejudgment(x, y):
    n1 = len(x)
    n2 = len(y)
    if n1 != n2:
        print('x 与 y 长度不相等')
        sys.exit()
    
    n = n1-1
    return n
        

'''
description: 求三次样条差值的 4n 个方程
param: {x[0,n], y[0,n]} n+1 个插值点
param: Type 三次样条边界条件 1 or 2 or 3
return {A, B} [a0 b0 c0 d0 a1 b1 c1 d1 ... a(n-1) b(n-1) c(n-1) d(n-1)] = [B] 形式的方程组 
'''
def calculateEquationParameters(x, y, Type=1, dy0=0, dyn=0):
    n = Prejudgment(x, y)

    parameterA = []
    parameterB = []
    
    # S_i(x_i) = y_i
    # S_i(x_{i+1}) = y_{i+1}
    # 0 <= i <= n-1
    for i in range(0, n):
        # S_i(x_i) = y_i
        data = np.zeros(n*4)
        data[i*4] = pow(x[i], 3)
        data[i*4+1] = pow(x[i], 2)
        data[i*4+2] = x[i]
        data[i*4+3] = 1
        parameterA.append(data.tolist())
        parameterB.append(y[i])
        
        # S_i(x_{i+1}) = y_{i+1}
        data1 = np.zeros(n*4)
        data1[i*4] = pow(x[(i+1)], 3)
        data1[i*4+1] = pow(x[(i+1)], 2)
        data1[i*4+2] = x[(i+1)]
        data1[i*4+3] = 1
        parameterA.append(data1.tolist())
        parameterB.append(y[i+1])

    # S'_i(x_{i+1}) = S'_{i+1}(x_{i+1})
    # 0 <= i <= n-2
    for i in range(0, n-1):
        data = np.zeros(n*4)

        data[i*4] = 3 * pow(x[i+1], 2)
        data[i*4+1] = 2 * x[i+1]
        data[i*4+2] = 1

        data[(i+1)*4] = -3 * pow(x[i+1], 2)
        data[(i+1)*4+1] = -2 * x[i+1]
        data[(i+1)*4+2] = -1
        
        parameterA.append(data.tolist())
        parameterB.append(0)

    # S''_i(x_{i+1}) = S''_{i+1}(x_{i+1})
    # 0 <= i <= n-2
    for i in range(0, n-1):
        data = np.zeros(n*4)

        data[i*4] = 6 * x[i+1]
        data[i*4+1] = 2

        data[(i+1)*4] = -6 * x[i+1]
        data[(i+1)*4+1] = -2
        
        parameterA.append(data.tolist())
        parameterB.append(0)

    if Type == 1:
        # S'_0(x_0) = y'_0
        data = np.zeros(n*4)
        data[0] = 3 * pow(x[0], 2)
        data[1] = 2 * x[0]
        data[2] = 1
        parameterA.append(data.tolist())
        parameterB.append(dy0)

        # S'_{n-1}(x_n) = y'_n
        data = np.zeros(n*4)
        data[(n-1)*4] = 3 * pow(x[n], 2)
        data[(n-1)*4+1] = 2 * x[n]
        data[(n-1)*4+2] = 1

        parameterA.append(data.tolist())
        parameterB.append(dyn)
    elif Type == 2:
        # S''(a) = S''(b) = 0

        # S''_0(x_0) = 0
        data = np.zeros(n*4)
        data[0] = 6 * x[0]
        data[1] = 2
        parameterA.append(data.tolist())
        parameterB.append(0)

        # S''_{n-1}(x_n) = 0
        data = np.zeros(n*4)
        data[(n-1)*4] = 6 * x[n]
        data[(n-1)*4+1] = 2
        parameterA.append(data.tolist())
        parameterB.append(0)

    elif Type == 3:
        # S'(a) = S'(b) and # S''(a) = S''(b)
        pass
    else:
        print('Error! Unknown "Type" Value!')


    return parameterA, parameterB

"""
功能：根据所给参数，计算三次函数的函数值：
参数：OriginalInterval为原始x的区间, parameters为二次函数的系数，x为自变量
返回值：为函数的因变量
"""
def calculate(OriginalInterval, paremeters, x):
    n = int(len(paremeters)/4)
    result=[]
    for data_x in x:

        Interval = 0
        if data_x <= OriginalInterval[0]:
            Interval = 0
        elif data_x >= OriginalInterval[-1]:
            Interval = n-1
        else:
            for i in range(0,n):
                if data_x >= OriginalInterval[i] and data_x < OriginalInterval[i+1]:
                    Interval = i
                    break

        result.append(paremeters[Interval*4+0]*data_x*data_x*data_x+paremeters[Interval*4+1]*data_x*data_x+paremeters[Interval*4+2]*data_x+paremeters[Interval*4+3])
    return result

"""
功能：将函数绘制成图像
参数：data_x,data_y为离散的点.new_data_x,new_data_y为由拉格朗日插值函数计算的值。x为函数的预测值。
返回值：空
"""
def Draw(data_x,data_y,new_data_x,new_data_y):
        plt.plot(new_data_x, new_data_y, label="拟合曲线", color="black")
        plt.scatter(data_x,data_y, label="离散数据",color="red")
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['axes.unicode_minus'] = False
        plt.title("三次样条函数")
        plt.legend(loc="upper left")
        plt.savefig('my_spline.png', dpi=300)
        plt.show()

def PrintS(parameterX):
    n = int(len(parameterX)/4)
    print('S(x) = ')
    for i in range(0, n):
        print("{0}x^3 + {1}x^2 + {2}x + {3}".format(parameterX[i*4], parameterX[i*4+1], parameterX[i*4+2], parameterX[i*4+3]))
    print('\n')
        
def main():
    x = [0,    1,    2,    3,    4,    5,    6,    7,    8,    9,    10]
    y = [2.51, 3.30, 4.04, 4.70, 5.22, 5.54, 5.78, 5.40, 5.57, 5.70, 5.80]
    dy0 = 0.8
    dyn = 0.2  
    parameterA, parameterB = calculateEquationParameters(x, y, 1, dy0, dyn)
    parameterX = MGauss_Caculate(parameterA, parameterB)

    PrintS(parameterX)

    # 画图
    new_data_x = np.arange(x[0]-0.5, x[-1]+0.6, 0.1)
    new_data_y = calculate(x, parameterX, new_data_x)
    Draw(x, y, new_data_x, new_data_y)

    # 打印
    new_data_x = np.arange(0.5, 10.5, 1)
    new_data_y = calculate(x, parameterX, new_data_x)
    # f4_5 = calculate(parameterX[8:12], [4.5])
    print(new_data_x)
    print(new_data_y)

if __name__ == "__main__":

    # 调用 chapter3 中的列主元高斯消去法
    from chapter3.q3 import MGauss_Caculate

    main()



