'''
正整数 A 的“D​A​​（为 1 位整数）部分”定义为由 A 中所有 D​A​​ 组成的新整数 P​A​​。
例如：给定 A=3862767，D​A​​=6，则 A 的“6 部分”P​A​​ 是 66，因为 A 中有 2 个 6。
现给定 A、D​A​​、B、D​B​​，请编写程序计算 P​A​​+P​B​​。
'''

a = input().split(' ')
p1 = a[0]; p2 = a[2]
n1 = int(a[1]); n2 = int(a[3])
str1, str2 = '', ''
for i in p1:
    if int(i) == n1:
        str1 += i

for i in p2:
    if int(i) == n2:
        str2 += i

if not str1:
    str1 = 0
if not str2:
    str2 = 0
print(int(str1)+int(str2))
