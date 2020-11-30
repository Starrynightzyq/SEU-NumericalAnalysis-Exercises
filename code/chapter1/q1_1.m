%% 习题1 第17题
% 课本 P20
clc
clear

prompt = '请输入 N: ';
N = input(prompt);

data0 = SN_Real(N);
data1 = SN_1(N);
data2 = SN_2(N);
fprintf('准确值:\t%.10f\n', data0);
fprintf('正向求和:\t%.10f, 误差: %.10f\n', data1, abs(data0 - data1));
fprintf('反向求和:\t%.10f, 误差: %.10f\n', data2, abs(data0 - data2));

%% 画图
clc
clear

prompt = '请输入 N: ';
N = input(prompt);
N_start = 101;

x = N_start:N;
y1 = zeros(1, (N-N_start+1));
y2 = zeros(1, (N-N_start+1));

tic
for i = x
    data0 = SN_Real(i);
    data1 = SN_1(i);
    data2 = SN_2(i);
%     y1(i - N_start + 1) = abs(data0 - data1);
%     y2(i - N_start + 1) = abs(data0 - data2);
    y1(i - N_start + 1) = (data0 - data1);
    y2(i - N_start + 1) = (data0 - data2);
end
toc

figure
plot(x, y1, x, y2);
legend('从大到小', '从小到大');
title('误差（准确值-计算值）')
xlabel('N');
ylabel('e');

saveas(gcf,'e.jpg')%保存图像为文件

%% ----------------------
function res = f(N)
%f - 1/(N^2 - 1)
%
% Syntax: res = f(N)
%
% 
    res = single(1/(N^2 - 1));
end

function sum = SN_1(N)
%SN_1 - sum f(a), a from 2 to N
%
% Syntax: res = SN_1(N)
%
% 正向求和，从 2 到 N
    sum = 0;
    for i = 2:N
        sum = sum + f(i);
    end
    sum = single(sum);
end

function sum = SN_2(N)
%SN_2 - sum f(a), a from N to 2
%
% Syntax: sum = SN_2(N)
%
% 反向求和，从 N 到 2
    sum = 0;
    for i = 2:N
        sum = sum + f(N-i+2);
    end
    sum = single(sum);
end

function sum = SN_Real(N)
%准确值
    sum = single((3/2 - (1/N) - (1/(N-1)))/2);
end


