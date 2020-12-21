'''
Author: your name
Date: 2020-12-21 08:48:26
LastEditTime: 2020-12-21 14:47:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /numerical_analysis/code/chapter5/q3.py
'''
import math
import sympy

Tn_buff = []
Sn_buff = []
Cn_buff = []
Rn_buff = []

'''
description: 递推关系求梯形公式
param {*} f 函数表达式
param {*} a 区间左端点
param {*} b 区间右端点
param {*} n_2 本次的n
param {*} Tn 上次的 T_n
return {*} T_2n 本次结果
'''
def Com_Trapezoid_Int(f, a, b, n_2=1, Tn=0):
    if n_2 == 1:
        T2n = 0.5*(b-a)*(f(a)+f(b))
    else:
        x_halfk = [a+(1+2*k)*(b-a)/n_2 for k in range(0, int(n_2/2))]
        T2n = 0
        for x in x_halfk:
            T2n = T2n + f(x)
        T2n = 0.5*Tn + (b-a)*T2n/n_2
    return T2n
    
'''
description: 利用低阶梯形公式求 Simpson
param {*} T2n 复化梯形公式 2n 结果
param {*} Tn 复化梯形公式 n 结果
return {*} Simpson Sn 结果
'''
def Com_Simpson_Int(T2n, Tn):
    Sn = 4.0*T2n/3.0 - Tn/3.0
    return Sn

'''
description: 利用低阶 Simpson 公式求 Cotes
param {*} S2n 复化 Simpson 公式 2n 结果
param {*} Sn 复化 Simpson 公式 n 结果
return {*} Cotes Cn 结果
'''
def Com_Cotes_Int(S2n, Sn):
    Cn = 16.0*S2n/15.0 - Sn/15.0
    return Cn

'''
description: 利用低阶 Cotes 公式求 Romberg
param {*} C2n 复化 Cotes 公式 2n 结果
param {*} Cn 复化 Cotes 公式 n 结果
return {*} Romberg Rn 结果
'''
def Com_Romberg_Int(C2n, Cn):
    Rn = 64.0*C2n/63.0 - Cn/63.0
    return Rn

'''
description: 判断误差限
param {*} R2n
param {*} Rn
param {*} err
return {*}
'''
def Is_Smaller_Than_Romberg_Error(R2n, Rn, err):
    if abs(R2n - Rn) <= abs(255.0*err):
        return True
    else:
        return False

def Get_Trapezoid(f, a, b, n):
    global Tn_buff
    i = int(math.log(n, 2))
    if len(Tn_buff)-1 >= i:
        return Tn_buff[i]
    else:
        Tn_last = -1
        if n/2 >= 1:
            Tn_last = Get_Trapezoid(f, a, b, n/2)
        Tn = Com_Trapezoid_Int(f, a, b, n, Tn_last)

        if len(Tn_buff) == i:
            Tn_buff.append(Tn)
            return Tn_buff[i]
        else:
            print("Error List Index (Get_Trapezoid)!!!, i = {0}, len(Tn_buff) = {1}".format(i, len(Tn_buff)))
            return -1

def Get_Simpson(f, a, b, n):
    global Sn_buff
    i = int(math.log(n, 2))
    if len(Sn_buff)-1 >= i:
        return Sn_buff[i]
    else:
        if n/2 >= 1:
            Get_Simpson(f, a, b, n/2)
        Tn = Get_Trapezoid(f, a, b, n)
        T2n = Get_Trapezoid(f, a, b, 2*n)
        Sn = Com_Simpson_Int(T2n, Tn)
        if len(Sn_buff) == i:
            Sn_buff.append(Sn)
            return Sn_buff[i]
        else:
            print("Error List Index (Get_Simpson)!!!, i = {0}, len(Sn_buff) = {1}".format(i, len(Sn_buff)))
            return -1

def Get_Cotes(f, a, b, n):
    global Cn_buff
    i = int(math.log(n, 2))
    if len(Cn_buff)-1 >= i:
        return Cn_buff[i]
    else:
        if n/2 >= 1:
            Get_Cotes(f, a, b, n/2)
        Sn = Get_Simpson(f, a, b, n)
        S2n = Get_Simpson(f, a, b, 2*n)
        Cn = Com_Cotes_Int(S2n, Sn)
        if len(Cn_buff) == i:
            Cn_buff.append(Cn)
            return Cn_buff[i]
        else:
            print("Error List Index (Get_Cotes)!!!, i = {0}, len(Cn_buff) = {1}".format(i, len(Cn_buff)))
            return -1

def Get_Romberg(f, a, b, n):
    global Rn_buff
    i = int(math.log(n, 2))
    if len(Rn_buff)-1 >= i:
        return Rn_buff[i]
    else:
        if n/2 >= 1:
            Get_Romberg(f, a, b, n/2)
        Cn = Get_Cotes(f, a, b, n)
        C2n = Get_Cotes(f, a, b, 2*n)
        Rn = Com_Romberg_Int(C2n, Cn)
        if len(Rn_buff) == i:
            Rn_buff.append(Rn)
            return Rn_buff[i]
        else:
            print("Error List Index (Get_Romberg)!!!, i = {0}, len(Rn_buff) = {1}".format(i, len(Rn_buff)))
            return -1

def Caculate_Romberg(f, a, b, err):
    n = 2
    Get_Romberg(f, a, b, n)
    while Is_Smaller_Than_Romberg_Error(Rn_buff[-1], Rn_buff[-2], err) == False:
        n = n*2
        Get_Romberg(f, a, b, n)
    return n


def expression0(x):
    return 1.0/x

def main():
    # Get_Romberg(expression0, 2, 8, 2)
    # print('\nTn_buff:\t', Tn_buff, '\nSn_buff:\t', Sn_buff, '\nCn_buff:\t', Cn_buff, '\nSn_buff:\t', Rn_buff)
    n = Caculate_Romberg(expression0, 2, 8, 0.5*pow(10, -7))
    print("n = ", n)
    print('\nTn_buff:\t', Tn_buff, '\nSn_buff:\t', Sn_buff, '\nCn_buff:\t', Cn_buff, '\nSn_buff:\t', Rn_buff)

if __name__ == "__main__":
    main()
