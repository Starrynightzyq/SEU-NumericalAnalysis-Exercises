'''
Author: your name
Date: 2020-12-21 15:14:01
LastEditTime: 2020-12-21 22:14:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /numerical_analysis/code/chapter5/romberg_test.py
'''
# from math import sqrt, exp, pi
import math
import time
import os, sys

RESULT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'q3_romberg_result.txt')

def print_row(lst, n):
    print('n =: ', n, ', ',' '.join('%11.8f, ' % x for x in lst))
    with open(RESULT_FILE, "a+") as fo:
        fo.write('n: {0}, '.format(n))
        fo.write(''.join('%11.8f, ' % x for x in lst))
        fo.write('\n')


def romberg(f, a, b, eps=1e-8):
    """Approximate the definite integral of f from a to b by Romberg's method.
    eps is the desired accuracy."""
    R = [[0.5 * (b - a) * (f(a) + f(b))]]  # R[0][0]
    print_row(R[0], 1)
    n = 1
    while True:
        h = float(b - a) / 2 ** n
        R_row_tmp = []
        R_row_tmp_0 = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1))
        R_row_tmp.append(R_row_tmp_0)
        for m in range(1, min(n, 3)+1):
            tmp = R_row_tmp[m-1] + (R_row_tmp[m-1] - R[n-1][m-1]) / (4 ** m - 1)
            R_row_tmp.append(tmp)
        R.append(R_row_tmp)
        print_row(R[n], 2**n)
        if n >= 4 and abs(R[n-1][3] - R[n][3])/255.0 < eps:
            return R[n][-1]
        n += 1

'''
description: 处理反常积分奇异点为 0 的情况，返回
return {*} 
'''
def Improper_deal(f, a, b, err=1e-8):
    m = 2
    x = a + (b-a)/m
    while 2.0*f(x)*x > err:
        m = m * 2.0
        x = a + (b-a)/m
    return x

def expression0(x):
    return 1.0/x

def expression1(x):
    return math.atan(x)/(pow(x, 1.5))

def main():
    a = Improper_deal(expression1, 0, 1, (0.5e-2)/2.0)
    print(a)
    romberg(expression1, a, 1, (0.5e-2)/2.0)

if __name__ == "__main__":
    time_start = time.time()
    if os.path.exists(RESULT_FILE):
        os.remove(RESULT_FILE)
    main()
    time_end=time.time()
    print('time cost {0} s. '.format(time_end - time_start))
    with open(RESULT_FILE, "a+") as fo:
        fo.write('time cost {0} s. \n'.format(time_end - time_start))
