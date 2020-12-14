'''
Author: zyq
Date: 2020-12-01 09:56:13
LastEditTime: 2020-12-14 22:02:45
LastEditors: Please set LastEditors
Description: Least squares approximation, 最佳平方逼近, 上机题 3
FilePath: /numerical_analysis/code/chapter4/q4_2.py
'''
import numpy as np
import sys, os
import matplotlib.pyplot as plt
from pylab import mpl
import math

'''
description: 
param {*} x n+1 个插值点
param {*} y n+1 个插值点
return {*} n
'''
def PrejudgmentShape(x, y):
    n1 = len(x)
    n2 = len(y)
    if n1 != n2:
        print('x 与 y 长度不相等')
        sys.exit()
    
    n = n1-1
    return n

'''
description: 求最佳平方逼近的正规方程
param {*} m m次最佳平方逼近
param {*} x n个自变量x
param {*} y n个因变量y
return {*} (A, b)
'''
def GetNormalEquation(m, x, y):
    A = []
    b = []
    PrejudgmentShape(x, y)
    for j in range(0,m+1):
        AAline = []
        for i in range(0, m+1):
            tmp = np.dot(np.power(x, j), np.power(x, i))
            AAline.append(tmp)
        A.append(AAline)
        tmp = np.dot(y, np.power(x, j))
        b.append(tmp)
    return A, b

'''
description: 获取最佳平方逼近的多项式
param {*} A 正规方程系数A
param {*} b 正规方程系数b
return {*} c 多项式系数，q(x) = c0 + c1*x + c2*x^2 + ... + cm*x^m
'''
def GetExpression(A, b):
    c = MGauss_Caculate(A, b)
    return c

'''
description: 计算最佳平方逼近多项式
param {*} m m次最佳平方逼近
param {*} x n个自变量x
param {*} y n个因变量y
return {*} c 最佳平方逼近多项式系数，q(x) = c0 + c1*x + c2*x^2 + ... + cm*x^m
'''
def GetLeastSquaresApproximationExpression(m, x, y):
    A, b = GetNormalEquation(m, x, y)
    c = GetExpression(A, b)
    return c

'''
description: 计算多项式，q(x) = c0 + c1*x + c2*x^2 + ... + cm*x^m
param {*} c 最佳平方逼近多项式系数
return {*} 多项式结果
'''
def CaculateExpression(c, x):
    res = 0
    for i, ci in enumerate(c):
        res = res + ci * pow(x, i)
    return res

'''
description: 计算多项式, x form x0 to xn, q(x) = c0 + c1*x + c2*x^2 + ... + cm*x^m
param {*} c 最佳平方逼近多项式系数
param {list} xn 
return {*}
'''
def CaculateInterval(c, xn):
    res = []
    for x in xn:
        res.append(CaculateExpression(c, x))
    return res

"""
功能：将函数绘制成图像
参数：data_x, data_y 为原始值，new_data_x, new_data_y 为预测计算的值。
返回值：空
"""
def Draw(data_x,data_y,new_data_x,new_data_y, title):
    plt.plot(new_data_x, new_data_y, label="拟合曲线", color="black")
    plt.scatter(data_x,data_y, label="离散数据",color="red")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title(title)
    plt.legend(loc="upper right")
    plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), title+'.png'), dpi=300)
    plt.show()

'''
description: 计算拟合误差 Q = \Sigma_{k=1}^{n} (q(x_k) - y_k)^2 
param {*} c 最佳平方逼近多项式系数, q(x) = c0 + c1*x + c2*x^2 + ... + cm*x^m
param {*} x
param {*} y
return {*} Q
'''
def GetFittingError(c, x, y):
    Err = 0
    for n, xn in enumerate(x):
        qx = CaculateExpression(c, xn)
        Err += pow((qx - y[n]), 2)
    return Err

