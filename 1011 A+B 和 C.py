# 给定区间 [−2​31​​,2​31​​] 内的 3 个整数 A、B 和 C，请判断 A+B 是否大于 C。

n = int(input())
k = {}
for i in range(0, n):
    k[i] = input().split()

for key, value in k.items():
    if int(value[0]) + int(value[1]) > int(value[2]):
        print('Case #{}: true'.format(key+1))
    else:
        print('Case #{}: false'.format(key+1))