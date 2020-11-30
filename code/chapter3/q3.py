import sys
import numpy as np

A = [[31, -13, 0, 0, 0, -10, 0, 0, 0],
    [-13, 35, -9, 0, -11, 0, 0, 0, 0],
    [0, -9, 31, -10, 0, 0, 0, 0, 0],
    [0, 0, -10, 79, -30, 0, 0, 0, -9],
    [0, 0, 0, -30, 57, -7, 0, -5, 0],
    [0, 0, 0, 0, -7, 47, -30, 0, 0],
    [0, 0, 0, 0, 0, -30, 41, 0, 0],
    [0, 0, 0, 0, -5, 0, 0, 27, -2],
    [0, 0, 0, -9, 0, 0, 0, -2, 29]]

b = [-15, 27, -23, 0, -20, 12, -7, 7, 10]

def find_shape(A, b):
    """
    获取 n
    """

    # n行 m列
    n1, m1 = A.shape
    n2, = b.shape

    # print(n1, m1)
    # print(n2)

    # 判断矩阵形状
    if n1 != m1 or n1 != n2:
        print('Error martix shape!')
        sys.exit()
    else:
        N = n1

    return N
    

def MGauss(A, b):
    """
    列主元 Gauss 消去 消元
    """

    # 判断矩阵形状
    N = find_shape(A, b)

    # 列主元高斯消元
    for k in range(0, N):
        p = k
        maxabs = abs(A[k, k])
        # 找列最大值
        for i in range(k+1, N):
            if abs(A[i, k]) > maxabs:
                p = i
                maxabs = abs(A[i, k])
        # print('maxabs', maxabs)
        # 最大值为 0
        if maxabs == 0:
            print('Singular')
            sys.exit()
        # 最大值不在对角线, 则交换两行
        if p != k:
            A[[p,k],:] = A[[k,p],:]
            b[[p,k]] = b[[k,p]]
        # print('exchange r{0} and r{1}:\r\n'.format(k, p), A)
        # 消元，将对角线以下变为 0
        for i in range(k+1, N):
            m_ik = A[i, k] / A[k, k]
            for j in range(0, N):
                A[i, j] -= A[k, j] * m_ik
            b[i] -= b[k] * m_ik
        # print('After Elimination:\r\n', np.concatenate((A,np.asarray([b]).T), axis = 1))
        
    if A[N-1, N-1] == 0:
        print('Singular')
        sys.exit()
    
    return A, b
        
def bring_back(A, b):
    """
    列主元 Gauss 消去 回带
    """
    
    # 判断矩阵形状
    N = find_shape(A, b)

    # 回带
    X = np.zeros(N)
    X[N-1] = b[N-1] / A[N-1, N-1]
    for i in range(0, N-1):
        k = N-2-i
        sigma = sum(A[k, j]*X[j] for j in range(k+1, N))
        # print('k:{0}, sigma:{1}'.format(k, sigma))
        X[k] = (b[k] - sigma) / A[k, k]

    return X

# 列主元高斯消去求解
def MGauss_Caculate(A, b):
    A_np = np.asarray(A, dtype = float)
    b_np = np.asarray(b, dtype = float)


    # 列主元、回带
    A_G, b_G = MGauss(A_np, b_np)
    x_G = bring_back(A_G, b_G)

    # print('A_G:b_G\r\n', np.concatenate((A_G,np.asarray([b_G]).T), axis = 1))

    return x_G
        
def main():
    """
    main
    """

    x_G = MGauss_Caculate(A, b)
    print('x_G', x_G)


if __name__ == "__main__":
    main()