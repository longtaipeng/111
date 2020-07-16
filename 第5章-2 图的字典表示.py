n = int(input())
num = 0
sum = 0
for i in range(n):
    s = eval(input())
    for key, value in s.items():
        m = value
        for key, value in m.items():
            num += 1
            sum += value
print('{} {} {}'.format(n, num, sum))