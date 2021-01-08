'''
Author: your name
Date: 2020-12-21 17:15:07
LastEditTime: 2021-01-08 22:56:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /numerical_analysis/code/chapter5/q3_gauss_legendre.py
'''
import time
import math
import os, sys

RESULT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'q3_gauss_legendre_result.txt')

def Gauss_Legendre(f, a, b):
    Int = (b-a) * (5.0 * f(0.5*(a+b-(b-a)*pow(3.0/5.0, 0.5))) + \
        8.0 * f(0.5*(a+b)) + 5.0 * f(0.5*(a+b+(b-a)*(pow(3.0/5.0, 0.5))))) / (9.0*2.0)
    return Int

def Com_Gauss_Legendre(f, a, b, n):
    h = (b-a)/n
    Int_Sum = 0.0
    for i in range(1, n+1):
        x0 = a + (i - 1.0) * h
        x1 = a + i * h
        Int_Sum += Gauss_Legendre(f, x0, x1)
    return Int_Sum

def Get_Com_Gauss_Legendre(f, a, b, err):
    Int_Last = 0
    i = 0
    while True:
        Int = Com_Gauss_Legendre(f, a, b, 2 ** i)

        print('n: {0}, {1}'.format(2**i, Int))
        with open(RESULT_FILE, "a+") as fo:
            fo.write('n: {0}, {1} \n'.format(2**i, Int))

        if abs(Int - Int_Last) <= err:
            return Int, i
        else:
            Int_Last = Int
            i += 1
    
def expression0(x):
    return math.exp(-1 * x ** 2)

def expression1(x):
    return math.atan(x)/(pow(x, 1.5))

def main():
    print('int3')
    int3, n3 = Get_Com_Gauss_Legendre(expression1, 1e-5, 1, (0.5e-7)/6.0) # 
    print('int2')
    int2, n2 = Get_Com_Gauss_Legendre(expression1, 1e-10, 1e-5, (0.5e-7)/6.0) #
    print('int1')
    int1, n1 = Get_Com_Gauss_Legendre(expression1, 0, 1e-10, (0.5e-7)/6.0) # 100.0
    int_all = int1+int2+int3
    n_times = 2**(n1+n2+n3)
    print('result is {0} , n is {1}'.format(int_all, n_times))
    with open(RESULT_FILE, "a+") as fo:
        fo.write('result is {0} , n is {1}'.format(int_all, n_times))
        fo.write('\n')

if __name__ == "__main__":
    time_start = time.time()
    if os.path.exists(RESULT_FILE):
        os.remove(RESULT_FILE)
    main()
    time_end=time.time()
    print('time cost {0} s. '.format(time_end - time_start))
    with open(RESULT_FILE, "a+") as fo:
        fo.write('time cost {0} s. \n'.format(time_end - time_start))