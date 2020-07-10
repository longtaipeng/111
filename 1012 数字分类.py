"""
给定一系列正整数，请按要求对数字进行分类，并输出以下 5 个数字：
    A​1​​ = 能被 5 整除的数字中所有偶数的和；
    A​2​​ = 将被 5 除后余 1 的数字按给出顺序进行交错求和，即计算 n​1​​−n​2​​+n​3​​−n​4​​⋯；
    A​3​​ = 被 5 除后余 2 的数字的个数；
    A​4​​ = 被 5 除后余 3 的数字的平均数，精确到小数点后 1 位；
    A​5​​ = 被 5 除后余 4 的数字中最大数字。
"""
a = list(map(int, input().split(' ')))
flag = a.pop(0)
A = []
A1 = []
A2 = []
A3 = []
A4 = []
A5 = []
sum1 = 0
sum2 = 0
count = 0
for i in a:
    if i % 5 == 0:
        A1.append(i)
    elif i % 5 == 1:
        A2.append(i)
    elif i % 5 == 2:
        A3.append(i)
    elif i % 5 == 3:
        A4.append(i)
    elif i % 5 == 4:
        A5.append(i)

if A1:
    for n in A1:
        if n % 2 == 0:
            sum1 += n
    A.append(sum1)
else:
    A.append('N')

if A2:
    for n in range(len(A2)):
        if n % 2 == 0:
            sum2 += A2[n]
        else:
            sum2 -= A2[n]
    A.append(sum2)
else:
    A.append('N')

if A3:
    A.append(len(A3))
else:
    A.append('N')

if A4:
    A.append(round(sum(A4)/len(A4), 1))
else:
    A.append('N')

if A5:
    A.append(max(A5))
else:
    A.append('N')

print(' '.join(str(A1) for A1 in A ))