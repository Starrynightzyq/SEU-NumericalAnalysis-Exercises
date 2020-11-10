import numpy as np 

def f(N):
    """
    1/(N^2 -1)
    """
    tmp = np.dtype(np.float32) # 单精度
    tmp = 1/(pow(N,2) - 1)

    return tmp

def SN_1(N):
    """
    S_N
    """
    sum = np.dtype(np.float32) # 单精度
    sum = 0
    for i in range(2,N+1):
        # print('SN1 {0}'.format(i))
        sum = sum + f(i)
        # print('SN1 {0}, sum : {1}'.format(i,sum))

    return sum

def SN_2(N):
    """
    S_N
    """
    sum = np.dtype(np.float32) # 单精度
    sum = 0
    for i in range(2,N+1):
        # print('SN2 {0}'.format(N-i+2))
        sum = sum + f(N-i+2)
        # print('SN2 {0}, sum : {1}'.format(N-i+2,sum))

    return sum

def main():
    """
    main
    """
    data1_10_2 = np.dtype(np.float32) # 单精度
    data2_10_2 = np.dtype(np.float32) # 单精度
    data1_10_4 = np.dtype(np.float32) # 单精度
    data2_10_4 = np.dtype(np.float32) # 单精度
    data1_10_6 = np.dtype(np.float32) # 单精度
    data2_10_6 = np.dtype(np.float32) # 单精度

    data1_10_2 = SN_1(pow(10,2))
    data2_10_2 = SN_2(pow(10,2))
    data1_10_4 = SN_1(pow(10,4))
    data2_10_4 = SN_2(pow(10,4))
    data1_10_6 = SN_1(pow(10,6))
    data2_10_6 = SN_2(pow(10,6))
    print('N\t正向求和\t反向求和\t差值')
    print('10^2\t%.16f\t%.16f\t%.16f' % (data1_10_2, data2_10_2, (data1_10_2-data2_10_2)))
    print('10^2\t%.16f\t%.16f\t%.16f' % (data1_10_4, data2_10_4, (data1_10_4-data2_10_4)))
    print('10^2\t%.16f\t%.16f\t%.16f' % (data1_10_6, data2_10_6, (data1_10_6-data2_10_6)))
    # print('{0}\t{1:.16}\t{2:.16}\t{3:.16}'.format('10^2', data1_10_2, data2_10_2, data1_10_2-data2_10_2))
    # print('{0}\t{1:.16}\t{2:.16}\t{3:.16}'.format('10^4', data1_10_4, data2_10_4, data1_10_4-data2_10_4))
    # print('{0}\t{1:.16}\t{2:.16}\t{3:.16}'.format('10^6', data1_10_6, data2_10_6, data1_10_6-data2_10_6))
    # print('10^2 SN1 is {0}, SN2 is {1}'.format(data1_10_2,data2_10_2))
    # print('10^4 SN1 is {0}, SN2 is {1}'.format(data1_10_4,data2_10_4))
    # print('10^6 SN1 is {0}, SN2 is {1}'.format(data1_10_6,data2_10_6))

if __name__ == "__main__":
    main()