a = list(map(int, input().split(' ')))
count = 0
for i in [0, 3, 6, 1, 4, 7, 2, 5, 8]:
    print(' {:4d}'.format(a[i]), end='')
    count += 1
    if count % 3 == 0:
        print('')