n = int(input())
num = list(map(int, input().split(' ')))
age = {}
for i in num:
    if 0 <= i < 51:
        if i not in age.keys():
            age[i] = 1
        else:
            age[i] += 1


for i in sorted(age.keys()):
    print('{}:{}'.format(i, age[i]))