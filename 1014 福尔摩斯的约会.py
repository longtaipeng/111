"""
大侦探福尔摩斯接到一张奇怪的字条：我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm。
大侦探很快就明白了，字条上奇怪的乱码实际上就是约会的时间星期四 14:04，因为前面两字符串中第 1 对相同的大写英
文字母（大小写有区分）是第 4 个字母 D，代表星期四；第 2 对相同的字符是 E ，那是第 5 个英文字母，代表一天里的
第 14 个钟头（于是一天的 0 点到 23 点由数字 0 到 9、以及大写字母 A 到 N 表示）；后面两字符串第 1 对相同的英文字
母 s 出现在第 4 个位置（从 0 开始计数）上，代表第 4 分钟。现给定两对字符串，请帮助福尔摩斯解码得到约会的时间。
"""

a = input()
b = input()
c = input()
d = input()
list_1 = []
num = 0
week = {'A': 'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI', 'F': 'SAT', 'G': 'SUN'}
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'i', 'J', 'K', 'L', 'M', 'N']

for i in range(min(len(a), len(b))):
    if a[i] == b[i]:
        if a[i].isupper():
            list_1.append(a[i])
    if len(list_1) == 2:
        break

for i in range(min(len(c), len(d))):
    if c[i] == d[i]:
        if c[i].isalpha():
            num = i + 1
            list_1.append(c[i])
            break
print('{} {:02d}:{:02d}'.format(week[list_1[0]], time.index(list_1[1]), i))
