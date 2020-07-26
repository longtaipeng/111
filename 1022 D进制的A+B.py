a = list(map(int, input().split(' ')))
num = a[0] + a[1]
num1 = []
while num != 0:
    num1.append(num%a[2])
    num = num//a[2]

num2 = [str(i) for i in reversed(num1)]
print(''.join(num2))
