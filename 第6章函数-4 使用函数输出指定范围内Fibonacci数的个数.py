def fib(n):
    a, b = 1, 1
    while n-1 > 0:
        a, b = b, a+b
        n -= 1
    return b

def printFN(m, n):
    list1 = list(range(m, n + 1))
    list2 = list()
    key = n
    i = 1
    while True:
        if fib(i) in list1:
            list2.append(int(fib(i)))
        if fib(i) >= key:
            break
        i += 1
