# 本题要求统计一个整型序列中出现次数最多的整数及其出现次数。
n = list(map( int, input().split(' ')))
num = {}
for i in n[1:]:
    if i not in num.keys():
        num[i] = 1
    else:
        num[i] += 1

max_num = max(num, key=num.get)
print(max_num, num[max_num])