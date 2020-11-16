#include <iostream>
#include <iomanip>
#include <math.h>

float f(int N) {
    float res = 0;
    res = float(1.0)/(pow(float(N), float(2)) - 1);
    return res;
}

float SN_1(int N) {
    float sum = 0;
    for (int i = 2; i <= N; i++)
    {
        sum += f(i);
    }
    return sum;
}

float SN_2(int N) {
    float sum = 0;
    for (int i = N; i >= 2; i--)
    {
        sum += f(i);
    }
    return sum;
}

float SN_Real(int N) {
    double sum = 0.0;
    // sum = float(0.5)*(float(1.5) - float(1.0)/float(N) - float(1.0)/float(N+1.0));
    sum = 0.5*(1.5 - 1.0/double(N) - 1.0/double(N+1.0));
    return sum;
}

int main() {
    float data0 = 0.0;
    float data1 = 0.0;
    float data2 = 0.0;

    int N = 0;

    std::cout<<"请输入N:"<<std::endl;
    std::cin>>N;

    data0 = SN_Real(N);
    data1 = SN_1(N);
    data2 = SN_2(N);

    std::cout<<"N\t精确值\t\t从大到小\t误差1   \t从小到大\t误差2"<<std::endl;
    std::cout<<N<<"\t"<< std::fixed << std::setprecision(16)<<data0<<"\t"<<data1<<"\t"<<abs(data0-data1)<<"\t"<<data2<<"\t"<<abs(data0-data2)<<std::endl;

    // printf("          value                              error\r\n");
    // printf("准确值:   %.24f\r\n", data0);
    // printf("从大到小: %.24f, 误差: %.24f\r\n", data1, abs(data0-data1));
    // printf("从大到小: %.24f, 误差: %.24f\r\n", data2, abs(data0-data2));

    return 0;
}