'''
description: 别求出其 2, 3, 4 次最佳平方逼近多项式.画出图形, 并比较拟合误差
param {*}
return {*}
'''
def Q1():
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y = [58, 50, 44, 38, 34, 30, 29, 26, 25, 24]

    result_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '最佳平方逼近_result.txt')

    if os.path.exists(result_file):
        os.remove(result_file)
    
    # 最佳平方逼近
    for m in range(2, 5):
        c = GetLeastSquaresApproximationExpression(m, x, y)
        # 画图
        new_x = np.arange(x[0]-0.5, x[-1]+0.6, 0.1)
        new_y = CaculateInterval(c, new_x)
        Draw(x, y, new_x, new_y, "{0}次最佳平方逼近".format(m))
        # 拟合误差
        FittingErr = GetFittingError(c, x, y)
        # 写入文件
        with open(result_file, "a+") as fo:
            fo.write("\n\\********************************************************\\\n")
            fo.write("{0} 次最佳平方逼近, m = {1}\n".format(m, m))
            fo.write("x = ")
            for xi in x:
                fo.write(str(xi))
                fo.write("\t")
            fo.write("\n")
            fo.write("y = ")
            for yi in y:
                fo.write(str(yi))
                fo.write("\t")
            fo.write("\n")
            fo.write("近似函数：q(x) = c0 + c1*x + c2*x^2 + ... + cm*x^m \n")
            fo.write("c = ")
            for ci in c:
                fo.write(str(format(ci, '.6g')))
                fo.write("\t")
            fo.write("\n")
            fo.write("拟合误差：{0}\n".format(format(FittingErr, '.8g')))
            fo.write("\\********************************************************\\\n")

# a+b÷x近似
def Q2_1():
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y = [58, 50, 44, 38, 34, 30, 29, 26, 25, 24]

    result_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'a+b÷x近似_result.txt')

    # a + b/x
    x1 = [1.0/xi for xi in x]
    c = GetLeastSquaresApproximationExpression(1, x1, y)
    # 画图
    new_x = np.arange(x[0]-0.5, x[-1]+0.6, 0.1)
    new_x1 = [1.0/xi for xi in new_x]
    new_y = CaculateInterval(c, new_x1)
    Draw(x, y, new_x, new_y, "a+b÷x近似")
    # 拟合误差
    FittingErr = GetFittingError(c, x1, y)
    # 写入文件
    with open(result_file, "w+") as fo:
        fo.write("\n\\********************************************************\\\n")
        fo.write("a+b÷x近似\n")
        fo.write("x = ")
        for xi in x:
            fo.write(str(xi))
            fo.write("\t")
        fo.write("\n")
        fo.write("y = ")
        for yi in y:
            fo.write(str(yi))
            fo.write("\t")
        fo.write("\n")
        fo.write("近似函数：q(x) = {} + {} / x \n".format(c[0], c[1]))
        fo.write("拟合误差：{0}\n".format(FittingErr))
        fo.write("\\********************************************************\\\n")

# a+blnx近似
def Q2_2():
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y = [58, 50, 44, 38, 34, 30, 29, 26, 25, 24]

    result_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'a+blnx近似_result.txt')

    # a + blnx
    x1 = [math.log(xi) for xi in x]
    c = GetLeastSquaresApproximationExpression(1, x1, y)
    # 画图
    new_x = np.arange(x[0]-0.5, x[-1]+0.6, 0.1)
    new_x1 = [math.log(xi) for xi in new_x]
    new_y = CaculateInterval(c, new_x1)
    Draw(x, y, new_x, new_y, "a+blnx近似")
    # 拟合误差
    FittingErr = GetFittingError(c, x1, y)
    # 写入文件
    with open(result_file, "w+") as fo:
        fo.write("\n\\********************************************************\\\n")
        fo.write("a+blnx近似\n")
        fo.write("x = ")
        for xi in x:
            fo.write(str(xi))
            fo.write("\t")
        fo.write("\n")
        fo.write("y = ")
        for yi in y:
            fo.write(str(yi))
            fo.write("\t")
        fo.write("\n")
        fo.write("近似函数：q(x) = {} + {} ln(x) \n".format(c[0], c[1]))
        fo.write("拟合误差：{0}\n".format(FittingErr))
        fo.write("\\********************************************************\\\n")

