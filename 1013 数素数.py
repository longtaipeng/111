"""
输出从 P​M​​ 到 P​N​​ 的所有素数，每 10 个数字占 1 行，其间以空格分隔，但行末不得有多余空格。
"""
from math import sqrt


def prime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


n, m = map(int, input().split(' '))
prime_list = [0]
first_number = 2
last_number = 100
while len(prime_list) < m:
    for q in range(first_number, last_number):
        if prime(q):
            prime_list.append(q)
    first_number = last_number
    last_number += 7

prime_list = prime_list[n:m+1]

for i in range(len(prime_list)//10+1):
    print(' '.join(str(a) for a in prime_list[i*10:i*10+10]))