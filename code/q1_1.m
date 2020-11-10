%% 习题1 第17题
% 课本 P20
clc
clear


data1_10_2 = SN_1(10);
data2_10_2 = SN_2(10);
fprintf('正向求和：2-10^2, sum is: %.10f\r\n', data1_10_2);
fprintf('反向求和：10^2-2, sum is: %.10f\r\n', data2_10_2);


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
    sum = single(0);
    for i = 2:N
        sum = sum + f(i);
%         disp(i);
    end
end

function sum = SN_2(N)
%SN_2 - sum f(a), a from N to 2
%
% Syntax: sum = SN_2(N)
%
% 反向求和，从 N 到 2
    sum = single(0);
    for i = 2:N
        sum = sum + f(N-i+2);
        % disp(N-i+2);
    end
end


