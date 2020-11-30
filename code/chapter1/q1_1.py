import numpy as np 
import sys
import matplotlib.pyplot as plt
import time

def f(N):
    """
    1/(N^2 -1)
    """
    # tmp = np.dtype(np.float32) # 单精度
    tmp = 1/(pow(N,2) - 1)

    return tmp

def SN_1(N):
    """
    S_N
    """
    # sum = np.dtype(np.float32) # 单精度
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
    # sum = np.dtype(np.float32) # 单精度
    sum = 0
    for i in range(2,N+1):
        # print('SN2 {0}'.format(N-i+2))
        sum = sum + f(N-i+2)
        # print('SN2 {0}, sum : {1}'.format(N-i+2,sum))

    return sum

def SN_Real(N):
    return (3/2 - (1/N) - (1/(N-1)))/2

def main(argv):
    """
    main
    """

    PLOT_FLAG = False

    if len(sys.argv) == 3 and sys.argv[2] == 'p':
        PLOT_FLAG = True
    elif len(sys.argv) != 2:
        print('请输入正确的 N!')
        sys.exit()
    
    N = int(sys.argv[1])

    # data1 = np.dtype(np.float32) # 单精度
    # data2 = np.dtype(np.float32) # 单精度

    if PLOT_FLAG == False:
        data0 = SN_Real(N)
        data1 = SN_1(N)
        data2 = SN_2(N)

        print('准确值:\t%.10f\n' % data0)
        print('正向求和:\t%.10f, 误差: %.10f\n' % (data1, abs(data0 - data1)))
        print('反向求和:\t%.10f, 误差: %.10f\n' % (data2, abs(data0 - data2)))
        print('data1 - data2: \t%.10f\n' % abs(data1 - data2))
    else:
        N_start = 101
        print('plot')
        y1 = []
        y2 = []

        time_start=time.time()
        for i in range(N_start, N):
            data0 = SN_Real(i)
            data1 = SN_1(i)
            data2 = SN_2(i)
            y1.append(data0 - data1)
            y2.append(data0 - data2)
        time_end=time.time()

        x = range(N_start, N)
        y_diff = [y1[i] - y2[i] for i in range(0,len(y1))]
        # print(x)
        plt.plot(x, y1, label="data1: from big to small") 
        plt.plot(x, y2, label="data2: from small to big") 
        plt.plot(x, y_diff, label="diff between data1 and data2")
        plt.xlabel('N')
        plt.ylabel('e')
        plt.title('e')

        # plt.show()
        plt.savefig("e{0}.png".format(N), dpi=300)
        print('time cost',time_end-time_start,'s')


if __name__ == "__main__":
    main(sys.argv[1:])