'''
description: 计算拟合误差 Q = \Sigma_{k=1}^{n} (q(x_k) - y_k)^2 
param {*} c 最佳平方逼近多项式系数, q(x) = a*exp(bx)
param {*} x
param {*} y
return {*} Q
'''
def GetFittingError_q2_3(c, x, y):
    Err = 0
    for n, xn in enumerate(x):
        qx1 = CaculateExpression(c, xn)
        qx = math.exp(qx1)
        Err += pow((qx - y[n]), 2)
    return Err

# a*exp(bx)近似
def Q2_3():
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y = [58, 50, 44, 38, 34, 30, 29, 26, 25, 24]

    result_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'a*exp(bx)近似_result.txt')

    # a + blnx
    y1 = [math.log(yi) for yi in y]
    c = GetLeastSquaresApproximationExpression(1, x, y1)
    # 画图
    new_x = np.arange(x[0]-0.5, x[-1]+0.6, 0.1)
    new_y1 = CaculateInterval(c, new_x)
    new_y = [math.exp(yi) for yi in new_y1]
    Draw(x, y, new_x, new_y, "a*exp(bx)近似")
    # 拟合误差
    FittingErr = GetFittingError_q2_3(c, x, y)
    # 写入文件
    with open(result_file, "w+") as fo:
        fo.write("\n\\********************************************************\\\n")
        fo.write("a*exp(bx)近似\n")
        fo.write("x = ")
        for xi in x:
            fo.write(str(xi))
            fo.write("\t")
        fo.write("\n")
        fo.write("y = ")
        for yi in y:
            fo.write(str(yi))
            fo.write("\t")
        fo.write("\n")
        fo.write("近似函数：q(x) = {0} * exp({1} * x) \n".format(math.exp(c[0]), c[1]))
        fo.write("拟合误差：{0}\n".format(FittingErr))
        fo.write("\\********************************************************\\\n")

'''
description: 计算拟合误差 Q = \Sigma_{k=1}^{n} (q(x_k) - y_k)^2 
param {*} c 最佳平方逼近多项式系数, q(x) = 1/(a+bx)
param {*} x
param {*} y
return {*} Q
'''
def GetFittingError_q2_4(c, x, y):
    Err = 0
    for n, xn in enumerate(x):
        qx1 = CaculateExpression(c, xn)
        qx = 1.0/qx1
        Err += pow((qx - y[n]), 2)
    return Err

# 1÷(a+bx)近似
def Q2_4():
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y = [58, 50, 44, 38, 34, 30, 29, 26, 25, 24]

    result_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '1÷(a+bx)近似_result.txt')

    # a + blnx
    y1 = [1.0/yi for yi in y]
    c = GetLeastSquaresApproximationExpression(1, x, y1)
    # 画图
    new_x = np.arange(x[0]-0.5, x[-1]+0.6, 0.1)
    new_y1 = CaculateInterval(c, new_x)
    new_y = [1.0/yi for yi in new_y1]
    Draw(x, y, new_x, new_y, "1÷(a+bx)近似")
    # 拟合误差
    FittingErr = GetFittingError_q2_4(c, x, y)
    # 写入文件
    with open(result_file, "w+") as fo:
        fo.write("\n\\********************************************************\\\n")
        fo.write("1÷(a+bx)近似\n")
        fo.write("x = ")
        for xi in x:
            fo.write(str(xi))
            fo.write("\t")
        fo.write("\n")
        fo.write("y = ")
        for yi in y:
            fo.write(str(yi))
            fo.write("\t")
        fo.write("\n")
        fo.write("近似函数：q(x) = 1 ÷ ( {0} + {1} * x) \n".format(math.exp(c[0]), c[1]))
        fo.write("拟合误差：{0}\n".format(FittingErr))
        fo.write("\\********************************************************\\\n")

def main():
    Q1()
    Q2_1()
    Q2_2()
    Q2_3()
    Q2_4()

if __name__ == "__main__":

    # 获取当前文件路径
    current_path = os.path.abspath(__file__)
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(current_path), '../')))
    # print(sys.path)
    # 调用 chapter3 中的列主元高斯消去法
    from chapter3.q3 import MGauss_Caculate

    main()